---
description: "Use when creating, editing, or reviewing AnyScript (.any) example and application models in the AMMR. Describes the standard main-file layout, the purpose of each section and top-level folder, and basic AnyScript conventions."
applyTo: "**/*.any"
---

# Writing AMMR example models

These guidelines apply to AnyScript application/example models (typically under `Application/` and `Tools/Templates/`). The [model-template.any](./model-template.any) file is the reference layout for new models. Do not restructure body model source code under `Body/` to follow this layout; it describes the models that *use* the body model.

## Using the template

- [model-template.any](./model-template.any) shows the section order, the top-level folders, and how each part is documented. Read it before creating or restructuring a model.
- Comments starting with `// Instructions:` in the template are guidance for the agent only. Follow them, but do not copy them into models.
- Copy the documentation (`///`, `///^`) and the section banners from the template, and adapt the text to the actual model.
- Many existing models predate the template. When editing them, keep their structure unless asked to restructure; the legacy variants are noted below.

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

Before `Main`, include the library definition: `#include "libdef.any"` (or `"../libdef.any"`) is the first statement. Through the root `libdef.any` (which includes `Body/AAUHuman/HumanModel.defs.any`) it defines the path variables (`<ANYBODY_PATH_AMMR>`, `<ANYBODY_PATH_BODY>`, `<ANYBODY_PATH_MODELUTILS>`, …) used by all later includes. Class templates from AMMR tools that must be defined outside `Main` are included right after it.

Inside `Main`, follow the section order of [model-template.any](./model-template.any). The user-facing parts come first so users can adapt and run the model without reading the mechanics:

1. **Parameters** – user-modifiable inputs.
2. **Operations** – `RunApplication`, the operation the user runs.
3. **Output** – results and post-processing.
4. **Model**, split into subsections:
   1. **Body Model** – `BM_*` configuration followed by `#include "<ANYBODY_PATH_BODY>/HumanModel.any"`.
   2. **Environment** – everything outside the human.
   3. **Model Assembly** – the `Model` folder that combines body model, environment, and their connections.
   4. **Study** – the `AnyBodyStudy` that analyses `Model`.

### Section banners

Separate the sections with comment banners and a `///^` Markdown heading, as in the template:

```anyscript
  // ******************************************************
  ///^ # Parameters Section
  // ******************************************************

  // --------------------------------
  ///^ ## Environment Section
  // --------------------------------
```

- Use `*` banners with a `#` heading for top-level sections and `-` banners with a `##` heading for subsections.
- The `///^` headings become part of the `Main` folder's documentation, so they form an outline of the model in the model tree.

### Purpose of each section and folder

| Section / folder | Why it exists |
| ---------------- | ------------- |
| `Parameters` | Collects every input the user is expected to change (posture, loads, applied forces, …) in one place at the top of the model, so users do not have to search the model to adapt it. Inputs may be split into several folders by category. Older models may not use this concept, may name it `Input`, or may include it from `Input/Parameters.any`. Other folders should reference these values instead of hard-coding numbers. |
| `RunApplication` | The single operation users run to execute the model in its intended sequence. Placed near the top so it is easy to find. Either reference an operation directly (e.g. `AnyOperation &RunApplication = Study.InverseDynamics;`) or include `<ANYBODY_PATH_MODELUTILS>/Operations/RunAppSequence.any`, which defines an `AnyOperationSequence RunApplication` that also runs muscle calibration. Older models include the run sequence at the end of `Main`. |
| `Output` | Collects result-related objects: derived output measures, file outputs, plots, and visualisations. Keeping them separate from the mechanics makes it clear what is computed for post-processing. It may be omitted or named differently in simple models. Older models often omit this folder entirely. |
| `HumanModel` | Created by `HumanModel.any` from the AMMR source. It holds the body model (`HumanModel.BodyModel`), anthropometrics/scaling, and default mannequin drivers. `BM_*` `#define` statements (usually in `Model/BodyModelConfiguration.any`) must come *before* `HumanModel.any` is included, since they control what the body model builds. Modify it from the application only through `BM_*` configuration and folder-reference overrides, never by editing files under `Body/`. |
| `Environment` | Holds everything outside the human: global reference frame, ground, seats, tools, machines, and other external segments. Keeping it separate makes it easy to reuse or swap the surroundings. It may be omitted if not needed, or replaced by a descriptively named folder (e.g. `Bike`). Older models place it inside `Model`. |
| `Model` | Composes the mechanical system that is analysed. It references the body model (`AnyFolder &BodyModel = .HumanModel.BodyModel;`) and the environment (`AnyFolder &Environment = .Environment;`). Joints, drivers, contacts, supports, and ground reaction force prediction connecting them go in the `Connections` subfolder. Older models use a `ModelEnvironmentConnection` subfolder for these connections. |
| `Study` | The `AnyBodyStudy` (or other `AnyStudy`-derived object) that runs the simulation on `Model`, with `AnyFolder &Model = .Model;`, `Gravity`, `tEnd`, and `nStep`. Simple models place a single study named `Study` directly in `Main`. Models with several studies may group them in a `Studies` folder. |

