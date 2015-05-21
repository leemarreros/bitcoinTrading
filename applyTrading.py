__author__ = 'steveleec'
#applyTrading.py

def calculatingArray(days, j):
    result = []
    sourceCode = open('btcnCNY.csv','rb').read()
    splitSource = sourceCode.split('\n')
    for day in range(days):
        lastRowDay = splitSource[j+1]
        splitLineLast = lastRowDay.split(',')
        lastDate = float(splitLineLast[0])

        result.append(float(splitLineLast[1]))

        compRowDay = splitSource[j]
        splitLineComp = compRowDay.split(',')
        compDate = float(splitLineComp[0])

        i = 0
        while lastDate - compDate < 60*60*24:
            i -= 1
            compRowDay = splitSource[j + i]
            splitLineComp = compRowDay.split(',')
            compDate = float(splitLineComp[0])

        j += i
    return result

def gettingPriceArray(days):
    j = -2 -1 #This is reference of the very last row of the file 'btcnCNY.csv'.
    return calculatingArray(days, j)

def gettingAveragePrice(priceArray):
    sum = 0
    for i in range(len(priceArray)):
        sum += priceArray[i]
    return sum/len(priceArray)

def suggestAction(averageSup60, averageInf20):
    if averageSup60 > averageInf20:
        print "Summary:"
        print " Average 60 Day Price: {}".format(averageSup60)
        print " Average 20 Day Price: {}".format(averageInf20)
        print "A 'Dead Cross' has happened."
        print "Recommendation: SELL bitcoins"
        print "why? This is a downtrend."

    elif averageSup60 < averageInf20:
        print "Summary:"
        print " Average 60 Day Price: {}".format(averageSup60)
        print " Average 20 Day Price: {}".format(averageInf20)
        print "A 'Golden Cross' has happened."
        print "Recommendation: BUY bitcoins"
        print "why? This is an uptrend."

    else:
        print "Summary:"
        print " Average 60 Day Price: {}".format(averageSup60)
        print " Average 20 Day Price: {}".format(averageInf20)
        print "No conclusive."
