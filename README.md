# bitcoinTrading

ALGORITHM TO TRADE BITCOINS

So far, bitcoin traders are using a limited amount of tools for trading. There is still a lack of development within this area. That represents a huge opportunity for borrowing some proved knowledge from a similar market: stock trading. For that reason, I am proposing a algorithm well used in the latter market that suggests to buy or sell a bitcoin at a particular moment.

This algorithm is based on the following technique: Moving Average Price (60 and 20). 60 and 20 make reference to the amount of days used to calculate the average.

According to the Moving Average Price technique, there is suggested moments to sell or buy bitcoins or shares. Those cases are the following:

	If the 20 days average price curve is above the 60 days average price curve, that represents a opportunity to buy. In other words, if the green line is above the red one there is an uptrend. Therefore, the price will keep raising: time to buy.

	The opposite is true as well. If the the 20 days average price curve is below the 60 days average price curve, that represents a opportunity to sell. This will happen when the red one is above the green one within a downward trend: time to sell.

	The best moment for buying bitcoins or shares is when a “golden cross” is achieved. That happens when the red line (60 days average curve) is cut by the green from below placing the latter one above the red one. That specific cross represents the beginning of an uptrend behavior.

	Investors should be careful about the “dead cross.” This moment takes pace when the red line (60 days average) cut the green one (20 days average) from above placing the latter one below the red one. Usually, that point represent the beginning of a downtrend behavior. 

	In brief, the Moving Average Price technique could be summarize as buy after golden crosses and sell after dead crosses.
	
Parts of the Program:
1. Bitcoin_Trading.py:	It is the first creen and it has all the connections to other parts of the program.
2. welcome.py:	Displays a welcoming message to the user.
3. ownExceptions.py:	There is one exception included in this part.
4. applyTrading:	It contains the algorithm trading and displays the conclusion about the investment.
