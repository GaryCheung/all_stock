from bs4 import BeautifulSoup
import requests
import pymysql
import time

url = 'http://quote.eastmoney.com/stocklist.html'
web_data = requests.get(url)
soup = BeautifulSoup(web_data.text,'lxml')

name = soup.select('div.quotebody > div > ul > li > a')
# print(name)

allstock = []
for names in name:
    allstock.append(names.get_text().encode('latin1','ignore').decode('gbk'))

print(allstock)