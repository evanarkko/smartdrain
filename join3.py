import pymssql

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


cursor.execute("SELECT CODE, [AWR].[dbo].[FLOW_QUALITY].STATION, QUALITY, AREA, WGS_84\
    FROM [AWR].[dbo].[FLOW_QUALITY]\
    INNER JOIN [AWR].[dbo].[AREA]\
    ON [AWR].[dbo].[FLOW_QUALITY].STATION = [AWR].[dbo].[AREA].STATION\
    INNER JOIN [AWR].[dbo].[HSY_TARGETS]\
    ON [AWR].[dbo].[FLOW_QUALITY].STATION = [AWR].[dbo].[HSY_TARGETS].STATION\
    ORDER BY [AWR].[dbo].[FLOW_QUALITY].STATION ASC")


print "code: stationname quality area wgs"

for row in cursor.fetchall():
    code = str(row[0])
    stationname = str(row[1])
    quality = str(row[2])
    area = str(row[3])
    wgs = str(row[4])
    print code + ": " + stationname + " " + quality + " " + area + " " + wgs