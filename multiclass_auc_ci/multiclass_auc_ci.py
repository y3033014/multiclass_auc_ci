import csv
import numpy as np
from multiclass_auc_ci.calc_ci import rounding
from multiclass_auc_ci.all_type_ci import (
    macro_normal,
    weighted_normal,
    micro_normal,
    handtill_normal,
    macro_percentile,
    weighted_percentile,
    micro_percentile,
    handtill_percentile
)


def auc_ci_select(auc_type,confidence_type,resample_num,label,score,random_seed,alpha):
    if (auc_type == "macro" and confidence_type == "normal"):
        lower,upper = macro_normal(label,score,resample_num,random_seed,alpha)

    elif (auc_type == "weighted" and confidence_type == "normal"):
        lower,upper = weighted_normal(label,score,resample_num,random_seed,alpha)

    elif (auc_type == "micro" and confidence_type == "normal"):
        lower,upper = micro_normal(label,score,resample_num,random_seed,alpha)

    elif (auc_type == "handtill" and confidence_type == "normal"):
        lower,upper = handtill_normal(label,score,resample_num,random_seed,alpha)

    elif (auc_type == "macro" and confidence_type == "percentile"):
        lower,upper = macro_percentile(label,score,resample_num,random_seed,alpha)
        
    elif (auc_type == "weighted" and confidence_type == "percentile"):
        lower,upper = weighted_percentile(label,score,resample_num,random_seed,alpha)

    elif (auc_type == "micro" and confidence_type == "percentile"):
        lower,upper = micro_percentile(label,score,resample_num,random_seed,alpha)

    elif (auc_type == "handtill" and confidence_type == "percentile"):
        lower,upper = handtill_percentile(label,score,resample_num,random_seed,alpha)

    else:
        print("Error:Please enter the correct name for auc_type or confidence_type")
        return


    return lower,upper

def multiclass_auc_ci(
    auc_type, #"macro" or "weighted" or "micro" or "handtill"
    confidence_type, #"normal" or "percentile"
    resample_num,
    example = None, #1～12
    label = None,
    score = None,
    random_seed = None,
    alpha = 0.95, #0～1
    digit = 0.0001
):
    if example is None and (score is None or label is None):
        print("Error:No score or label has been entered")
        return
    
    elif example is not None:
        n_file = 108
        n_class = 3
        example_score = np.zeros((n_file,n_class))
        example_label = np.zeros(n_file)
    
        if example < 1 or 12 < example :
            print("Error:Please enter a value from 1 to 12 for example")
            return
        elif 0 < example and example < 7:
            data_file = f'./multiclass_auc_ci/data/withAI/withAI_r{example}.csv'
            with open(data_file, encoding='utf-8') as f:
                reader_file = csv.reader(f)
                result_all = ([row for row in reader_file])
            f.close()

        elif 6 < example and example < 12:
            data_file = f'./multiclass_auc_ci/data/withoutAI/withoutAI_r{example-6}.csv'
            with open(data_file, encoding='utf-8') as f:
                reader_file = csv.reader(f)
                result_all = ([row for row in reader_file])
            f.close()

        for case_no in range(n_file):
            example_label[case_no] = float(result_all[case_no+1][0])
            for class_no in range(n_class):
                example_score[case_no][class_no] = float(result_all[case_no+1][class_no+1])

        lower,upper = auc_ci_select(auc_type,confidence_type,resample_num,example_label,example_score,random_seed,alpha)

    else:
        lower,upper = auc_ci_select(auc_type,confidence_type,resample_num,label,score,random_seed,alpha)

    return rounding(lower,digit),rounding(upper,digit)
