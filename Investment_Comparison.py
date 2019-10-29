import pandas as pd
import pandas_datareader as web
import datetime
import matplotlib.pyplot as plt

# write the stock ticker for the stocks you are comparing as a string
# example : ticker1 = "TSLA"
ticker1 = ""
ticker2 = ""

# write money to invest in dollar amount
# example : investment = 1000
investment =

# date formatting is (year, month, day) all as integers
# example : fromdate = datetime.datetime(2014 , 4, 1)
fromdate = datetime.datetime( , , )
todate = datetime.datetime( ,  ,)

#RUN THE CODE!

# =====================================================================================================================
# =====================================================================================================================


dfone = web.DataReader(ticker1, "yahoo", fromdate, todate)
dfone = dfone[["Close"]]
dfone["Pct Change"] = dfone["Close"]/dfone["Close"][0]
returnlabel1 = ticker1 + " Return"
dfone[returnlabel1] = dfone["Pct Change"]*investment
onereturn = dfone[[returnlabel1]]
onefinal = dfone[returnlabel1][-1]

dftwo = web.DataReader(ticker2, "yahoo", fromdate, todate)
dftwo = dftwo[["Close"]]
dftwo = dftwo.loc[fromdate:todate]
dftwo["Pct Change"] = dftwo["Close"]/dftwo["Close"][0]
returnlabel2 = ticker2 + " Return"
dftwo[returnlabel2] = dftwo["Pct Change"]*investment
tworeturn = dftwo[[returnlabel2]]
twofinal = dftwo[returnlabel2][-1]

dfcomparison = onereturn.join(tworeturn, how="inner")
dfcomparison.plot()
# plt.show()

print("Your return on", investment, "for" , ticker1 , "is:" , onefinal)
print("Your return on", investment, "for" , ticker2 , "is:" , twofinal)
