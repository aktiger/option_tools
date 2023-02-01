import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

#定义常数
r = 0.03 # 无风险收益率
S0 = 100 # 股票价格
K = 90 # 行权价
T = 1 # 时间

#设定波动率的范围，以及步长
sigma_min, sigma_max, h = 0.01, 0.30, 0.01

#生成波动率的序列
sigma_list = np.arange(sigma_min, sigma_max + h, h)

#建立空的列表，用于存放隐含波动率
implied_volatilities = []

#计算隐含波动率
for sigma in sigma_list:
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    implied_volatility = sigma * np.sqrt(2 * np.pi / T) * np.exp(-d1 ** 2 / 2) / (S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2))
    implied_volatilities.append(implied_volatility)

#绘制波动率锥
plt.title('Implied Volatility Cone')
plt.plot(sigma_list, implied_volatilities, 'b-')
plt.xlabel('sigma')
plt.ylabel('implied volatility')
plt.xlim(0, 0.3)
plt.ylim(0, 0.3)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()