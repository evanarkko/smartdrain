import pymssql
import sys
def get_database(database):
    server = '10.144.72.11'
    user = 'AWR_DEV'
    password =  'NEO'
    conn = pymssql.connect(server, user, password, database)
    return conn

def connect():
    return {
        'AWR': get_database('AWR'), 
        'HSY_EL': get_database('HSY_EL')
    }

conn = connect()
cursor = conn['AWR'].cursor()


"""
cursor.execute("SELECT STATION, AREA \
    FROM [AWR].[dbo].[AREA]")
"""


"""
cursor.execute("SELECT STATION, QUALITY \
    FROM [AWR].[dbo].[FLOW_QUALITY]\
    WHERE STATION = STATION\
    ORDER BY STATION ASC")
"""

    #INNER JOIN [AWR].[dbo].[HSY_TARGETS]\
    #ON [AWR].[dbo].[HSY_TARGETS].NAME = [AWR].[dbo].[AREA].STATION\


cursor.execute("SELECT CODE, NAME, LAT, LONG\
    FROM [AWR].[dbo].[HSY_TARGETS]\
    ORDER BY CODE ASC")


print "code, stationname, lat, long"

for row in cursor.fetchall():
    print row