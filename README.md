⚠️  Generated with LLM help, so stay alert and code carefully ⚠️

# Phone Number Extractor

This repository shows a minimalist Python project for extracting phone
numbers from free-form text data using regex. It includes basic steps for
text preprocessing, extracting data, and evaluating the results against
ground truth values.

## Quickstart

```bash
git clone [this repo]
cd minimal_python_repo
pip install uv
uv venv
source .venv\Scripts\activate
(venv) uv sync
(venv) uv run phone_number_extractor.py
(venv) deactivate # when you are done
```

## Setup

You can install and manage dependencies and run this project using UV (a
lightweight package manager) or pip (traditional package manager).

### Overview

1. Create a virtual environment to isolate the project dependencies from your system’s Python installation

2. Activate the environment

    **Once activated, you should see `(env)` at the beginning of the terminal prompt, indicating that the virtual environment is active.**
 

3. Install dependencies

    **Make sure to install dependencies inside the environment.**

4. Run the script

 Once the dependencies are installed, run the script to extract phone numbers from text and evaluate the results.

### Option 1: Using pip

**pip** is the traditional package manager for Python.

1. Create a Virtual Environment:

   Open a terminal (or command prompt) and navigate to the directory where you have the project, then create a virtual environment named `env`

     ```bash
     python -m venv env
     ```

2. Activate it:

    **Windows**:
      ```bash
      source .\env\Scripts\activate
      ```

   **macOS/Linux**:
      ```bash
      source ./env/bin/activate
      ```

3. Install dependencies:

   Make sure you are in the venv, then install project dependencies:
    ```bash
    (env) pip install -r requirements.txt
    ```

4. Run the script with Python directly:
    ```bash
    (env) python -m phone_number_extractor.py
    ```

### Option 2: Using uv

[**UV**](https://uv.readthedocs.io/en/latest/) is a minimalist package manager for Python projects. Here's how to set it up.

0. Install **UV**:
    ```bash
    pip install uv
    ```

1. Navigate to the project directory, then create virtual environment:
    ```bash
    deactivate  # just in case already in a virtualenv from somewhere else
    uv venv
    ```

2. Activate the virtual environment:
   ```bash
   source .\venv\Scripts\activate # Windows
   source ./venv/bin/activate # Mac/Linux
   ```

3. Install project dependencies. Note: these are defined in `pyproject.toml`.
    ```bash
    (venv) uv sync
    ```

4. Run
    ```bash
    (venv) uv run phone_number_extractor.py
    ```

## License

TBD

## Notes 

- **Type Hints**: Use type hints for clarity and better IDE support. Type hints also allow use of static checkers like `mypy` to catch errors before code is run.

- **Use `Path` from `pathlib`**: Always prefer using `Path` for working with file paths instead of raw strings for better cross-platform compatibility. For instance, Windows uses back slashes while OS/Linux using slashes for paths.

- **Modular Code**: The script is broken down into small, single-purpose functions for readability and maintainability. Keep functions focused on one task and avoid large, monolithic blocks of code.

- **Docstrings**: Each function has a clear docstring explaining its purpose. This is important for maintaining code and helping others understand the purpose of each function.

- **Use `pyproject.toml`**: This file is used to manage project metadata, dependencies, and entry points for command-line interface scripts. It helps standardize configurations for packaging and dependency management.

- **Use virtual environments**: Use a separate virtual environment for each project. This ensure that the packages used in one project don’t conflict with other projects.

- **Confirm you are in right virtual environment**: Check where your python executable is located.  The output should be in the same folder, e.g. something similar to `[...]/minimal_python_repo/.venv/Scripts/python`.

  ```bash
  gcm python # On Windows. Note, gcm stands for Get-Command
  which python # On MacOS / LinuX
  ```
