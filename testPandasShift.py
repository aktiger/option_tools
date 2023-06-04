import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")
pd.options.plotting.backend = "plotly"
#从csv文件获取数据
data = pd.read_csv('testPandasShit.csv', sep='\s+')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)

print("原始数据:\n{0}".format(data['close']))
print("shift(1)后数据\n{0}".format(data['close'].shift(1)))
ret = np.log(data["close"]) - np.log(data["close"].shift(1))
print("收益率对数:\n{0}\n".format(ret))