import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#从csv文件获取数据
data = pd.read_csv('ag2306.csv', sep='\s+')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
#print(type(data))
#print(data.columns)
#print(data.index)
#print(data.head(1))
print(data['close'])

ret = np.log(data["close"]) - np.log(data["close"].shift(1))
df = pd.DataFrame()
df["std_22"] = ret.rolling(22).std()
df["std_44"] = ret.rolling(44).std()
df["std_66"] = ret.rolling(66).std()
#df["std_132"] = ret.rolling(132).std()
df["ret"] = ret.cumsum()
df["hv_22"] = df["std_22"] * np.sqrt(252)
df["hv_44"] = df["std_44"] * np.sqrt(252)
df["hv_66"] = df["std_66"] * np.sqrt(252)
df_cp = df.dropna()
#print(df_cp)
print(df_cp.tail(20))
df_cp.iloc[-120:,4:].plot(figsize=(20,10))  #-120，表示从最后一行开始往前数120行。4：表示从第4列开始，也就是hv_22

bin = [0,20,40,60,80,100]

print(df_cp.columns[0+4])
print(pd.cut(df_cp.iloc[:,0+4], 5, retbins=True))
cdic = {}
for i in range(3):
    cdic[df_cp.columns[i+4]] = pd.cut(df_cp.iloc[:,i+4], 5, retbins=True)[1]

print("####")
print(cdic)
vol_cone = pd.DataFrame.from_dict(cdic)
vol_cone.index = bin
vol_cone
vol_cone.T.plot(figsize=(12,6))
qdic = {}
for i in range(3):
    qdic[df_cp.columns[i + 4]] = pd.qcut(df_cp.iloc[:, i + 4], 5, retbins=True)[1]

prob_cone = pd.DataFrame.from_dict(qdic)
prob_cone.index = bin
prob_cone
prob_cone.T.plot(figsize=(12,6))



