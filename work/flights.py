#!/usr/bin/python
import Util, datetime
from datetime import timedelta
U = Util.Util()
#URL="firefox.exe -new-tab http://www.hipmunk.com/#!SFO.LIM,"
#URL="firefox.exe -new-tab http://www.hipmunk.com/#!JFK.SJC,"
#URL="open -a Firefox.app -new-tab http://www.hipmunk.com/#!SFO,LIM,"
URL="open -a Firefox.app -new-tab http://www.hipmunk.com/#!ELP,SFO"
#NICHI=10
NICHI=10
WEEKS_TO_SEARCH=15
START_DATE=datetime.datetime(2012,6,7)
def main():
	global NICHI,U,START_DATE
	#dt = datetime.datetime(2012,7,26)
	#dt = datetime.datetime(2012,5,24)
	td = timedelta(days=7)
	#U.runCmd("firefox")
	for i in range(WEEKS_TO_SEARCH):
		cmd =makeURL(START_DATE,NICHI)
		U.printStep(cmd)
		U.runCmd(cmd)
		START_DATE = START_DATE+td


def makeURL(date,dios):
	global URL
	td = timedelta(days=dios)
	nudt = date+td
	d1 = dateToString(date.ctime().split()[1:3])
	d2 = dateToString(nudt.ctime().split()[1:3])
	return URL+d1+"."+d2
def dateToString(date):
	return str(date[0])+str(date[1])

main()
