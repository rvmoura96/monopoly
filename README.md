[![codecov](https://codecov.io/gh/rvmoura96/monopoly/branch/master/graph/badge.svg)](https://codecov.io/gh/rvmoura96/monopoly)
![CI](https://github.com/rvmoura96/monopoly/workflows/CI/badge.svg)

# Monopoly game

This is a simple monopoly implementation.

You should have poetry installed as a dependencies and environment manager.
[how to install](https://python-poetry.org/docs/#installation)

With poetry installed you can easily create an virtual environment and install all dependencies with the following commands:

```
poetry shell; poetry install
```

After creating the virtual environment and installing all dependencies, the following command can be used to run unittests

```
pytest
```

To execute the core for monopoly simulator you should run the following command, it will plot on the shell the results for simulations:
```
python monopoly/game.py
```

To check code coverage you can click in this badge [![codecov](https://codecov.io/gh/rvmoura96/monopoly/branch/master/graph/badge.svg)](https://codecov.io/gh/rvmoura96/monopoly) and to check CI ![CI](https://github.com/rvmoura96/monopoly/workflows/CI/badge.svg)

On linter step from CI it's executed syntax analisys and unittests.
