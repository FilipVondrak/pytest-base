# Requirements
- tested on `Python 3.13`
- need to specify the path to the binary in `conftest.py`

# Install
1. create `venv` using
```sh 
python -m venv .venv
```

2. activate the venv using 
```sh 
source .venv/bin/activate
```
3. install dependencies using 
```sh 
pip install -r requirements.txt
```

# Run
- to run all tests in parallel, run the following command in the base directory:
```sh
pytest -v -n auto
```
- to also generete html report, also add the `--html=report.html` flag
```sh
pytest -v -n auto --html=report.html
```