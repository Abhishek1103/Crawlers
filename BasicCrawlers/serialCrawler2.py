import requests as req
from bs4 import BeautifulSoup
from queue import *

#proxy = {"http": "http://username:password@<Proxy_IP:Port>/",
#                "https": "http://username:password@<Proxy_IP:Port>/"}

#q = Queue()
st = set()
st2 = set()
print("Enter initial URL: ", end="")

linksFile = open("DistinctLinks","w")
initialUrl = "https://timesofindia.indiatimes.com"
#initialUrl = "https://www.youtube.com/"
initialUrl = input()
#source = req.get(initialUrl, proxies=proxy)
source = req.get(initialUrl)
data = source.text
soup = BeautifulSoup(data, "html.parser")

for link in soup.find_all('a'):
    s = str(link.get('href'))
    if(s[0] == 'h'):
        print(str(s))
        st.add(s)
        #st2.add(s)
        #linksFile.write(s+"\n")
i=0
try:
    while i < 30000:
        url = st.pop()
        linksFile.write(str(url)+"\n")
        source = req.get(url, proxies=proxy)
        data = source.text
        soup = BeautifulSoup(data, "html.parser")

        for link in soup.find_all('a'):
            s = str(link.get('href'))
            try:
                if(s[0] == 'h'):
                    #print(str(s))
                    st.add(s)
                    #st2.add(s)
                    i += 1
                    if i%1000 == 0 :
                        print(i)
            except Exception as ex:
                print(str(ex)+": Invalid URL")
    for lnk in st:
        linksFile.write(str(lnk)+"\n")
    linksFile.close()
except Exception as ex:
    linksFile.close()
    template = "An exception of type {0} occurred. Arguments:\n{1!r}"
    message = template.format(type(ex).__name__, ex.args)
    print(message)
    print("EXITING..!!")