### Tests

Test files in `Tests/Applications/` rely on `Main.RunApplication` and on the study path (usually `Main.Study`). If you rename or move these objects, update the corresponding test file.

## AnyScript conventions

- Use descriptive CamelCase names for folders and objects.
- Reference existing objects with folder references (`AnyFolder &BodyModel = .HumanModel.BodyModel;`) instead of duplicating them.
- Use relative references (`.`, `..`) within a local structure and avoid absolute `Main.…` references whenever possible.
- Use the `BM_*` defines and the documented AMMR tools (`<ANYBODY_PATH_MODELUTILS>`, `<ANYBODY_PATH_AMMR>/Tools/…`) rather than copying their code into the application.
- Document objects with AnyScript doc comments so they appear in the model tree:
  - `///` documents the object that follows it. Place it on the line(s) above the object.
  - `///<` documents the preceding object. Place it after the object on the same line, or on the line immediately below it.
  - `///^` documents the enclosing (parent) scope. Typically used at the top of a folder to describe the folder itself.
- Use `//` for ordinary implementation comments. Comment *why* something is done, not what the code obviously does.

## Minimal skeleton

```anyscript
#include "libdef.any"

Main = {
  ///^ Short description of what the model demonstrates.

  // ******************************************************
  ///^ # Parameters Section
  // ******************************************************

  /// User-modifiable input parameters
  AnyFolder Parameters = {
    AnyVar tEnd = 1.0; ///< Duration of the analysis in seconds
  };

  // ******************************************************
  ///^ # Operations Section
  // ******************************************************

  /// Run this operation to execute the model
  AnyOperation &RunApplication = Study.InverseDynamics;

  // ******************************************************
  ///^ # Output Section
  // ******************************************************

  /// Results and post-processing
  AnyFolder Output = {};

  // ******************************************************
  ///^ # Model Section
  // ******************************************************

  // --------------------------------
  ///^ ## Body Model Section
  // --------------------------------

  #include "Model/BodyModelConfiguration.any"
  #include "<ANYBODY_PATH_BODY>/HumanModel.any"

  // --------------------------------
  ///^ ## Environment Section
  // --------------------------------

  /// Objects surrounding the human
  AnyFolder Environment = {
    AnyFixedRefFrame GlobalRef = {};
  };

  // --------------------------------
  ///^ ## Model Assembly Section
  // --------------------------------

  /// The mechanical system analysed by the study
  AnyFolder Model = {
    AnyFolder &BodyModel = .HumanModel.BodyModel;
    AnyFolder &Environment = .Environment;
    /// Joints and drivers connecting the body model and the environment
    AnyFolder Connections = {
      #include "Model/JointsAndDrivers.any"
    };
  };

  // --------------------------------
  ///^ ## Study Section
  // --------------------------------

  /// The main study of the model
  AnyBodyStudy Study = {
    AnyFolder &Model = .Model;
    Gravity = {0.0, -9.81, 0.0};
    tEnd = ..Parameters.tEnd;
    nStep = 50;
  };
};
```