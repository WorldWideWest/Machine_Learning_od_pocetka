import numpy as np
import pandas as pd

np.set_printoptions(suppress = True)

## Importovanje dataseta

class SimpleLinearRegression():
    def __init__(self, dataFrame):
        self.dataFrame = pd.DataFrame(dataFrame)

    def Fit(self):
        
        independent = lambda dataFrame: np.array(dataFrame.iloc[:, 0].values)
        dependent = lambda dataFrame: np.array(dataFrame.iloc[:, 1].values)
        
        x = independent(self.dataFrame) # nezavisne varijable
        y = dependent(self.dataFrame) # zavisne varijable

        # Kalkuliranje koeficijenta linearne korelacije (r)

        xMean = np.sum(x) / len(x)
        yMean = np.sum(y) / len(y)

        xSum, ySum = 0, 0
        counter = 0

        xDen, yDen = 0, 0
        denominator = 0

        for i in range(0, len(x)):
            xSum = x[i] - xMean
            ySum = y[i] - yMean
            counter += (xSum * ySum)
            
            xDen += xSum ** 2
            yDen += ySum ** 2

            if i == len(x) - 1:
                denominator = np.sqrt(xDen * yDen)
        
        r = counter / denominator # koeficijent linearne korelacije 

        Sx, Sy = 0, 0 # Standardna devijacija x, y
        xSum, ySum = 0, 0 # Ponovno inicjaliziranje varijabli
        sxSum, sySum = 0, 0

        for i in range(0, len(x)):
            xSum = x[i] - xMean
            ySum = y[i] - yMean

            sxSum += xSum ** 2
            sySum += ySum ** 2

            if i == len(x) - 1:
                Sx = np.sqrt(sxSum / (len(x) - 1))
                Sy = np.sqrt(sySum / (len(y) - 1))


        b = r * (Sy / Sx) # nagib regresione linije

        print(b)
