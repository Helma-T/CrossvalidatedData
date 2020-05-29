anonymized <- read.csv("~/Documents/PhD/a_InteractiveMoodTracker/Data/PreStudy/anonymized.csv")
library(dplyr)
x=select(anonymized, "A_1", "A_2", "A_3")
friedman.test(data.matrix(x))