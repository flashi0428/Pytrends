#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pytrends
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=360)
kw_list = ["X"]
pytrends.build_payload(kw_list, cat=67, timeframe='today 5-y', geo='MX', gprop='')
Visits = pytrends.get_historical_interest(kw_list, year_start=2019, month_start=8, day_start=30, hour_start=0, year_end=2019, month_end=9, day_end=3, hour_end=0, cat=0, geo='', gprop='', sleep=0)
df=Visits
export_excel = df.to_excel (r'C:\Users\X\OneDrive\Desktop\Archive.xlsx', index = 'date', header=True) 

