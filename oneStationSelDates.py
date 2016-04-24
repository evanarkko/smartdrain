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
	tomorrowString = '2016-02-01'
	stationid = '1023'

	#
	cursor.execute("SELECT TOP 2000 STATION_NAME, STS, CODE, OUTPUT_QUANTITY\
		FROM [AWR].[dbo].[HSY_MES_PUMP_1H], [AWR].[dbo].[HSY_TARGETS] \
		WHERE STS > (%s) \
		AND STS < (%s) \
		AND OUTPUT_QUANTITY < 5000 \
		AND OUTPUT_QUANTITY > 0 \
		AND STATION_NAME = NAME \
		AND CODE = (%s) \
		ORDER BY STS ASC", (dayWantedString, tomorrowString, stationid))

	for row in cursor.fetchall():
		print row[0] + " " + str(row[1]) + " " + str(row[2]) + " " + str(row[3])
		#print str(row[0]) + " " + str(row[1]) + " " + str(row[2])

main()