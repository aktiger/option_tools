import numpy as np
import sys
from scipy.stats import norm

def calPriceIntervalPositive(initPrice, N_sigma, volatility, leftTime, yearDay):
    return initPrice * np.exp(N_sigma * volatility * np.sqrt(leftTime / yearDay))


def calPriceIntervalNegative(initPrice, N_sigma, volatility, leftTime, yearDay):
    return initPrice * np.exp(-N_sigma * volatility * np.sqrt(leftTime / yearDay))


def fullIntervalWithNSigma(initPrice, N_sigma, volatility, leftTime, yearDay):
    return "[" + str(calPriceIntervalNegative(initPrice, N_sigma, volatility, leftTime, yearDay)) + "," + \
           str((calPriceIntervalPositive(initPrice, N_sigma, volatility, leftTime, yearDay))) + "]"


def fullIntervalWithProb(initPrice, prob, volatility, leftTime, yearDay):
    N_sigma = norm.ppf(1- (1-prob)/2)
    return "[" + str(calPriceIntervalNegative(initPrice, N_sigma, volatility, leftTime, yearDay)) + "," + \
           str((calPriceIntervalPositive(initPrice, N_sigma, volatility, leftTime, yearDay))) + "]"

# python confidenceInference.py Prob 5600 0.86638 0.21 30 252 22

'''
 ~/cvs/option_tools  master  python confidenceInference.py prob 5600 0.9973002039367398 0.21 30 252                           ✔  base   18:22:36
[4505.937387484188,6959.706117334515]

 ~/cvs/option_tools  master  python confidenceInference.py nsig 5600 3 0.21 30 252                                            ✔  base   18:23:29
[4505.937387484187,6959.7061173345155]
'''

if __name__ == '__main__':
    if (sys.argv[1]=="nsig"):
        print(fullIntervalWithNSigma(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]),
                                 float(sys.argv[6])))
    elif(sys.argv[1]=="prob"):
        print(fullIntervalWithProb(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]),
                                 float(sys.argv[6])))
    else:
        print("error input " + sys.argv[1])

