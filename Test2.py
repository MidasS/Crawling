import pandas.io.data as web
import datetime
import pandas as pd
import matplotlib.pyplot as plt

start=datetime.datetime(2014,1,1)
end=datetime.datetime(2015,2,15)

soil=web.DataReader("010950.KS","yahoo",start,end)
print (soil)
plt.plot(soil.index, soil['Close'])
plt.show()
# soil['MA5']=pd.stats.moments.rolling_mean(soil['AdjClose'],5)
# soil['MA20']=pd.stats.moments.rolling_mean(soil['AdjClose'],20)
# soil['MA60']=pd.stats.moments.rolling_mean(soil['AdjClose'],60)
# soil['MA120']=pd.stats.moments.rolling_mean(soil['AdjClose'],120)
# #
# print(soil.tail().sort_index(0,ascending=False))
