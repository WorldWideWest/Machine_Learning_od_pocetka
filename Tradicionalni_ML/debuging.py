import pandas as pd 
import numpy as np

from linearnaRegresija import SimpleLinearRegression

data = pd.read_excel("dataSet/cars-simple-reg.xlsx")

parsing = SimpleLinearRegression(data)
parsing.Fit()
