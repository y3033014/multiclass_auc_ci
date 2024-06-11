# multiclass_auc_ci

## Description
`multiclass_auc_ci` is a Python library for calculating multiclass auc confidence interval.

## Dependencies
- Python >= 3.11
- openpyxl >= 3.1.2
- numpy >= 1.26.2
- scipy >= 1.13.0
- scikit-learn >= 1.4.2

## Installation
```bash
pip install multiclass_auc_ci
```

## Usage
### Examples of Use
```python
from multiclass_auc_ci import multiclass_auc_ci

lower,upper = multiclass_auc_ci("macro","normal",0.95,100,example=1)

print(f"macro auc confidence interval = [{lower} - {upper}]")
```

### Argument list
|Argument name|Required or optional|Type|Default value|Contents|
|---|---|---|---|---|
