from decimal import Decimal, ROUND_HALF_UP
from scipy.stats import norm
import numpy as np

def rounding(value,digit): #四捨五入
    rounding_value = Decimal(str(value)).quantize(Decimal(f'{digit}'),rounding=ROUND_HALF_UP)
    return rounding_value

def ci_normal(data,alpha): #ブートストラップ法によりリサンプリングしたデータから得たAUCの分布を正規分布と仮定
    random_variable = norm.ppf(1-((1-alpha)/2))
    mean = np.mean(data)
    std = np.std(data)
    lower = mean - random_variable * std
    upper = mean + random_variable * std
    return lower,upper

def ci_percentile(data,alpha): #ブートストラップ法によりリサンプリングしたデータから得たAUCの分布がノンパラメトリック、パーセンタイル法
    lower_quantile = (1 - alpha)/2 * 100
    upper_quantile = (1 - ((1 - alpha)/2)) * 100
    lower,upper =  np.percentile(data,[lower_quantile,upper_quantile])
    return lower,upper

