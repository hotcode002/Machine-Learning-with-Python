##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
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
# 3. Check the data types of all the columns in the data frame
# 4. Calculate the average stock price and set it as a new coulmn - average
#    - average =  (adj_high + adj_open)/2
# 5. What is the maximum adjusted volume till date ?
# 6. When did the maximum adjusted volume occur ?
# 7. Filter out just the data for 2018
# 8. Filter out all the rows where the adjusted volume is > 100 M
# 9. Filter out only the first 5 columns
#    - Open, High, Low, Close, Volume
#    - For these 5 columns, filter out all the rows with adjusted volume > 100 M
#    - On top of this, filter out rows with Open value > 100
##########################################################################
# LEARNING - 
# 1. What is a data frame
# 2. How to read data from file to a data frame using pandas 
# 3. Rows and columns in a data frame
# 4. Shape, min,max,average of values in a data frame
# 5. How to rename columns of a data frame
# 6. How to get the individual column values of a data frame
# 7. How to add a new column to a data frame
# 8. How to slice a data frame by rows, columns
#    - Row & column based slicing using iloc
# 9. How to filter out data from a data frame
#    - Filter out data from any row/column based on its value
#    - Single & multiple filters using boolean masks
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

# 1. Describe the Apple Stock data frame
#    - Column names, shape, row count
#    - More info on data values like their min/max/mean of the columns
print ( appl.columns)
print ( appl.describe() )
print ( appl.shape )
print ( appl.shape[0])

# 2. Change the following column names (rest of them can remain as-is)
#    - Ex-Dividend  -> ex_dividend
#    - Split Ratio  -> split_ratio
#    - Adj. Open    -> adj_open
#    - Adj. High    -> adj_high
#    - Adj. Low     -> adj_low
#    - Adj. Close   -> adj_close
#    - Adj. Volume  -> adj_volume
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
# print ( appl.columns)

# 3. Check the data types of all the columns in the data frame
print ( appl.dtypes)

# 4. Calculate the average stock price and set it as a new coulmn - average
#    - average =  (adj_high + adj_open)/2
appl['average'] = appl['adj_high'] + appl['adj_low']

# 5. What is the maximum adjusted volume till date ?
print ( appl['adj_volume'].max())

# 6. When did the maximum adjusted volume occur ?
print ( appl[appl['adj_volume'] == appl['adj_volume'].max()] )

# 7. Filter out just the data for 2018
print ( appl.loc['2018-01-01':'2018-12-31'])

# 8. Filter out all the rows where the adjusted volume is > 100 M
print ( appl[appl['adj_volume'] > 100000000] )

# 9. Filter out only the first 5 columns
#    - Open, High, Low, Close, Volume
# iloc - by index
print ( appl.iloc [:,0:5])

# loc  - by name
# print ( appl.loc[:,["Open","High","Low","Close","Volume"]])

#    - For these 5 columns, filter out all the rows with adjusted volume > 100 M
print ( appl.loc[ ( appl['Volume'] > 100000000 )  ,
         ["Open","High","Low","Close","Volume"]])

#    - on top of this filter out rows with 'Open value > 100
print ( appl.loc[ ( appl['Volume'] > 100000000 ) & ( appl['Open'] > 100 ) ,
         ["Open","High","Low","Close","Volume"]])
