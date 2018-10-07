import requests as req
from bs4 import BeautifulSoup
from queue import *


#proxy = {"http": "http://username:password@<Proxy_IP:Port>/",
#                "https": "http://username:password@<Proxy_IP:Port>/"}
q = Queue()

linksFile = open("Links","a")
initialUrl = "https://timesofindia.indiatimes.com"
#source = req.get(initialUrl, proxies=proxy)
source = req.get(initialUrl)
data = source.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    s = str(link.get('href'))
    if(s[0] == 'h'):
        print(str(s))
        q.put(s)
        linksFile.write(s+"\n")
try:
    while q.empty() == False:
        url = q.get()
        source = req.get(url, proxies=proxy)
        data = source.text
        soup = BeautifulSoup(data, "html.parser")

        for link in soup.find_all('a'):
            s = str(link.get('href'))
            try:
                if(s[0] == 'h'):
                    print(str(s))
                    q.put(s)
                    linksFile.write(s+"\n")
            except Exception as ex:
                print(str(ex))
except Exception as ex:
    linksFile.close()
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    print("EXITING..!!")
