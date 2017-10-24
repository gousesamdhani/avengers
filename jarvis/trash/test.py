import datetime

#def print_dates(start_date, end_date)
start_date = '2017-08-17'
end_date = '2017-09-17'

start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
end = datetime.datetime.strptime(end_date, '%Y-%m-%d')

step = datetime.timedelta(days=1)
while start <= end :
	print (start)
	start += step
