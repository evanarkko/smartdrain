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

cursor.execute("SELECT TOP 2000 STS, OUTPUT_QUANTITY, REGION_FLOW, NORMAL_WASTE_WATER, STATION_NAME, CODE, NEXT_STATION \
        FROM [AWR].[dbo].[HSY_MES_PUMP_1H], [AWR].[dbo].[HSY_TARGETS] \
        WHERE STS > (%s) \
        AND STS < (%s) \
        AND OUTPUT_QUANTITY < 5000 \
        AND OUTPUT_QUANTITY > 0 \
        AND STATION_NAME = NAME \
        AND CODE = (%s) \
        ORDER BY STS ASC")


print "code: stationname quality area wgs"

for row in cursor.fetchall():
    code = str(row[0])
    name = str(row[1]).decode('iso-8859-1')
    lat = str(row[2])
    longi = str(row[3])
    print code + " " + name + " " + lat + " " + longi

    #t = s.decode('iso-8859-1')