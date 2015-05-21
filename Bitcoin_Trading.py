__author__ = 'steveleec'
#Bitcoin_Trading.py

import welcome
import applyTrading
import ownExceptions

welcome.welcome()
daysAmount1 = 60
daysAmount2 = 20

try:
    opt = raw_input('Chose an option (A): ').upper()
    ownExceptions.checkChoiceGA(opt)

    if opt == "A":
        averageSup60 = applyTrading.gettingAveragePrice(applyTrading.gettingPriceArray(daysAmount1))
        averageInf20 = applyTrading.gettingAveragePrice(applyTrading.gettingPriceArray(daysAmount2))
        lastPrice = applyTrading.gettingPriceArray(1)[0]
        applyTrading.suggestAction(averageSup60, averageInf20)

except ownExceptions.WrongChoiceGA:
    ownExceptions.printChoiceExceptionGA()
