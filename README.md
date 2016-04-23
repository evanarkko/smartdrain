# smartdrain
Repository for Smart Water Hackaton scripts

####Preparations:

Get FreeTDS : http://www.freetds.org/
```
$ pip install pymssql
```

Import pymssql:
```
$ python
>>> import pymssql
```
####Usage:
```
$ python allstations.py '2016-01-01' '2016-01-16'
```
or print to file:
```
$ python allstations.py '2016-01-01' '2016-01-16' > 'yourfilename.txt'
```
..to print first two weeks of all stations from 1.1.2016-15.1.2016. 

You need to edit SQL query to get more than first 100 rows.
```
#db query
	cursor.execute("SELECT TOP 100 STS, ...
```
change to:
```
#db query
	cursor.execute("SELECT TOP 200000 STS, ...
```
or appropriate to your range.
