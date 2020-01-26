# Pyramid Scaffold


## Getting Started


Change directory into your newly created project.
```bash
$ cd calculator
```
Create a Python virtual environment.
```bash
$ python3 -m venv env
```
Upgrade packaging tools.
```bash
$ env/bin/pip install --upgrade pip setuptools
```
Install the project in editable mode with its testing requirements.
```bash
$ env/bin/pip install -e ".[testing]"
```
Run your project's tests.
```bash
$ env/bin/pytest
```
Run your project.
```bash
$ env/bin/pserve development.ini
```

## Run using Docker
```bash
$ docker build calculator .
$ docker run -p 6543:6543 calculator
```