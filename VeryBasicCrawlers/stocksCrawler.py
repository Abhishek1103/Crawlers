import requests
from bs4 import BeautifulSoup
import datetime

url1 = "https://economictimes.indiatimes.com/indices/sensex_30_companies"
url2 = "https://economictimes.indiatimes.com/hindi/indices/nifty_50_companies"

lst = [url1, url2]

stock = open("/home/aks/Desktop/stocks.txt","a")
d = datetime.datetime.now().strftime ("%d")
stock.write(str(d)+" ")
for url in lst:
    sourceCode = requests.get(url, proxies=proxy)
    data = sourceCode.text
    #print(data)
    soup = BeautifulSoup(data, "html.parser")

    for link in soup.find_all('div'):
        if str(link.get('id')) == "ltp":
            print(link.text)
            stock.write(str(link.text)+" ")

stock.write("\n")
stock.close()
# sourceCode = requests.get(url3, proxies=proxy)
# data = sourceCode.text
# soup = BeautifulSoup(data, "html.parser")
# #for i in range(1):
# for link in soup.find_all('span'):
#     #print(link.text)
#     #s = str(link.get('class'))
#     #if s[0:5] == "last_":
#     if str(link.get('class')) == "_Rnb fmob_pr fac-l":
#         print(link.text)
