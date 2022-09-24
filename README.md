# python-cli-base

## python project for building cli applications
Just fork or copy this repo to start your own python cli application.

1. PyPI Package upload guide: https://packaging.python.org/en/latest/tutorials/packaging-projects/

## commands
### install packages
1. `python -m pip install --upgrade build`
2. `pip install twine`

### build & upload
1. `python -m build`
2. `python -m twine upload --repository testpypi dist/*`

### install built package
3. `python3 -m pip install --index-url https://test.pypi.org/simple/ python-cli-base`
