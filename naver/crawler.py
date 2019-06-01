from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

class Naver:
    def __init__(self, url):
        #url = urlopen(url)
        con = requests.get(url)
        #print(con.content)

        soup = BeautifulSoup(con.content, 'html.parser')
#class="lst_pop"
        ul = soup.find("ul",{"class":"lst_pop"})
        infoPrint = []

        for li in ul.find_all("li"):
            infolist = []

            for b in li.find_all("td"):
                info = b.get_text().strip()
                infolist.append(info)

            if(len(infolist)):
                infoPrint.append(infolist)

        print(infoPrint)


