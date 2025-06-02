from pathlib import Path
from itertools import product, groupby
from collections import ChainMap
from anypytools import AnyPyProcess, macro_commands as mc
from anypytools.abcutils import AnyPyProcessOutputList
from anypytools.tools import winepath, ON_WINDOWS

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
        {'BM_LEG_MODEL':'_LEG_MODEL_TLEM_'}

    ],
    [
        {'BM_CALIBRATION_TYPE':'_EXPERIMENTAL_CALIBRATION_TYPE_2PAR_'}
    ],
    [
        {'BM_LEG_MUSCLES_BOTH': '_MUSCLES_3E_HILL_'},
        {'BM_LEG_MUSCLES_BOTH': '_MUSCLES_SIMPLE_'}
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
        for var in AMS_VARIABLES:
            formatted.setdefault(var.split(".")[-1], []).append(result[var])
    
    return formatted    


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
                # mc.OperationRun(OPERATION),
                # *make_dump_commands(AMS_VARIABLES),
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


def test_joint_strength(model_output: AnyPyProcessOutputList):
    """ test the trunk region mass"""
    output = model_output["JointStrength"]
    
    rounded_vals = [round(val, ABS_TOL) for val in output]
