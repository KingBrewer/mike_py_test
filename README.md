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
