# CrossvalidatedData

SEE HERE FOR THE DISCUSSION: https://stats.stackexchange.com/questions/467977/friedmans-test-in-spss-gives-different-results-from-r-and-python/468930?noredirect=1#comment866529_468930

I have a repeated measurement of n=452 participants. The Friedman test of SPSS gives df=2, chi-square 36.970 whereas below is the output of R and python. I cannot explain this difference for chi-square value (30 from R and python vs 36 from SPSS) although it is not too much. Can anyone help me understand this? When I test for my other data, this happens only to two out of 6 groups of repeated measures. For the rest, the values are equal between platforms. Python and R always behave the same and the only difference is with SPSS.

#Friedman rank sum test in R        
friedman.test(data.matrix(x))
data:  data.matrix(x)
Friedman chi-squared = 30.389, df = 2, p-value = 2.518e-07

#----------------------------------------------

#Friedman Test in python
friedmanchisquare(x1, x2, x3)

FriedmanchisquareResult(statistic=30.38907395069963, pvalue=2.5182360483490374e-07)
SPSS output enter image description here

I tried looking up the implementations, but I could not figure out something myself. Here is the python implementation of Friedman: https://github.com/scipy/scipy/blob/v0.15.1/scipy/stats/stats.py#L4211
