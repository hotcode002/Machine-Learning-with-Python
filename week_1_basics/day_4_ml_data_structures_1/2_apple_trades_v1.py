##########################################################################
# TODO - 
# 1. What is the monthly average "Close" price of Apple stock
# 2. What is the yearly average "Close" price of Apple stock
# 3. plot the closing price against time
# 4. What happened in 2014 ?
# 5. Read the adjusted close values time series and plot again 
# 6. Remove the data older than 1990
# 7. Filter out just the data between 2012-01-31 and 2013-02-10
# 8. Filter out all the data where the adjusted close price went above 150
##########################################################################
from pandas import Series
from pandas import read_csv
import matplotlib.pyplot as plt

appl_close_ts = read_csv("./data/apple_close_ts.csv", parse_dates=[0],
                             index_col      =   0,
                             squeeze        =   True)

# resample the Time Series data to summarize mean by month
appl_close_ts_m = appl_close_ts.resample('M').mean()

# resample the Time Series data to summarize mean by year
appl_close_ts_y = appl_close_ts.resample('Y').mean()

plt.plot( appl_close_ts )
plt.show()

# Read the adjusted close price
appl_adj_close_ts = read_csv("./data/apple_adj_close_ts.csv", parse_dates=[0],
                             index_col      =   0,
                             squeeze        =   True)

plt.plot( appl_adj_close_ts )
plt.show() 

# Remove the data older than 1990
appl_adj_close_ts_1990 = appl_adj_close_ts[appl_adj_close_ts.index.year > 1990]

# 7. Filter out just the data between 2012-01-31 and 2013-02-10
#    -- In the case of a time series, this is essentially filtering a DF by index
#    -- hence, we used loc
appl_adj_close_ts_2012= appl_adj_close_ts.loc['2010-01-31':'2013-02-10']

# 8. Filter out all the data where the adjusted close price went above 150
appl_adj_close_ts_150 = appl_adj_close_ts[appl_adj_close_ts > 150]
print ( appl_adj_close_ts_150)