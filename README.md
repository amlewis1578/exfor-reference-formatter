# `exforrefs`

a Python package to find and format the reference information for EXFOR entries, from a DOI.

## installation

### Editable version for development

For developing the package, install in editable mode:

```bash
pip install -e .
```

and run 

```bash
pre-commit install
```

to get the pre-commit hooks working (there is a pre-commit hook to run `black`, which formats the python files, when you commit something).

### Static version for use

move into the directory and run

```bash
pip install .
```

to install a static version of the package.


## Running tests

To run the unit tests, run `pytest` from the base of the repo (the directory that has the `tests` and  `src` sub-directories.) If the tests fail because of import errors, make sure that you have the package installed.

The command `pytest` will run any files that match the pattern: `tests/*test.py`. This is defined at the end of the [`pyproject.toml`](pyproject.toml) file, along with some test markers that can be used later in more advanced testing.


## using the `exforrefs` package



