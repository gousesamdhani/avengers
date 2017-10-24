import datetime
from dateutil import parser

def list_date_in_range(start_date, end_date):
	date_list = []
	start = parser.parse(start_date)
	end = parser.parse(end_date)


	#start_date = '2017-08-17'
	#end_date = '2017-09-17'

	#start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
	#end = datetime.datetime.strptime(end_date, '%Y-%m-%d')

	step = datetime.timedelta(days=1)
	while start <= end :
		date_list.append(start)
		start += step
	print (date_list)

list_date_in_range('2017-08-17','2017-09-17')

