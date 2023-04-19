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


if __name__ == '__main__':
    if (sys.argv[1]=="nsig"):
        print(fullIntervalWithNSigma(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]),
                                 float(sys.argv[6])))
    elif(sys.argv[1]=="prob"):
        print(fullIntervalWithProb(float(sys.argv[2]), float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5]),
                                 float(sys.argv[6])))
    else:
        print("error input")

