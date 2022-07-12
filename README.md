# Machine Learning Project Template

## Papermill

### Update parameters in notebook

```
papermill -f notebooks/train_iris.yml --prepare-only notebooks/train_iris.ipynb notebooks/train_iris.ipynb
```

or use script

```
./update_parameter.sh  notebooks/train_iris
```

## DJX

Run grid.

```
djx data/grid/feature_estimator/train.yml
```

## Setup

### Install main packages

```
python3.9 -m venv .venv
. .venv/bin/activate
pip install --upgrade pip
pip install wheel
pip install torch -f https://data.pyg.org/whl/torch-1.11.0+cu102.html
pip install -e ".[dev]"
pip install -e djx
```

**Note**

Pytorch needs to be installed separately to match the right cuda version.
See also: https://pytorch.org/get-started/locally/ (_Not really needed for this
template, but useful for other projects_)
