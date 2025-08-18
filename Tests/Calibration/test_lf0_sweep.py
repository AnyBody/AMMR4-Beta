from pathlib import Path
from itertools import product
from collections import ChainMap
from anypytools import AnyPyProcess, macro_commands as mc
from anypytools.abcutils import AnyPyProcessOutputList
from anypytools.tools import winepath, ON_WINDOWS
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd

import pytest

MODEL_FILE = "test_calibration_lowerbody.any"
OPERATION = "Main.HumanModel.Calibration.CalibrationSequence"
AMS_VARIABLES = [
    # "Main.HumanModel.BodyModel.Right.Leg.Data.RangeOfMotion.Ankle.MaxPlantarFlexionAngle",
    # "Main.HumanModel.BodyModel.Right.Leg.Data.RangeOfMotion.Ankle.MaxDorsiFlexionAngle",
    # "Main.HumanModel.BodyModel.Right.Leg.Data.RangeOfMotion.Ankle.MaxEversionAngle",
    # "Main.HumanModel.BodyModel.Right.Leg.Data.RangeOfMotion.Ankle.MaxInversionAngle",
    # "Main.HumanModel.BodyModel.Right.Leg.Data.RangeOfMotion.Ankle.NumOfPoints",
    "Main.HumanModel.Calibration.RightCal6Ankle.Ankle.Data",
    "Main.HumanModel.Calibration.RightCal6Ankle.SubTalar.Data",
    "Main.HumanModel.Calibration.RightCal6Ankle.MuscleArr",
    "Main.HumanModel.Calibration.RightCal6Ankle.Output.Lmt"
]

DEFINES_COMBINATIONS = product(
    [
        {'BM_LEG_MODEL': 1} # _LEG_MODEL_TLEM_
    ],
    [
        {'BM_CALIBRATION_TYPE': 3} # _EXPERIMENTAL_CALIBRATION_TYPE_2PAR_
    ],
    [
        {'BM_LEG_MUSCLES_BOTH': 2}, # _MUSCLES_3E_HILL_
    ],
    [
        {"TEST_NAME":"test_cal_joint_strength_0"}, # set to indicate running from test framework
    ],
)

DEFINES = [dict(**ChainMap(*defs)) for defs in DEFINES_COMBINATIONS]

def make_dump_commands(variables: list[str]) -> list[mc.MacroCommand]: 
    return [mc.Dump(var) for var in variables]


@pytest.fixture(scope="module")
def model_output() -> dict:
    """ run the models and provide the test output"""

    model = next(Path().rglob(MODEL_FILE)).resolve()

    if not ON_WINDOWS:
        model = winepath(model, "-w")

    macros = []
    for defs in DEFINES:
        macros.append(
            [
                mc.Load(model, defs=defs),
                mc.OperationRun(OPERATION),
                *make_dump_commands(AMS_VARIABLES),
            ]
        )

    app = AnyPyProcess(
        num_processes=2,
        anybodycon_path= pytest.anytest.ams_path
    )

    results = app.start_macro(macros)
    for result, defs in zip(results, DEFINES):
        if 'ERROR' in result:
            pytest.fail(f"Model had erros:\n{result['ERROR']}\n, defs: {defs}")

    return results

# def plot_lf0_sweep(muscleArr: list, lmt: list, ankleData: list, subTalarData: list) -> None:



def test_lf0_sweep(model_output: AnyPyProcessOutputList) -> None:
    """
    Test to check the lf0 when sweeping the posture space for joint.
    """
    muscleArr = model_output["MuscleArr"].flatten().tolist()
    lmt = model_output["Lmt"].squeeze()
    ankleData = model_output["Ankle.Data"]
    subTalarData = model_output["SubTalar.Data"]

    df = pd.DataFrame(lmt, columns=muscleArr)
    df.insert(0, "Ankle (deg)", ankleData.flatten() * 180 / np.pi)
    df.insert(1, "SubTalar (deg)", subTalarData.flatten() * 180 / np.pi)
    df.to_csv("lf0_sweep.csv", index=False)


def test_plot_lf0_sweep():

    df = pd.read_csv("lf0_sweep.csv")
    x_vals = df["Ankle (deg)"]
    y_vals = df["SubTalar (deg)"]
    # Create a 3D plot for each column that starts with "Main" in the DataFrame
    for col in df.columns[2:]:
        
        name = col.split('.')[-1]
        # plot setup
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_title(f" {name} Lf0 Sweep")
        plt.xlabel("Plantar Flexion(X axis)")
        plt.ylabel("Inversion (Y axis)")
        ax.grid(True)
        z_vals = df[col]

        ax.plot(x_vals, y_vals, z_vals, 'bo')

        
        fig.savefig(f"{name}_Lf0_sweep.png", dpi=300, bbox_inches='tight')
        if "FlexorHall" in name:
            plt.show()
        else:
            plt.close(fig)

    