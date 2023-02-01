import matplotlib.pyplot as plt
import pandas as pd

#从csv文件获取数据
data = pd.read_csv('historical_data.csv')

#计算各百分位数的波动率
percentiles = [0.5, 0.7, 0.9]
vol_list = []
for percentile in percentiles:
    vol_list.append(data['Volatility'].quantile(percentile))

#定义vol_cone函数
def vol_cone(percentiles, vol_list):
    plt.plot(percentiles, vol_list, 'ro-')
    plt.xlabel('percentiles')
    plt.ylabel('Volatility')
    plt.title('Historical Volatility Cone')
    plt.grid(True)
    plt.show()   TT

#调用vol_cone函数
vol_cone(percentiles, vol_list)