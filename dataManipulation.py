
#write calendar date as DD/MM/YYY AND
#only get the seconds, minutes and hour component of the time (without miliseconds)
def formattedTime(oldTime):
	#calendar date computation
	calendarDateOld = oldTime[:10]

	day = calendarDateOld[-2:]
	month = calendarDateOld[5:7]
	year = calendarDateOld[:4]

	calendarDateNew = day + "." + month + "." + year

	#clock time computation
	clock = oldTime[11:19]

	return (calendarDateNew, clock)