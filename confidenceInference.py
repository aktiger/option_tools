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
    print(fullInterval(float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])))

