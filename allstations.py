import pymssql
from datetime import datetime
from datetime import timedelta
import sys, getopt
"""
Pumping station data reader
param: starting date, ending date ('YYYY-DD-MM' 'YYYY-DD-MM')
return: (print to console)
"""
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

#def main(start, end, station_id):
def main(argv):
	#connection
	conn = connect()
	cursor = conn['AWR'].cursor()

	dayWantedString = sys.argv[1]
	tomorrowString = sys.argv[2]

	#db query
	cursor.execute("SELECT TOP 100 STS, OUTPUT_QUANTITY, REGION_FLOW, NORMAL_WASTE_WATER, STATION_NAME, CODE, NEXT_STATION \
		FROM [AWR].[dbo].[HSY_MES_PUMP_1H], [AWR].[dbo].[HSY_TARGETS] \
		WHERE STS > (%s) \
		AND STS < (%s) \
		AND OUTPUT_QUANTITY < 10000 \
		AND OUTPUT_QUANTITY > 0 \
		AND STATION_NAME = NAME \
		AND TARGET_TYPE = 'JVP' \
		ORDER BY STS ASC", (dayWantedString, tomorrowString))

	#print query
	print "\nAWR: day, pumpId, amount\n"
	for row in cursor.fetchall():
		print row
		#here you can do stuff with the data
		#row[0] = datetime (STS)
		#row[1] = output quantity 
		#...

if __name__ == "__main__":
   main(sys.argv[1:])