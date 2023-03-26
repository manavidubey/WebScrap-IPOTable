import urllib.request

from pprint import pprint

from html_table_parser.parser import HTMLTableParser
import pandas as pd


def url_get_contents(url):

	req = urllib.request.Request(url=url)
	urlreq = urllib.request.urlopen(req)

	return urlreq.read()

xhtml = url_get_contents('https://www.motilaloswal.com/upcoming-ipo').decode('utf-8')

m = HTMLTableParser()

m.feed(xhtml)

pprint(m.tables[1])

print("Dataframe\n")
print(pd.DataFrame(m.tables[1]))
pd.DataFrame(m.tables[1]).to_excel('tables.xlsx', index=False)

import datetime
import time

# Get current date
current_date = datetime.date.today()

# Loop through each row in the table and check the date
for i in range(len(m.tables[1])):
    row = m.tables[1][i]
    date_str = row[3] # Assuming the date is in the third column
    
    # Convert date string to datetime object
    date_obj = datetime.datetime.strptime(date_str, '%d-%b-%Y')
    
    # Calculate difference between current date and table date
    delta = date_obj.date() - current_date
    
    # If the difference is less than or equal to 7 days, add alarm code
    if delta.days <= 7:
        alarm_code = time.strftime('%H:%M:%S', time.gmtime(delta.seconds))
        m.tables[1][i][3] = f"{date_str} ({alarm_code})" # Add alarm code to date string

# Print updated table
pprint(m.tables[1])
