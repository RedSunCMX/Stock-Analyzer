#given the symbol, the startdate, and the enddate, this function will return the volatility number to be used in the BlackScholes Calc

import ystockquote
import math

# Calculate mean of the values
def m(values):
        size = len(values)
        sum = 0.0
        for n in range(0, size):
                sum += values[n]
        return sum / size;

# Calculate standard deviation
def stdv(x):
    from math import sqrt
    n, mean, std = len(x), 0, 0
    for a in x:
		mean = mean + a
    mean = mean / float(n)
    for a in x:
		std = std + (a - mean)**2
    std = sqrt(std / float(n-1))
    return std

def volatlility_number(symbol, startdate, enddate):
	
	pdata = ystockquote.get_historical_prices(symbol, startdate, enddate)
	
	closing_price_list = []
	
	list_of_logs = []
	
	for p in pdata:
		closing_price_list.append(p[4])
	closing_price_list.remove('Close')
	
	nice = [float(i) for i in closing_price_list]
	#print "this is how nice", nice
	
	for n in range(1, (len(pdata) - 1)):
		day = float(pdata[n][4]) 
		day_before = float(pdata[(n + 1)][4])
		#print day
		#print day_before
		H = (day / day_before)
		G = math.log(H)
		list_of_logs.append(G)
		#print G
		#print ""
		
	standard_deviation = stdv(list_of_logs)
	volatility_number = (standard_deviation * math.sqrt(252))
	return volatility_number

print volatlility_number('IBM', '20130120', '20130205')

        
