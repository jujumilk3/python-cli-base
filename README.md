# python-cli-base

## python project for building cli applications
Just fork or copy this repo to start your own python cli application.

1. https://pypi.org/project/python-cli-base/
2. PyPI Package upload guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/

## commands
### install packages
1. `python -m pip install --upgrade build`
2. `pip install twine`

### build & upload
1. `python -m build`
2. package upload
   1. test pypi: `python -m twine upload --repository testpypi dist/*`
   2. live pypi: `python -m twine upload dist/*`

### install built package & pcb commands
1. `pip install python-cli-base`
2. `pcb --help`
```dotenv
Usage: pcb [OPTIONS] COMMAND [ARGS]...

Options:
  -c, --check TEXT    check1
  -c2, --check2 TEXT  check2
  -c3, --check3 TEXT  check3
  --version           Show the version and exit.
  --help              Show this message and exit.
```
3. `pcb --version`
```dotenv
pcb 0.0.1
```
4. `pcb -c zxc -c2 asd` (Check `python_cli_base/__init__.py`)
```shell
check: zxc
check2: asd
{'check': 'zxc', 'check2': 'asd', 'check3': None}
```
