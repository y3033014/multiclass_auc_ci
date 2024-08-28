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

lower,upper = multiclass_auc_ci("macro","normal",100,example=1)

print(f"macro auc confidence interval = [{lower} - {upper}]")
```

### Argument list
|Argument name|Required or optional|Type|Default value|Contents|
|---|---|---|---|---|
|auc_type|Required|str|-|"macro" or "weighted" or "micro" or "handtill"|
|confidence_type|Required|str|-|"normal" or "percentile"|
|resample_num|Required|int|-|Nmber of resampling times|
|example|Optional|int|None|Whether to use the data provided,1~12|
|label|Optional|array of shape(number of data)|None|True label|
|score|Optional|array of shape((number of data),(number of class))|None|Target scores|
|random_seed|Optional|int|None|Random seed|
|alpha|Optional|float|0.95|Confidence rate of confidence interval|
|digit|Optional|float|0.0001|Number of display digits|

Either example or score and label must be entered.