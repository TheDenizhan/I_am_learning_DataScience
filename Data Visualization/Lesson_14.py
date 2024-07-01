#BASİT ZAMAN SERİSİ GRAFİĞİ
from datetime import datetime

import pandas as pd
import pandas_datareader as pr
sym = "AAPL",
sT= datetime(2016,1,1)
eT= datetime(2019,1,1)
df = pr.get_data_yahoo(sym,start=sT,end=eT)
print("bura",df.head())
print(df.shape)
print(df["Close"].head())
print(df["Close"].plot())
df["Close"]= pd.DatetimeIndex(df["Close"].index)
