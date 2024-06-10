# mike_py_test


## Bootstraping

### Clone the repo
```bash
git clone git@github.com:KingBrewer/mike_py_test
```

### Install python and venv (virtual python environment manager)

```bash
sudo apt update
sudo apt install python3 python3-venv
```


### now bootstrap python environment in the folder

```bash
cd mike_py_test

python3 -m venv helloenv
source helloenv/bin/activate

pip install -r requirements.txt

# Do your work in the virtual environment

deactivate
```

### Running the script in development mode:

Note the venv needs to be activated

```bash
python3 hello/hello.py 
```


### Installing the script and using it as a package

```bash

## install the script
## below will run setup.py and install all required dependencies,
## finally installing it in some /bin/ folder which will allow to call it
## from the command line

pip install .

### Now when it's installed, just call it

hello

```


