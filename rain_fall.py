from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup



def rain_fall_scraaper():

    url = "https://weather.naver.com/today/09140104"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    
    rain_fall = soup.find_all("strong",{"class" : "rainfall"})
    rain_fall_am = rain_fall[0].get_text()
    rain_fall_pm = rain_fall[1].get_text()
    
    rain = rain_fall_am, rain_fall_pm


    return rain


