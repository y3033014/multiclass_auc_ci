import numpy as np
from sklearn.utils import resample
from sklearn.metrics import roc_auc_score
from .calc_ci import (ci_normal,ci_percentile)

def macro_normal(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovr",average="macro"))
    lower,upper = ci_normal(resample_auc_list,alpha)
    return lower,upper

def weighted_normal(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovr",average="weighted"))
    lower,upper = ci_normal(resample_auc_list,alpha)
    return lower,upper

def micro_normal(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovr",average="micro"))
    lower,upper = ci_normal(resample_auc_list,alpha)
    return lower,upper

def handtill_normal(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovo",average="macro"))
    lower,upper = ci_normal(resample_auc_list,alpha)
    return lower,upper

def macro_percentile(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovr",average="macro"))
    lower,upper = ci_percentile(resample_auc_list,alpha)
    return lower,upper

def weighted_percentile(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovr",average="weighted"))
    lower,upper = ci_percentile(resample_auc_list,alpha)
    return lower,upper

def micro_percentile(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovr",average="micro"))
    lower,upper = ci_percentile(resample_auc_list,alpha)
    return lower,upper

def handtill_percentile(label,score,resample_num,random_seed,alpha):
    resample_auc_list = np.array([])
    for resample_no in range(resample_num):
        resample_label,resample_score = resample(label,score,random_state=random_seed)
        resample_auc_list = np.insert(resample_auc_list,np.size(resample_auc_list),roc_auc_score(resample_label,resample_score,multi_class="ovo",average="macro"))
    lower,upper = ci_percentile(resample_auc_list,alpha)
    return lower,upper