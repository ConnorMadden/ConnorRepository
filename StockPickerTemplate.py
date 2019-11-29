# BROGAR STOCK PICKING PROJECT

# Pick your dates (Make them strings)
# Example: startDate = "2019-8-28"
startDate = ""
endDate = ""

# Put your ticker symbol as a string
# Example: ticker1 = "TSLA"
# Put the amount of money you plan to invest
# Example: investment1 = 25000
ticket1 = ""
investment1 =
ticket2 = ""
investment2 =
ticket3 = ""
investment3 =
ticket4 = ""
investment4 =

# Put the weekly business day you want your return as a string
# Only valid codes are MON, TUE, WED, THU, FRI (Markets closed weekends)
# Example: DayOfTheWeek = "WED"
DayOfTheWeek = ''

# RUN THE FILE!!!
# An Excel Will be created showing values and returns.
# Means and STDs will be printed below.

# ===================================================================================================
# ===================================================================================================
# ===================================================================================================


import pandas as pd
import pandas_datareader as web

index = pd.date_range(startDate,endDate, freq="W-" + DayOfTheWeek)
df1 = web.DataReader(ticket1,"yahoo",startDate,endDate)
shares1 = investment1/df1["Close"][0]
shares1 = int(shares1)
df1 = df1[["Close"]]
df1 = df1.reindex(index)
df1["Value of " + ticket1] = df1["Close"]*shares1
df1 = df1[["Value of " + ticket1]]


df2 = web.DataReader(ticket2,"yahoo",startDate,endDate)
shares2 = investment2/df2["Close"][0]
shares2 = int(shares2)
df2 = df2[["Close"]]
df2["Value of " + ticket2] = df2["Close"]*shares2
df2 = df2[["Value of " + ticket2]]

df3 = web.DataReader(ticket3,"yahoo",startDate,endDate)
shares3 = investment3/df3["Close"][0]
shares3 = int(shares3)
df3 = df3[["Close"]]
df3["Value of " + ticket3] = df3["Close"]*shares3
df3 = df3[["Value of " + ticket3]]


df4 = web.DataReader(ticket4,"yahoo",startDate,endDate)
shares4 = investment4/df4["Close"][0]
shares4 = int(shares4)
df4 = df4[["Close"]]
df4["Value of " + ticket4] = df4["Close"]*shares4
df4 = df4[["Value of " + ticket4]]


dfFinal = df1.join(df2,how = "inner")
dfFinal = dfFinal.join(df3, how = "inner")
dfFinal = dfFinal.join(df4, how = "inner")
dfFinal["Portfolio Value"] = dfFinal["Value of " + ticket1] + dfFinal["Value of " + ticket2] + dfFinal["Value of " + ticket3] + dfFinal["Value of " + ticket4]


dfFinal["Portfolio Value 2"] = dfFinal["Portfolio Value"].shift(1)
dfFinal["Portfolio Return"] = (dfFinal["Portfolio Value"]-dfFinal["Portfolio Value 2"])/dfFinal["Portfolio Value 2"]

dfVFINX = web.DataReader("VFINX","yahoo",startDate,endDate)
sharesVFINX = 100000/dfVFINX["Close"][0]
sharesVFINX = int(sharesVFINX)
dfVFINX = dfVFINX[["Close"]]
dfVFINX = dfVFINX.reindex(index)
dfVFINX["VFINX Value"] = dfVFINX["Close"]*sharesVFINX
dfVFINX = dfVFINX[["VFINX Value"]]
dfFinal = dfFinal.join(dfVFINX,how="inner")
dfFinal["VFINX Value 2"] = dfFinal["VFINX Value"].shift(1)
dfFinal["VFINX Return"] = (dfFinal["VFINX Value"]-dfFinal["VFINX Value 2"])/dfFinal["VFINX Value 2"]

dfQQQ = web.DataReader("QQQ","yahoo",startDate,endDate)
sharesQQQ = 100000/dfQQQ["Close"][0]
sharesQQQ = int(sharesQQQ)
dfQQQ = dfQQQ[["Close"]]
dfQQQ = dfQQQ.reindex(index)
dfQQQ["QQQ Value"] = dfQQQ["Close"]*sharesQQQ
dfQQQ = dfQQQ[["QQQ Value"]]
dfFinal = dfFinal.join(dfQQQ,how="inner")
dfFinal["QQQ Value 2"] = dfFinal["QQQ Value"].shift(1)
dfFinal["QQQ Return"] = (dfFinal["QQQ Value"]-dfFinal["QQQ Value 2"])/dfFinal["QQQ Value 2"]

dfVHGEX = web.DataReader("VHGEX","yahoo",startDate,endDate)
sharesVHGEX = 100000/dfVHGEX["Close"][0]
sharesVHGEX = int(sharesVHGEX)
dfVHGEX = dfVHGEX[["Close"]]
dfVHGEX = dfVHGEX.reindex(index)
dfVHGEX["VHGEX Value"] = dfVHGEX["Close"]*sharesVHGEX
dfVHGEX = dfVHGEX[["VHGEX Value"]]
dfFinal = dfFinal.join(dfVHGEX,how="inner")
dfFinal["VHGEX Value 2"] = dfFinal["VHGEX Value"].shift(1)
dfFinal["VHGEX Return"] = (dfFinal["VHGEX Value"]-dfFinal["VHGEX Value 2"])/dfFinal["VHGEX Value 2"]

dfFinal.drop(["Portfolio Value 2","VFINX Value 2","QQQ Value 2","VHGEX Value 2"],axis=1, inplace=True)

portfolioMean = dfFinal["Portfolio Return"].mean()
portfolioStd = dfFinal["Portfolio Return"].std()
vfinxMean = dfFinal["VFINX Return"].mean()
vfinxStd = dfFinal["VFINX Return"].std()
QQQMean = dfFinal["QQQ Return"].mean()
QQQStd = dfFinal["QQQ Return"].std()
VHGEXMean = dfFinal["VHGEX Return"].mean()
VHGEXStd = dfFinal["VHGEX Return"].std()

print("Portfolio Mean: " + str(portfolioMean) +" Portfolio Std: " + str(portfolioStd))
print("VFINX Mean: "+ str(vfinxMean) +" VFINX Std: "+ str(vfinxStd))
print("QQQ Mean: "+ str(QQQMean) + " QQQ Std: "+ str(QQQStd))
print("VHGEX Mean: "+ str(VHGEXMean) + " VHGEX Std: "+ str(VHGEXStd))
print("")
print(dfFinal)
dfFinal.to_excel(ticket1+"-"+ticket2+"-"+ticket3+"-"+ticket4+".xlsx")

