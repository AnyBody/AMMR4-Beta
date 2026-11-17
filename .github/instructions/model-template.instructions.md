---
description: "Use when creating, editing, or reviewing AnyScript (.any) example and application models in the AMMR. Describes the standard main-file layout, the purpose of each top-level folder, and basic AnyScript conventions."
applyTo: "**/*.any"
---

# Writing AMMR example models

These guidelines apply to AnyScript application/example models (typically under `Application/` and `Tools/Templates/`). The [model-template.any](./model-template.any) file is the reference layout for new models. Do not restructure body model source code under `Body/` to follow this layout; it describes the models that *use* the body model.

## Model directory layout

A typical example model lives in its own folder:

```text
Application/Examples/<ModelName>/
├── <ModelName>.main.any        # Entry point (contains the Main folder)
├── libdef.any                  # Points to the AMMR (often just `#include "../libdef.any"`)
├── Input/Parameters.any        # Optional: user-modifiable parameters
└── Model/                      # Model parts split into included files
    ├── BodyModelConfiguration.any
    ├── Environment.any
    ├── JointsAndDrivers.any
    ├── Mannequin.any
    └── ...
```

- Name the entry point `<ModelName>.main.any` (or `.Main.any`). It is the file users load and the file tests include from `Tests/Applications/test_<ModelName>.any`.
- Keep the main file short and readable. Move larger blocks into files under `Model/` (or `Input/`) and `#include` them where they belong in the folder hierarchy.
- Use `/` as path separator in `#include` and `#path` statements for portability.

## Main file structure

Follow the structure of [model-template.any](./model-template.any). In order:

1. **Library definition** – `#include "libdef.any"` (or `"../libdef.any"`) is the first statement. Through the root `libdef.any` (which includes `Body/AAUHuman/HumanModel.defs.any`) it defines the path variables (`<ANYBODY_PATH_AMMR>`, `<ANYBODY_PATH_BODY>`, `<ANYBODY_PATH_MODELUTILS>`, …) used by all later includes.
2. **`Main`** – The root folder required by every AnyScript model. Everything else is placed inside it.
3. **Body model configuration** – `BM_*` `#define` statements (usually in `Model/BodyModelConfiguration.any`) must come *before* `HumanModel.any` is included, since they control what the body model builds.
4. **`HumanModel`** – Included with `#include "<ANYBODY_PATH_BODY>/HumanModel.any"`.
5. The remaining folders described below.

### Purpose of the top-level folders

| Folder | Why it exists |
| ------ | ------------- |
| `Parameters` | Collects every input the user is expected to change (posture, loads, applied forces, …) in one place at the top of the model, so users do not have to search the model to adapt it. Older models may not use that concept or name it `Input` or include it from `Input/Parameters.any`. Other folders should reference these values instead of hard-coding numbers. |
| `HumanModel` | Created by `HumanModel.any` from the AMMR source. It holds the body model (`HumanModel.BodyModel`), anthropometrics/scaling, and default mannequin drivers. Modify it from the application only through `BM_*` configuration and folder-reference overrides, never by editing files under `Body/`. |
| `Environment` | Holds everything outside the human: global reference frame, ground, seats, tools, machines, and other external segments. Keeping it separate makes it easy to reuse or swap the surroundings. It may be omitted if not needed, or replaced by a descriptively named folder (e.g. `Bike`). Older models place it inside `Model`. |
| `Model` | Composes the mechanical system that is analysed. It references the body model (`AnyFolder &BodyModel = .HumanModel.BodyModel;`) and the environment, and contains the connections between them: joints, drivers, contacts, supports, and ground reaction force prediction. Older models use a `ModelEnvironmentConnection` subfolder for these connections. |
| `Output` | Collects result-related objects: derived output measures, file outputs, plots, and visualisations. Keeping them separate from the mechanics makes it clear what is computed for post-processing. It may be omitted or named differently in simple models. Older models often omits this folder entirely. |
| `Studies` | Holds the `AnyBodyStudy` (or other `AnyStudy`-derived) objects that run the simulation, e.g. with `AnyFolder &Model = .Model;`, `Gravity`, `tEnd`, and `nStep`. Simple models place a single study (conventionally `Main.Study`) directly in `Main` instead. |

### Application sequence and tests

- End `Main` with the run sequence, e.g. `#include "<ANYBODY_PATH_MODELUTILS>/Operations/RunAppSequence.any"` or a local `Model/RunAppSequence.any`. This provides `Main.RunApplication`.
- Test files in `Tests/Applications/` rely on `Main.RunApplication` and on the study path (usually `Main.Study`). If you rename or move these objects, update the corresponding test file.

## AnyScript conventions

- Use descriptive CamelCase names for folders and objects.
- Reference existing objects with folder references (`AnyFolder &BodyModel = .HumanModel.BodyModel;`) instead of duplicating them.
- Use relative references (`.`, `..`) within a local structure and avoid absolute `Main.…` references whenever possible.
- Use the `BM_*` defines and the documented AMMR tools (`<ANYBODY_PATH_MODELUTILS>`, `<ANYBODY_PATH_AMMR>/Tools/…`) rather than copying their code into the application.
- Document objects with AnyScript doc comments so they appear in the model tree:
  - `///` above an object documents that object.
  - `///<` after an object on the same line documents that object.
  - `///^` at the top inside a folder documents the enclosing folder.
- Use `//` for ordinary implementation comments. Comment *why* something is done, not what the code obviously does.

## Minimal skeleton

```anyscript
#include "libdef.any"

Main = {
  #include "Model/BodyModelConfiguration.any"

  AnyFolder Parameters = {
    AnyVar tEnd = 1.0;
  };

  #include "<ANYBODY_PATH_BODY>/HumanModel.any"

  AnyFolder Environment = {
    AnyFixedRefFrame GlobalRef = {};
  };

  AnyFolder Model = {
    AnyFolder &BodyModel = .HumanModel.BodyModel;
    AnyFolder &Environment = .Environment;
    #include "Model/JointsAndDrivers.any"
  };

  AnyBodyStudy Study = {
    AnyFolder &Model = .Model;
    Gravity = {0.0, -9.81, 0.0};
    tEnd = Main.Parameters.tEnd;
    nStep = 50;
  };

  #include "<ANYBODY_PATH_MODELUTILS>/Operations/RunAppSequence.any"
}; //Main
```
