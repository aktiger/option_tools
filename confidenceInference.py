import numpy as np
import sys

def calPriceIntervalPositive(initPrice, N_sigma, volatility, leftTime, yearDay):
    return initPrice * np.exp(N_sigma * volatility * np.sqrt(leftTime / yearDay))


def calPriceIntervalNegative(initPrice, N_sigma, volatility, leftTime, yearDay):
    return initPrice * np.exp(-N_sigma * volatility * np.sqrt(leftTime / yearDay))


def fullInterval(initPrice, N_sigma, volatility, leftTime, yearDay):
    return "[" + str(calPriceIntervalNegative(initPrice, N_sigma, volatility, leftTime, yearDay)) + "," + \
           str((calPriceIntervalPositive(initPrice, N_sigma, volatility, leftTime, yearDay))) + "]"


if __name__ == '__main__':
    print(fullInterval(5600, 1.95, 0.13, 30, 252))
