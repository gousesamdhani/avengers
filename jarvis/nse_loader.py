"""
Author: Abhishek
Description: This script will load NSE data to HULK
"""

from numpy import genfromtxt
from time import time
from datetime import datetime
from sqlalchemy import Column, Integer, DECIMAL, Float, Date, String, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv
import pandas as pd
from sqlalchemy import *


class NSE_LOADER():

	def load_nse_eod_staging(self):
		__tablename__ = 'nse_eod_staging'

		SYMBOL = Column(VARCHAR(20), primary_key=True, nullable=False)   
		SERIES = Column(VARCHAR(5), primary_key=True, nullable=False) 
		OPEN = Column(DECIMAL(10,5)) 
		HIGH = Column(DECIMAL(10,5)) 
		LOW = Column(DECIMAL(10,5))
		CLOSE = Column(DECIMAL(10,5))
		LAST = Column(DECIMAL(10,5))
		PREVCLOSE = Column(DECIMAL(10,5))
		TOTTRDQTY = Column(Integer)   
		TOTTRDVAL = Column(DECIMAL(15,5))
		TIMESTAMP = Column(Date, primary_key=True, nullable=False)
		TOTALTRADES = Column(Integer)
		ISIN = Column(VARCHAR(20))

		engine = create_engine("{flavor}://{username}:{password}@{host}/{database}".format(flavor='mysql+pymysql', host='localhost', database='hulk', username='root', password='93@gmail.com'))
		metadata = MetaData()
		metadata.create_all(engine)
		file_name = 'cm21AUG2017bhav.csv'
		df = pd.read_csv(file_name)
		df.to_sql(con=engine, index = False, name=__tablename__, if_exists='replace')

nse_loader_obj = NSE_LOADER() 
nse_loader_obj.load_nse_eod_staging()
