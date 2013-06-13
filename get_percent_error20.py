#Change startdate to pick where the SD calculation should start from

import ystockquote
import VolCalcSD
import nicedatestring
import nicedatestring3
import datetime

def get_movement_stocks():

	R = ['AOL', 'A', 'AA', 'AAPL', 'ABB', 'ABC', 'ABT', 'ABX', 'ACAD', 'ACAS', 'ACE', 'ACI', 'ACN', 'ADBE', 'ADI', 'ADM', 'ADP', 'ADSK', 'AEE', 'AEP', 'AES', 'AET', 'AFL', 'AGN', 'AGO', 'AIG', 'AINV', 'AIV', 'AKAM', 'AKS', 'ALKS', 'ALL', 'ALTR', 'ALXN', 'AMAT', 'AMD', 'AMGN', 'AMRN', 'AMSC', 'AMT', 'AMTD', 'AMX', 'AMZN', 'ANF', 'ANH', 'ANN', 'APA', 'APC', 'APOL', 'ARIA', 'ARNA', 'ARO', 'ARRS', 'ATI', 'ATML', 'ATVI', 'AU', 'AVB', 'AVP', 'AVT', 'AXL', 'AXP', 'AXS', 'AZN', 'BA', 'BAC', 'BAX', 'BBBY', 'BBD', 'BBT', 'BBY', 'BCE', 'BCS', 'BDN', 'BG', 'BHI', 'BIIB', 'BK', 'BMC', 'BMY', 'BP', 'BPO', 'BR', 'BRCD', 'BRCM', 'BSX', 'BTU', 'BUD', 'BVN', 'BXP', 'BYD', 'C', 'CA', 'CAG', 'CAH', 'CAM', 'CAT', 'CBB', 'CBG', 'CBI', 'CBL', 'CCE', 'CCI', 'CCJ', 'CCL', 'CDR', 'CEDC', 'CELG', 'CFN', 'CHK', 'CHRW', 'CHS', 'CI', 'CIEN', 'CIG', 'CIT', 'CL', 'CLF', 'CLI', 'CLP', 'CMA', 'CMCSA', 'CMCSK', 'CME', 'CMI', 'CMS', 'CNO', 'CNP', 'CNQ', 'CNX', 'COCO', 'COF', 'COG', 'COH', 'COP', 'COST', 'CPB', 'CPN', 'CPRT', 'CREE', 'CRK', 'CRM', 'CRUS', 'CSC', 'CSCO', 'CSE', 'CSTR', 'CSX', 'CTL', 'CTRP', 'CTSH', 'CTXS', 'CVC', 'CVS', 'CVX', 'CX', 'CXW', 'CY', 'CYH', 'CZR', 'DAL', 'DB', 'DCTH', 'DD', 'DDR', 'DE', 'DECK', 'DELL', 'DF', 'DFS', 'DG', 'DHI', 'DHR', 'DIS', 'DISH', 'DLTR', 'DNDN', 'DNR', 'DOV', 'DOW', 'DRE', 'DRI', 'DTV', 'DUK', 'DV', 'DVAX', 'EAT', 'EBAY', 'ECA', 'EFX', 'EIX', 'EL', 'ELN', 'ELY', 'EMC', 'EMN', 'EMR', 'ENDP', 'EOG', 'EPD', 'EQR', 'ESRX', 'ESV', 'ETFC', 'ETN', 'ETR', 'EW', 'EXC', 'EXEL', 'F', 'FAF', 'FAST', 'FCS', 'FCX', 'FDO', 'FDX', 'FE', 'FHN', 'FII', 'FINL', 'FITB', 'FL', 'FLEX', 'FLR', 'FNF', 'FNFG', 'FNSR', 'FOSL', 'FRX', 'FSL', 'FST', 'FTE', 'FTI', 'FULT', 'G', 'GCI', 'GD', 'GDI', 'GDP', 'GE', 'GFI', 'GG', 'GGB', 'GGP', 'GILD', 'GIS', 'GLW', 'GM', 'GMCR', 'GME', 'GNTX', 'GNW', 'GOOG', 'GPK', 'GPOR', 'GPS', 'GRMN', 'GS', 'GSK', 'GT', 'GTI', 'HAL', 'HAS', 'HBAN', 'HCA', 'HCBK', 'HCP', 'HD', 'HIG', 'HL', 'HMA', 'HMY', 'HNZ', 'HOLX', 'HON', 'HOT', 'HOV', 'HP', 'HPQ', 'HRB', 'HSP', 'HUM', 'IACI', 'IBM', 'IBN', 'IDTI', 'IGT', 'ILMN', 'INCY', 'INFA', 'INFN', 'INFY', 'ING', 'INTC', 'INTU', 'INVN', 'IP', 'IPG', 'IR', 'ISIS', 'ITW', 'JBL', 'JBLU', 'JCI', 'JCP', 'JDSU', 'JEF', 'JNJ', 'JNPR', 'JNS', 'JPM', 'JRCC', 'JWN', 'K', 'KBH', 'KEG', 'KERX', 'KEY', 'KGC', 'KIM', 'KLAC', 'KMB', 'KMI', 'KO', 'KR', 'KSS', 'KWK', 'LBTYA', 'LEAP', 'LEN', 'LF', 'LGF', 'LLTC', 'LLY', 'LM', 'LMT', 'LNC', 'LOW', 'LPX', 'LRCX', 'LSI', 'LTD', 'LUV', 'LVLT', 'MAR', 'MAS', 'MAT', 'MBI', 'MBT', 'MCD', 'MCHP', 'MCK', 'MCO', 'MDR', 'MDRX', 'MDT', 'MET', 'MFA', 'MFC', 'MGM', 'MHP', 'MHR', 'MMC', 'MMM', 'MNKD', 'MNST', 'MO', 'MOH', 'MON', 'MRK', 'MRO', 'MRVL', 'MSFT', 'MTG', 'MTOR', 'MTW', 'MU', 'MUR', 'MXIM', 'MYGN', 'MYL', 'NAV', 'NBG', 'NBIX', 'NBL', 'NCR', 'NCT', 'NDAQ', 'NE', 'NEM', 'NFLX', 'NFX', 'NI', 'NIHD', 'NKE', 'NLY', 'NOC', 'NOK', 'NPSP', 'NR', 'NRG', 'NSC', 'NTAP', 'NTE', 'NUAN', 'NUE', 'NVDA', 'NVO', 'NVS', 'NWS', 'NXY', 'O', 'OCLR', 'OCN', 'ODP', 'OEH', 'OHI', 'OMC', 'ONCY', 'ONNN', 'ONXX', 'ORCL', 'ORLY', 'OXY', 'PAA', 'PANL', 'PAYX', 'PBCT', 'PBF', 'PBI', 'PBR', 'PCAR', 'PDLI', 'PDS', 'PEG', 'PEP', 'PER', 'PFE', 'PFG', 'PG', 'PGH', 'PGR', 'PHH', 'PII', 'PLCM', 'PLD', 'PMCS', 'PMT', 'PNC', 'POM', 'POT', 'PPG', 'PPHM', 'PPL', 'PRGO', 'PRU', 'PSEC', 'PTEN', 'PVA', 'PVH', 'PWER', 'PWR', 'PXD', 'QCOM', 'RAD', 'RAI', 'RCL', 'RDC', 'RDN', 'REGN', 'RF', 'RFMD', 'RGC', 'RIG', 'RIO', 'ROST', 'RRC', 'RRD', 'RSG', 'RSH', 'RTN', 'S', 'SAN', 'SAP', 'SBUX', 'SDS', 'SE', 'SEE', 'SFD', 'SID', 'SINA', 'SIRI', 'SKM', 'SKS', 'SLB', 'SLM', 'SNDK', 'SNE', 'SNH', 'SNV', 'SNY', 'SO', 'SONS', 'SPF', 'SPLS', 'SPN', 'SQNM', 'STI', 'STJ', 'STLD', 'STM', 'STR', 'STSI', 'STT', 'STX', 'STZ', 'SU', 'SVM', 'SVU', 'SWC', 'SWFT', 'SWKS', 'SWN', 'SWY', 'SYK', 'SYMC', 'SYY', 'T', 'TCB', 'TE', 'TEF', 'TER', 'TEVA', 'TEX', 'TGT', 'THC', 'TIBX', 'TIVO', 'TJX', 'TLAB', 'TLM', 'TMO', 'TOL', 'TOT', 'TQNT', 'TS', 'TSM', 'TSN', 'TSO', 'TTWO', 'TWI', 'TWTC', 'TWX', 'TXN', 'TXT', 'TYC', 'TZA', 'UBS', 'UDR', 'UN', 'UNH', 'UNM', 'UNP', 'UPS', 'URBN', 'URI', 'USB', 'USG', 'UTX', 'V', 'VIP', 'VLO', 'VOD', 'VRSN', 'VSH', 'VTR', 'VVUS', 'VZ', 'WAG', 'WCRX', 'WDC', 'WEC', 'WEN', 'WFC', 'WFR', 'WFT', 'WHX', 'WIN', 'WLT', 'WM', 'WMB', 'WMT', 'WNC', 'WRE', 'WY', 'WYNN', 'X', 'XEL', 'XL', 'XLNX', 'XOM', 'XRX', 'YHOO', 'YUM', 'ZION', 'ZQK']
	
	symbols_list = R
	enddate = nicedatestring.getnicedatetime()
	three_months_ago = datetime.date.today() - datetime.timedelta(days=90)
	
	quad_list = []
	
	
	def get_percent_change(symbol):
		startdate =  str(nicedatestring3.getnicedatetime(three_months_ago))
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
					
		#Gets the percent change per day since penetration
		startdate = date_of_threshold_penetration.replace('-','') #This takes out the dashes from the date it was penetrated
		
		pdata = ystockquote.get_historical_prices(symbol, startdate, enddate)
		print ""
		print startdate
		del pdata[0]
		pdata.reverse()
		print pdata[0][4]
		print
		print symbol
		
		if ((float(pdata[1][4]) - float(pdata[0][4])) / float(pdata[0][4])) > 0:
			if ((float(pdata[2][4]) - float(pdata[0][4])) / float(pdata[0][4])) > 0:
				if ((float(pdata[3][4]) - float(pdata[0][4])) / float(pdata[0][4])) > 0:
					if ((float(pdata[4][4]) - float(pdata[0][4])) / float(pdata[0][4])) > 0:
						if startdate[:6] == nicedatestring.getnicedatetime()[:6]: #shows the history for the month in this line?
							quad_list.append(sym)
							for n in range(1, len(pdata)):
								closing_price = float(pdata[n][4]) 
								price_that_penetration_occurred = float(pdata[0][4])
								print pdata[n][0], closing_price, ((closing_price - price_that_penetration_occurred) / price_that_penetration_occurred) * 100
			
	
	
	
	for sym in symbols_list:
		
			try: 
				get_percent_change(sym)
			except: 
				continue
	
	return quad_list
	
print get_movement_stocks()


