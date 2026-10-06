---
applyTo: ./Tools/**/*
description: Instructions for AMMR tools
---

# AMMR Tools Development Instructions


## Modules

Modules are the building blocks of the AMMR tools. Each module should have a clear responsibility and should be designed to be reusable across different parts of the project. 
When creating a new module, follow these guidelines:

- Name the module clearly to reflect its purpose.
- Keep the module focused on a single, well-defined, and cohesive responsibility.
- Document the module's public interface and usage examples.
- Write tests for the module to ensure its correctness.

Types of modules:
- **Library Modules**: Modules that provide reusable functionality across different an application area, such MoCap interfacing, human-environment contact, etc.
  - A folder in `Tools`
  - A `libdef.any` file that can be included, when using the module from an application.

- **Feature Modules**: Modules that implement specific features or functionalities within the application. Typically, they reside in a Library Module folder.
  - A deficated file
  - Formats:
    - Single include file: A single file containing the feature module's implementation.
    - Class-template: A feature module implemented as one or more class templates, allowing for flexible and reusable class definitions. Typically, one main class-template is the modules interface, but with assisting class-templates providing additional functionality as part of the interface to the main one.


## Module Include Files

## Module Class-Templates

When creating a new class-template, follow these guidelines:

- Name the class and the file clearly to reflect its purpose.
- Keep the class focused on a single responsibility.
- Document the class's public interface and usage examples.
- Write tests for the class to ensure its correctness.



## Examples



## Testing

In principle, every module and class should have corresponding tests to ensure their correctness and reliability. 
Follow these guidelines when writing tests:

- Write tests for all public methods and functions.
- Cover both typical and edge cases.
- Keep tests independent and isolated.
- Use descriptive names for test cases to clearly indicate their purpose.

Types of tests:

- **Unit Tests**: Test individual modules or classes in isolation to ensure they work as expected.
- **Example Tests**: Test specific examples or scenarios to ensure the system behaves as expected in those cases.

- **Regression Tests**: Test existing functionality to ensure that new changes do not break the existing behavior.
