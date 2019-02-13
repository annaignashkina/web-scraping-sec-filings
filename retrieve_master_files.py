import urllib.request as ur
import os
import time

# set the working directory here
os.chdir('C:\\Users\\Anna')

# Download master files with the full index of different kinds of filings (10-K, 13D, 8-K, etc.)
for year in range(1999, 2018):
    for qtr in range(1,5):
        url = 'https://www.sec.gov/Archives/edgar/full-index/' + str(year) + '/QTR' + str(qtr) + \
        '/master.idx'
        ur.urlretrieve(url, str(year)+'Q' + str(qtr) + 'master.idx')
        time.sleep(1)
