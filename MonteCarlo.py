import pandas_datareader as web
import numpy as np
import matplotlib.pyplot as pt


ticker = "MSFT"
startDate = "2018-11-18"
endDate = "2019-11-18"

df = web.DataReader(ticker, "yahoo", startDate, endDate)
df = df[["Close"]]

dfTrain = web.DataReader(ticker, "yahoo", "2019-11-15", "2019-11-19")
dfTrain = dfTrain[["Close"]]
dfTrain["Pct"] = dfTrain["Close"].pct_change()

histMean = dfTrain["Pct"].mean()
histStd = dfTrain["Pct"].std()

print(histMean , histStd)

todayPrice = df["Close"][-1]
print(todayPrice)


timePoints = 252
scenarios = 100

for scenario in range(0,scenarios):
    prices = [todayPrice]
    moteCarloMoves = np.random.normal(histMean, histStd , timePoints)
    for move in moteCarloMoves:
      prices.append(prices[-1]*(1+move))

    days = list(range(0,253))
    pt.plot(days,prices)

pt.show()

# pt.hist(moteCarloMoves,timePoints)
# pt.show()
