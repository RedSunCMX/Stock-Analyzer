#This program runs through all stocks and finds stocks that have had an uncharacteristic and recent upward movement.
#The program returns the date of the uncharacteristic movement and the the percentage increase/decrease in the price of the stock
#relative to the price of the stock on the date of the breakthrough

import ystockquote #this is the python module that accesses the yahoo finance API
import VolCalcSD #VolCalcSD determines the Standard Deviation of a stock's movement
import get_percent_error20 #Isolates the stocks that meet the upward movement criteria
import nicedatestring #converts date to format that works with the ystockquote module for the Yahoo Finance API
import nicedatestring3
import datetime

R = get_percent_error20.get_movement_stocks()


symbols_list = R
one_month_ago = datetime.date.today() - datetime.timedelta(days=30)
enddate = nicedatestring.getnicedatetime()


def get_percent_change(symbol):
	startdate = str(nicedatestring3.getnicedatetime(one_month_ago))
	list_of_percent_changes = []
	
	pdata = ystockquote.get_historical_prices(symbol, startdate, enddate)
	del pdata[0]
	pdata.reverse()
	#print pdata
	
	# This gets the percent changes for all dates
	for n in range(len(pdata) - 1):
			day_before = float(pdata[n][4]) 
			day = float(pdata[(n + 1)][4])
			percent_change = ((day - day_before) / day) * 100
			#print day, pdata[(n + 1)][0], day_before, pdata[n][0], percent_change
			list_of_percent_changes.append(percent_change)
			
	#print list_of_percent_changes
	
	VolCalcSD.stdv(list_of_percent_changes)
	threshold = VolCalcSD.stdv(list_of_percent_changes) * 2
	print "threshold", threshold
			
		
	#This determines the price and date when the breakthrough happened
	for p in range(len(pdata) - 1):
			day_before = float(pdata[p][4]) 
			day = float(pdata[(p + 1)][4])
			percent_change = ((day - day_before) / day) * 100
			if percent_change > threshold:
				print day, pdata[p+1][0], day_before, pdata[(p)][0], percent_change
				date_of_threshold_penetration = pdata[p+1][0]
				print 
				print 
				breakthrough = percent_change
				print "breakthrough", date_of_threshold_penetration, breakthrough
				break
				list_of_percent_changes.append(percent_change)
				
	#Now I have to figure out how to get the percent change per day since penetration
	startdate = date_of_threshold_penetration.replace('-','') #This takes out the dashes from the date it was penetrated
	
	pdata = ystockquote.get_historical_prices(symbol, startdate, enddate)
	del pdata[0]
	pdata.reverse()
	print pdata[0][4]
	print
	print symbol
	
	for n in range(1, len(pdata)):
			closing_price = float(pdata[n][4]) 
			price_that_penetration_occurred = float(pdata[0][4])
			print pdata[n][0], closing_price, ((closing_price - price_that_penetration_occurred) / price_that_penetration_occurred) * 100
			



for sym in symbols_list:
	if ystockquote.get_price(sym) > 20.0:
		try: 
			get_percent_change(sym)
		except: 
			continue

print R





