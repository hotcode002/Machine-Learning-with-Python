##########################################################################
# TODO - 
# 1. Describe the Apple Stock data frame
#    - Column names, shape, row count
#    - More info on data values like their min/max/mean of the columns
# 2. Change the following column names (rest of them can remain as-is)
#    - Ex-Dividend  -> ex_dividend
#    - Split Ratio  -> split_ratio
#    - Adj. Open    -> adj_open
#    - Adj. High    -> adj_high
#    - Adj. Low     -> adj_low
#    - Adj. Close   -> adj_close
#    - Adj. Volume  -> adj_volume
# 3. plot the closing price against time
# 4. What happened in 2014 ?
# 5. Read the adjusted close values time series and plot again 
# 6. Remove the data older than 1990
# 7. Filter out just the data between 2012-01-31 and 2013-02-10
# 8. Filter out all the data where the adjusted close price went above 150
##########################################################################
# LEARNING - 
# 1. What is time series data
# 2. How to read time series data using pandas 
# 3. What is resampling
# 4. How to plot time series
# 5. How to filter time series data based on date ranges and actual values
##########################################################################
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt

##########################################################################
# How to get the stock data from quandl ?
##########################################################################
# appl = quandl.get("WIKI/AAPL")         # Returns a data frame
# appl.to_csv("./data/apple_df.csv") # write the data frame out to CSV
##########################################################################

appl = pd.read_csv("./data/apple_df.csv", index_col="Date")


print ( appl.columns)
print ( appl.describe() )
print ( appl.shape )
print ( appl.shape[0])

# use the rename function specifically to rename some columns only
appl.rename(columns={   "Adj. Low"     : "adj_low",
                        "Adj. High"    : "adj_high",
                        "Adj. Open"    : "adj_open",
                        "Adj. Close"   : "adj_close",
                        "Adj. Volume"  : "adj_volume",
                        "Ex-Dividend"  : "ex_dividend"}, inplace = True)

# or create a new data frame                            
# appl = appl.rename(columns={"Adj. Low"     : "adj_low",
#                             "Adj. High"    : "adj_high",
#                             "Adj. Open"    : "adj_open",
#                             "Adj. Close"   : "adj_close",
#                             "Adj. Volume"  : "adj_volume",
#                             "Ex-Dividend"  : "ex_dividend"})

# or use the columns tuple to change the entire columns tuple 
# appl.columns = ['Open', 'High', 'Low', 'Close', 'Volume', 'ex_dividend', 'split_ratio',
#                 'adj_open', 'adj_high', 'adj_low', 'adj_close', 'adj_volume']

print ( appl.columns)
