import datetime

def getnicedatetime(now):

	day = str(now.day)
	month = str(now.month)

	if len(day) == 1:
		day = "0" + day
	
	if len(month) == 1:
		month = "0" + month

	if len(str(now.day)) == 1 and len(str(now.month)) == 1:
		return str(now.year) + month + day
		
	if len(str(now.day)) == 2 and len(str(now.month)) == 1:
		return str(now.year) + month + str(now.day)
		
	if len(str(now.day)) == 1 and len(str(now.month)) == 2:
		return str(now.year) + str(now.month) + day