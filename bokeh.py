import pandas as pd
pd.options.plotting.backend = "plotly"

df = pd.DataFrame(dict(a=[21323223321,3,2], b=[3,2,1]))
fig = df.plot()
fig.show()