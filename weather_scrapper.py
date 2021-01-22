from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup


def extract_now_temper():
    
    url = "https://weather.naver.com/today/09140104"
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    weather = soup.find("dl", {"class" : "summary_list"}).get_text().strip().split("\n")
    
    return weather
