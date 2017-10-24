"""
Author: Abhishek
Description: This module will have class to scrape NSE data from web.

Equity Bhav URL     : https://www.nseindia.com/content/historical/EQUITIES/2017/AUG/cm17AUG2017bhav.csv.zip
Derivative Bhav URL : https://www.nseindia.com/content/historical/DERIVATIVES/2017/SEP/fo20SEP2017bhav.csv.zip
"""

#from dateutil.parser import parse

import shutil
#import urllib2
import zipfile
import datetime
import urllib.request
from dateutil import parser

class Nse_scrapper():

	nse_bhav_url_template = "https://www.nseindia.com/content/historical/"
	http_header = {'User-Agent': 'mybot', 'Accept': '*/*',"Referer": "https://www.nseindia.com/products/content/equities/equities/archieve_eq.htm"}

	def nse_bhavcopy_scrapper(self, act_date):
		url2 = "https://www.nseindia.com/content/historical/EQUITIES/2017/AUG/cm17AUG2017bhav.csv.zip"
		segment = 'EQUITIES'
		year = act_date.strftime('%Y')
		month =  act_date.strftime('%^b')
		bhav_name = act_date.strftime('cm%d%^b%Ybhav.csv.zip')
		url = nse_scrapper_obj.nse_bhav_url_template+segment+'/'+year+'/'+month+'/'+bhav_name
		request = urllib.request.Request(url , headers=nse_scrapper_obj.http_header)
		file_name = 'zip_dump/'+bhav_name
		out_csv = 'csv_dump/'
		try:
			with (urllib.request.urlopen(request)) as response, open(file_name, 'wb') as out_file:
		  	  	shutil.copyfileobj(response, out_file)
	    			with zipfile.ZipFile(file_name) as zf:
	        			zf.extractall(out_csv)
			nse_scrapper_obj.success_flag = 1
			with open ('log/nse_scrapper_log', 'a+') as file_obj:
				file_obj.write("Successfuly downloaded bhav copy of date " + act_date.strftime('%Y%d%m') +'\n')
				file_obj.write("Passed URL : " + url + '\n\n')
			

		except:
			#print ("There is no data for " + str(act_date))
			nse_scrapper_obj.success_flag = 0
			with open ('log/nse_scrapper_log', 'a+') as file_obj:
				file_obj.write("Failed to download bhav copy of date " + act_date.strftime('%Y%d%m')+ '\n')
				file_obj.write("Failed URL : " + url + '\n\n')

			#print (url_responce_code)

	def nae_date_range_bhavcopy(self, start_date, end_date):
		date_list = utility_obj.list_date_in_range(start_date, end_date)
		print (date_list)
		for bhav_date in date_list:
			nse_scrapper_obj.nse_bhavcopy_scrapper(bhav_date)

	def nse_day_duration_bhavcopy(self, days):
		bhav_date = datetime.date.today() 
		day_counter = days
		step = datetime.timedelta(days=1)
		while day_counter > 0 :
			nse_scrapper_obj.nse_bhavcopy_scrapper(bhav_date)
			if (nse_scrapper_obj.success_flag == 1):
				day_counter = day_counter - 1
			bhav_date -= step
			

	def nse_bhavcopy_latest(self):
		pass

class Utility():

	def list_date_in_range(self,start_date, end_date):
		date_list = []
		start = parser.parse(start_date)
		#start = start.strftime('%Y-%m-%d')
		#start = datetime.strptime(start,'%Y-%m-%d')
		end = parser.parse(end_date)
		#end = end.strftime('%Y-%m-%d')
		#datetime.strptime(end,'%Y-%m-%d')
		step = datetime.timedelta(days=1)
		while start <= end :
			date_list.append(start)
			start += step
		return date_list

	def prev_date(self, day_numbers):
		pass





dt = "2017-09-11"
act_date = parser.parse(dt)
nse_scrapper_obj = Nse_scrapper()
utility_obj = Utility()
#utility_obj.list_date_in_range('2017-08-17','2017-09-17')
#nse_scrapper_obj.nse_bhavcopy_scrapper(act_date)
#nse_scrapper_obj.nae_date_range_bhavcopy('2017-09-1','2017-09-30')
#nse_scrapper_obj.nse_day_duration_bhavcopy(15)
