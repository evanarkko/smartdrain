import pymssql
from datetime import datetime
from datetime import timedelta
import sys, getopt

def get_database(database):
    server = '10.144.72.11'
    user = 'AWR_DEV'
    password =  'NEO'
    conn = pymssql.connect(server, user, password, database)
    return conn

def connect():
    return {
        'AWR': get_database('AWR')
    }



def main():
#def main(argv):
	#connection
	conn = connect()
	cursor = conn['AWR'].cursor()

	dayWantedString = '2016-01-01'
	tomorrowString = '2016-01-02'
	stationid = '2016'

	#pumpID
	pumpID = 'JVP2016'

	cursor.execute("SELECT TOP 2000 STS, OUTPUT_QUANTITY, REGION_FLOW, NORMAL_WASTE_WATER, STATION_NAME, CODE, NEXT_STATION \
		FROM [AWR].[dbo].[HSY_MES_PUMP_1H], [AWR].[dbo].[HSY_TARGETS] \
		WHERE STS > (%s) \
		AND STS < (%s) \
		AND OUTPUT_QUANTITY < 5000 \
		AND OUTPUT_QUANTITY > 0 \
		AND STATION_NAME = NAME \
		AND CODE = (%s) \
		ORDER BY STS ASC", (dayWantedString, tomorrowString, stationid))

	#print query
	print "\nAWR: day, pumpId, amount\n"
	for row in cursor.fetchall():
		print row

main()