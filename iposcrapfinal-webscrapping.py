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
