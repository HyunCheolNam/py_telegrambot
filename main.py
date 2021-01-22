import telepot
from weather_scrapper import extract_now_temper as temper
from rain_fall import rain_fall_scraaper as rain
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from datetime import datetime



token = "1566171747:AAErKOcC6qijYZO7sHyZauFgrYNq_88QlC8"
hc_bot = "1440238200"
bot = telepot.Bot(token)

#습도, 바람, 체감온도
weather = temper()
#강수확률 
rain_fall = rain()
#오늘 날짜 가져오기(오늘날짜 기사만 가져오기위해)


CHOSUN_URL = "http://it.chosun.com/svc/list_in/list.html?pn=1"

now_day = datetime.now()
today = now_day.strftime('%Y.%m.%d')
# print(today)

result = requests.get(CHOSUN_URL)
soup = BeautifulSoup(result.text, "html.parser")
pagination = soup.find("div", {"class" : "paginate"}).get_text().strip().split("\n")
page_result = pagination[1:-1]
max_page = page_result[-1]

#news title 가져오기
news_title = soup.find_all("span", {"class" : "tt"})
title = []
for i in news_title:
    title.append(i.text.strip())
# print(title)

#news date 가져오기
news_date = soup.find_all("span", {"class" : "date"})
date = []
for i in news_date:
    date.append(i.text)


news_link = soup.find_all("div",{"class" : "txt_wrap"})
link = []
for href in news_link:
    link.append(href.find("a")["href"])
print(len(link))


for i in range(0,20):
    bot.sendMessage(hc_bot,link[i] )
bot.sendMessage(hc_bot, weather[0]+":"+weather[1]+"\n"+weather[2]+":"+weather[3]+"\n"+weather[4]+":"+weather[5])
bot.sendMessage(hc_bot, "오전 : " + rain_fall[0] +"\n" + "오후 : " + rain_fall[1])

# 도전해봤지만 실패한 코드 
# pages = pagination.find_all('a')
# page_result = pages[2:-1]
# print(page_result)



