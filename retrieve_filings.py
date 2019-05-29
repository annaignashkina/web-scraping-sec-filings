import urllib.request as ur
import os
import zipfile
import pandas as pd
from bs4 import BeautifulSoup as bf
import re
import time

# set how many columns/rows you want to display in pandas
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)

# Directory to store filings
dir = 'put ur dir here'

# set the working directory here
folder0 = 'put ur dir here'
os.chdir(folder0)


#download filings based on links from master files
i=0
df0 = pd.DataFrame()
for year in range(1994, 2018):
    for qtr in range(1,5):
        filename = folder0 + str(year)+'Q' + str(qtr) + 'master.idx'
        with open(filename) as f:
            for n, line in enumerate(f):
                if i==0:
                    if 'txt' in line:
                        n_line = n + 1
                        i = i + 1
                else:
                    break
        df = pd.read_csv(filename, skiprows=list(range(0, n_line-3))+[n_line-2], sep='|',\
         encoding = 'ISO-8859-1')
# Here you can change the type of filings
        df = df[df['Form Type'].apply(lambda x: True if '13F-HR' in x else False)]
        df0 = df0.append(df)

df0.to_csv('filings_links_1994_2017_13fhr.csv')

url = 'https://www.sec.gov/Archives/'
df0 = pd.read_csv(folder0+'filings_links_1994_2017_13fhr.csv', index_col=0)
df0 = df0.reset_index(drop=True)
df0['date'] = pd.to_datetime(df0['Date Filed'], format='%Y-%m-%d')
years = df0.date.dt.year.unique()

#make sure the directories with years are alwaredy in place, if not use

#if not os.path.exists(os.path.dirname(filename)):
#    try:
#        os.makedirs(os.path.dirname(filename))
#        ...
for year in years:
    os.chdir(dir+str(int(year)))
    df = df0[df0.date.dt.year==year]
    for i, row in df.iterrows():
        filename = row['Filename']
        url0 = url + filename
        filename = filename.split('/')[-1]
        try:
            ur.urlretrieve(url0, filename)
            time.sleep(0.1)
        except Exception:
            pass


# The last step can take a while
