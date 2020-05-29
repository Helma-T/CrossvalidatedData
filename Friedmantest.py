import matplotlib.pyplot as plt
import pandas
import numpy as np
import pandas
import scipy as sp
import numpy as np
from scipy import stats
from scipy.stats import boxcox
from scipy.stats import mannwhitneyu
from scipy.stats import ks_2samp
from scipy.stats import wilcoxon
from scipy.stats import friedmanchisquare

import warnings
import numpy as np
import pandas as pd
import scipy.stats as st
import statsmodels as sm
import matplotlib
import matplotlib.pyplot as plt



# Friedman Test

# Assumptions: 
#     Observations in each sample are independent and identically distributed (iid).
#     Observations in each sample can be ranked.
#     Observations across each sample are paired.
# Interpretation: 
#     H0: the distributions of all samples are equal.
#     H1: the distributions of one or more samples are not equal.

def my_friedman_test(q1, q2, q3, expt_ratings): 

    stat, p = friedmanchisquare(q1, q2, q3)
    print('stat=%.3f, p=%.3f' % (stat, p))
    if p > 0.05:
        print('Friedman Test: Probably the same distribution, the distributions of all samples are equal.')
    else:
        print('Friedman Test:Probably different distributions, the distributions of one or more samples are not equal.')

# Kendall’s W  
    if expt_ratings.ndim!=2:
        raise 'ratings matrix must be 2-dimensional'
    m = expt_ratings.shape[1] #raters
    k = expt_ratings.shape[0] # items rated

    print(stat/(k*(m-1)))

    rating_sums = np.sum(expt_ratings, axis=1)
    S = k*np.var(rating_sums)

    W= (12*S)/((m**2)*(k**3-k))

    # print ("raters: ",m," items rated: ", k, "and W= ",'%.8f' % W)

    stat, p = wilcoxon(q1, q2)
    print(q1.name+" and "+q2.name+'stat=  %.3f,  p= %.3f' % (stat, p), "z=", stats.norm.isf(p / 2))
    stat, p = wilcoxon(q1, q3)
    print(q1.name+" and "+q3.name+'stat=  %.3f,  p= %.3f' % (stat, p))
    stat, p = wilcoxon(q3, q2)
    print(q3.name+" and "+q2.name+'stat=  %.3f,  p= %.3f' % (stat, p))
    

    print('if p > 0.01: Wilcoxon Signed: Probably the same distribution. Else, Probably different distributions ')
    print("Bonferroni Correction: .05 or .01 alpha devided by 3 for the significant level")
    print("---------------------------------------------")
    return


anonymized=pd.read_csv("anonymized.csv")
my_friedman_test(anonymized["A_1"],anonymized["A_2"],anonymized["A_3"], anonymized[["A_1", "A_2","A_3"]])
