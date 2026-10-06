---
applyTo: **/*.any
description: AnyScript syntax, style, naming, and include conventions for AMMR source files.
---

# AnyScript Syntax Instructions
Use these rules when creating or modifying AnyScript files in this repository.

## Scope
- Applies to all files matched by the frontmatter applyTo pattern.
- If a local folder has stricter conventions, follow the local convention.
- For new files and major refactoring of existing files, follow these conventions unless there is a compelling reason to deviate.
- For minor edits to existing files, follow the existing style of the file unless there is a compelling reason to change it.


## Formatting
- Use consistent indentation within each file, by default two spaces. Prefer existing file style when editing.
- Use consistent spacing around operators and after commas, by default one space. 


### Variables and expressions
- Keep one statement per line unless a short declaration is clearly more readable on one line.

```anyscript
AnyVar a = 1; // Good

AnyVar b = 2; AnyVar c = 3; // Generally bad, two statements in one line is less readable, but acceptable for short declarations of less important variables.

AnyVar d = (a + b) * c; // Good, keep expressions on one line if they are short and readable.
AnyVar d = (a+b)*c; // ok. Operator spacing can be omitted to save space in long expressions and support readability for blocks of the expessions.
AnyVar d = (Main.a + Main.b) * (Main.b + Main.c);

AnyVector v = {1, 2; 3, 4}; // Good, keep short vector and matrix definitions on one line.

// ok, but to consider splitting longer expressions and matrices into multiple lines for readability.
AnyMatrix A = {
  {1, 2; 3, 4},
  {5, 6; 7, 8},
  v  
}; 
AnyVar d = 
  (Main.a + Main.b) 
  * (Main.b + Main.c)
  * (Main.a + Main.c)
  ;

```


### Folders and blocks
- Keep block braces visually consistent with surrounding code.

```anyscript
AnyFolder FolderObjects = {
  AnyFolder SubFolder1 = {
    AnyFolder SubSubFolder1 = {};
  };
  AnyFolder SubFolder2 = {}; // Empty folder. Keep closing brace aligned with opening brace of the block
};
```



## Naming
- Use descriptive names for objects, folders, and variables.
- Avoid repetitions in complete names (for example, avoid "DriverDriver" or "StudyStudy"). ????????

<!-- - Prefer consistent PascalCase naming for major AnyScript object names when existing files use PascalCase.
- Keep abbreviations consistent with nearby files and established domain terms.
- Do not rename public or widely referenced symbols unless required by the task. -->

## Include Conventions
<!-- - Place include directives in a stable, readable order.
- Prefer repository-consistent include path style for the current folder.
- Keep root configuration includes near the top of entry files.
- Avoid introducing duplicate includes. -->


## Code Commenting

- Use comments to explain why certain code is written in a specific way, not what the code does. ???

- Documentation-comments should be used for public objects and functions, and should follow the AnyScript documentation comment style.
  In this context a public object is one that is intended to be used by other scripts or directly by the user as interesting data or functionality.
  For example, a public object could be a folder that contains the main model, key components, or variables used by other scripts.
  Whereas clearly internal objects that are not intended to be used by other scripts or the user, do not require documentation comments.



```anyscript
/// Standard documentation comment for a public/key object.
AnyFolder KeyFolder = {
  /// Documentation comment for a public variable.
  AnyVar KeyVariable = 1;
  
  // Regular comment for an internal object or variable.
  AnyVar InternalVariable = 2;
};
```

```anyscript
  AnyVar KeyVariable = 1; ///< Documentation comment for a public variable in shorter form, line after the variable declaration (e.g. on the same line).
```


```anyscript
/// Standard documentation comment for a public/key object.
AnyFolder KeyFolder = {

  ///^ Documentation comment for the KeyFolder object, using the alternative documentation comment style with ^ symbol.
  ///^ here indicating the start of the key variables sections
  
  AnyVar KeyVariable1 = 1; ///< Key Variable no. 1.
  AnyVar KeyVariable2 = 1; ///< Key Variable no. 2.
  
  ///^ Documentation comment for the KeyFolder object for the internal variables section, using the alternative documentation comment style with ^ symbol.
  AnyVar InternalVariable = 2;   // Regular comment for an internal object or variable.

};
```


## Structure Patterns
- Keep Main model entry structure aligned with existing application patterns.
- Group related declarations into folders or sections for readability.
- Keep references and aliases close to the objects they configure.

## Safety and Compatibility
- Preserve existing behavior unless the task explicitly asks for a functional change.
- Avoid broad refactors that mix style-only edits with behavior changes.
- Minimize changes in shared definitions to reduce downstream breakage risk.

## Verification Checklist
- File parses without syntax errors in AnyBody.
- Include paths resolve correctly from the edited file.
- Naming and layout match neighboring files in the same subsystem.
- No unintended behavior changes were introduced.

## Project-Specific Decisions To Fill In
- Canonical indentation policy (tabs or spaces, and width).
- Preferred include ordering strategy.
- Explicit naming rules by object type (for example folders, drivers, studies).
- Any forbidden patterns specific to this repository.

## Notes
- This file is intentionally detailed but conservative.
- Add concrete examples later from representative files in Application, Body, and Tools.
