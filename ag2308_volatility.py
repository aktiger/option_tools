import pandas as pd
import numpy as np

pd.options.plotting.backend = "plotly"
#从csv文件获取数据
data = pd.read_csv('ag2308.csv', sep='\s+')
pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
#print(type(data))
#print(data.columns)
#print(data.index)
#print(data.head(1))
print(data['close'])

ret = np.log(data["close"]) - np.log(data["close"].shift(1))
df = pd.DataFrame()
df["date"] = data['date']
df["std_20"] = ret.rolling(20).std()
df["std_44"] = ret.rolling(40).std()
df["std_65"] = ret.rolling(65).std()
#df["std_132"] = ret.rolling(132).std()
df["ret"] = ret.cumsum()
df["hv_22"] = df["std_20"] * np.sqrt(252)
df["hv_44"] = df["std_44"] * np.sqrt(252)
df["hv_65"] = df["std_65"] * np.sqrt(252)
df_cp = df.dropna()
#print(df_cp)
print(df_cp.tail(20))
fig11 = df_cp.iloc[-252:,5:].set_index(df_cp["date"]).plot()  #-120，表示从最后一行开始往前数120行。4：表示从第4列开始，也就是hv_22

fig11.show()
bin = [0,20,40,60,80,100]

print(df_cp.columns[0+5])
print(pd.cut(df_cp.iloc[:,0+5], 5, retbins=True))
cdic = {}
for i in range(3):
    cdic[df_cp.columns[i+5]] = pd.cut(df_cp.iloc[:,i+5], 5, retbins=True)[1]

print("####")
print(cdic)
vol_cone = pd.DataFrame.from_dict(cdic)
vol_cone.index = bin
vol_cone
fig22 = vol_cone.T.plot()
fig22.show()

qdic = {}
for i in range(3):
    qdic[df_cp.columns[i + 5]] = pd.qcut(df_cp.iloc[:, i + 5], 5, retbins=True)[1]

prob_cone = pd.DataFrame.from_dict(qdic)
prob_cone.index = bin
prob_cone
fig33 = prob_cone.T.plot()
fig33.show()



