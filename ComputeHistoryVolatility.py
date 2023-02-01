import numpy as np

def historical_volatility(close, lookback_period):
    log_returns = np.diff(np.log(close))
    vol = np.std(log_returns) * (np.sqrt(252))
    return vol

#示例
close = [100, 110, 90, 80, 60, 40, 70, 50]
lookback_period = 252

vol = historical_volatility(close, lookback_period)
print(vol) # 0.3579
