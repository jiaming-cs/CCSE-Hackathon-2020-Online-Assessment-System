# Hackathon-2020

This repository is built for KSU CCSE 2020 Hackathon Magmutal Challenge.

## Usage

### Setup Virtual Evironment
Conda:
```
conda create -n venv python=3.7
conda activate venv
pip install -r requirements.txt
```
OR

Virtualenv:

On Windows:

```
virtualenv venv --python=3.7
cd venv/Scripts 
activate
cd ../..
pip install -r requirements.txt
```

On Linux:

```
virtualenv venv --python=3.7
source venv/bin/activate
pip install -r requirements.txt
```

Run the server:
```
python app.py
```
