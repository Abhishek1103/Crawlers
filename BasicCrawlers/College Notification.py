'''
<div class="leftboldtxt"><img src="images/arrow_down.png" style="width:15px;height:15px;margin:0
2px 0 -20px;" class="ari"><font size="3px">
<strong>Revised Important Notice for DASA Students</strong></font><img src="images/new2.gif"></div>
'''


import requests
from bs4 import BeautifulSoup

def college_notification_spider():
    url = "https://academics.mnnit.ac.in/"
    sourceCode = requests.get(url)
    plainText = sourceCode.text
    #print(plainText)
    soup = BeautifulSoup(plainText)
    notificationList = []
    for link in soup.findAll('strong'):
        notification = link.string
        notificationList.append(notification)
    c = 0
    for link in soup.findAll('div', {'class': 'leftnormaltxt', 'style': 'font-size:13px;'}):
        notificationLink = link.findAll('a')
        c=c+1
        if notificationLink:
            print(c,":",notificationList[c-1])
            for i in notificationLink:
                final=str(i)
                print(url+final[9:final.find('>')-1])
        else:
            print(c, ":",notificationList[c-1])
            print("->",link.string)

college_notification_spider()
