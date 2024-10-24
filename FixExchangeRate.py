#!/usr/bin/python3
'''This program is written to get queries for 
Fix Exchange rate from the Al Bank directly and to be run in db.
Importing some libs'''
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup as soup

# Initializing variable
url = 'https://www.bankofalbania.org/Markets/Official_exchange_rate/'

response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = response.content

fer = soup(webpage, "html.parser")

# Extracting data for article section
bodyHtml = fer.find('div', {'class' : 'mb-2'})
bodyTable = fer.find('table', {'class' : 'table'})

# Calculating result
res = bodyHtml.get_text()
tdata = bodyTable.get_text()

# Printing the result
udate = res[13:23]

date_object = datetime.strptime(udate, '%d.%m.%Y').date()
udate = date_object.strftime("%d/%m/%Y")
today = date.today()

d1 = today.strftime("%d/%m/%Y")
sysdate = datetime.strptime(d1, '%d/%m/%Y').date()

clst = tdata.split()
eur = clst[15]
usd = clst[11]

eur = float(eur)
usd = float(usd)

def exchange():
    '''This is the main function which generates the sql query.'''
    print("Date on Website: ", udate)
    print("Today\'s date: ", sysdate)
    print("USD :", usd, " EUR:", eur)
    print("==================================")
    
    if sysdate > date_object:
        print("Not Updated!")
    else:
        print("Currency Rate Updated.")    
    
    usdq = f"select VF_CONFIG_CUR_RATES_FUNC ('8','{usd}','840','USD to Albanian Lek','{udate}') from dual;"
    eurq = f"select VF_CONFIG_CUR_RATES_FUNC ('8','{eur}','978','EUR to Albanian Lek','{udate}') from dual;"
    dateq = f"select * from vf_config_cur_rates_t where effective_date in ('{udate}');"    
    
    queryList = ['\n', usdq, eurq, dateq, '\n']    
    for query in queryList:
        print(query)

if __name__ == "__main__":
    exchange()
