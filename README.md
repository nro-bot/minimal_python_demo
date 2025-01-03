⚠️  Generated with LLM help, so stay alert and code carefully ⚠️

# Phone Number Extractor

This repository shows a minimalist Python project for extracting phone
numbers from free-form text data using regex. It includes basic steps for
text preprocessing, extracting data, and evaluating the results against
ground truth values.

## Setup

You can install and manage dependencies and run this project using UV (a
lightweight package manager) or pip (traditional package manager). Below
are the instructions for both methods.

The first step is to create a virtual environment to isolate the project
dependencies from your system’s Python installation. This ensures that the
packages used in the project don’t conflict with other projects. i

**Once activated, you should see `(env)` at the beginning of the terminal prompt, indicating that the virtual environment is active.**

After creating it, make sure installation steps are all inside that
environment.


### Option 1: Using pip 

**pip** is the traditional package manager for Python. Follow these steps:

1. Create a Virtual Environment

Open a terminal (or command prompt) and navigate to the directory where you have the project.

Run the following command to create a virtual environment:
     ```bash
     python -m venv env
     ```

This will create a virtual environment named `env`.

2. Activate the Virtual Environment

Once the virtual environment is created, activate it:

- **Windows** (Command Prompt):
  ```bash
  .\env\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source ./env/bin/activate
  ```
3. Install dependencies 

Make sure you are in the venv, then install project dependencies:
```bash
(env) pip install -r requirements.txt
```

### Option 2: Using uv

[**UV**](https://uv.readthedocs.io/en/latest/) is a minimalist package manager for Python projects. Here's how to set it up.

1. Install **UV**:
    ```bash
    pip install uv
    ```

2. Navigate to the project directory, then create virtual environment
    ```bash
    deactivate  # just in case already in a virtual environment
    uv venv
    ```

2. Activate the virtual environment. 
- **Windows** (Command Prompt):
  ```bash
  .\.venv\Scripts\activate
  ```
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

3. Install project dependencies defined in `pyproject.toml`:
    ```bash
    (env) uv install
    ```

## Running the Script

Once the dependencies are installed, run the script to extract phone numbers from text and evaluate the results.

### With UV:

```bash
(env) uv run phone_number_extractor.py
```

### With Python:

Alternatively, run the script with Python directly:

```bash
(env) python -m phone_number_extractor.py
```

## License

TBD

## Design Decision Notes

- **Type Hints**: Use type hints for clarity and better IDE support. Type hints also allow use of static checkers like `mypy` to catch errors before code is run.

- **Use `Path` from `pathlib`**: Always prefer using `Path` for working with file paths instead of raw strings for better cross-platform compatibility. For instance, Windows uses back slashes while OS/Linux using slashes for paths.

- **Modular Code**: The script is broken down into small, single-purpose functions for readability and maintainability. Keep functions focused on one task and avoid large, monolithic blocks of code.

- **Docstrings**: Each function has a clear docstring explaining its purpose. This is important for maintaining code and helping others understand the purpose of each function. 

- **Use `pyproject.toml`**: This file is used to manage project metadata, dependencies, and entry points for command-line interface scripts. It helps standardize configurations for packaging and dependency management.
