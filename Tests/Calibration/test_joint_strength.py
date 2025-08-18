from pathlib import Path
from itertools import product, groupby
from collections import ChainMap
from anypytools import AnyPyProcess, macro_commands as mc
from anypytools.abcutils import AnyPyProcessOutputList
from anypytools.tools import winepath, ON_WINDOWS
import matplotlib.pyplot as plt

import pytest

ABS_TOL = 3
MODEL_FILE = "test_calibration_lowerbody.any"
OPERATION = "Main.HumanModel.EvalulateJointStrength.Run_all_studies"
AMS_VARIABLES = [
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.HipFlexion.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.HipExtension.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.KneeFlexion.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.KneeExtension.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.AnklePlantarFlexion.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.AnkleDorsiFlexion.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.HipAdduction.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.HipAbduction.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.HipInternalRotation.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.HipExternalRotation.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.SubTalarEversion.Study.Output.JointStrength.JointStrength",
    "Main.HumanModel.EvalulateJointStrength.Right.Leg.SubTalarInversion.Study.Output.JointStrength.JointStrength",
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
        {'BM_LEG_MUSCLES_BOTH': 1} # _MUSCLES_SIMPLE_
    ],
    [
        {"TEST_NAME":"test_cal_joint_strength_0"}, # set to indicate running from test framework
    ],
)

DEFINES = [dict(**ChainMap(*defs)) for defs in DEFINES_COMBINATIONS]


def all_equal(iterable) -> bool:
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def extract_output(output: AnyPyProcessOutputList) -> dict[str,list]:
    """ extract output variables from the model into a dict""" 
    formatted = {}
    for result in output:
        muscle_config = get_muscle_config(result["task_macro"][0])

        for var in AMS_VARIABLES:
            formatted.setdefault(f"{muscle_config}_{var.split(".")[-5]}", result[var])
    
    return formatted    


def get_muscle_config(load_string: str) -> str:
    """ get the muscle configuration from the load string"""
    if 'BM_LEG_MUSCLES_BOTH="2"' in load_string:
        return "3E"
    elif 'BM_LEG_MUSCLES_BOTH="1"' in load_string:
        return "SIMPLE"
    else:
        raise ValueError(f"Unknown muscle configuration in {load_string}")
    

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

    return extract_output(results)


def test_joint_strength(model_output: AnyPyProcessOutputList) -> None:
    
    # plot the same joint strength for each variable across different muscle configurations
    joints = [
        "HipFlexion",
        "HipExtension",
        "KneeFlexion",
        "KneeExtension",
        "AnklePlantarFlexion",
        "AnkleDorsiFlexion",
        "HipAdduction",
        "HipAbduction",
        "HipInternalRotation",
        "HipExternalRotation",
        "SubTalarEversion",
        "SubTalarInversion",
    ]
    for var in joints:
        output: dict[str, list[float]] = {key: value for key, value in model_output.items() if var in key}
        # plt.figure(figsize=(10, 6))
        for key, values in output.items():
            plt.plot(values, label=key)
        plt.title(f"Joint Strength for {var}")
        plt.xlabel("Study")
        plt.ylabel("Joint Strength")
        plt.legend()
        plt.grid()
        plt.savefig(f"Tests/Calibration/joint_strength_{var}.png")
        plt.close()

    
    