import numpy as np
import pandas as pd


## Importovanje dataseta

class SimpleLinearRegression():
    def __init__(self, dataFrame):
        self.dataFrame = pd.DataFrame(dataFrame)

    def Fit(self):
        
        independent = lambda dataFrame: np.array(dataFrame.iloc[:, 0].values)
        dependent = lambda dataFrame: np.array(dataFrame.iloc[:, 1].values)
        

        

        x = independent(self.dataFrame) # nezavisne varijable
        y = dependent(self.dataFrame) # zavisne varijable

        ## Kalkuliranje koeficijenta linearne korelacije (r)

        xMean = np.sum(x) / len(x)
        yMean = np.sum(y) / len(y)

        xSum, ySum = 0, 0

        for xi in x:
            xSum += (xi - xMean)

        for yi in y:
            ySum += (yi - yMean)

        counter = xSum * ySum
        denominator = (xSum ** 2) * (ySum ** 2)
        
        print(counter)
        print(denominator)

        #r = counter / denominator
        #return float(r)


        #print(xMean)
        #print(yMean)
       
       
        

