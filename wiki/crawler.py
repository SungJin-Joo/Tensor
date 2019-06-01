from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

class Wiki:
    def __init__(self, url):
        #url = urlopen(url)
        con = requests.get(url)
        #print(con.content)

        soup = BeautifulSoup(con.content, 'html.parser')

        infoTable = soup.find("table",{"class":"wikitable sortable"})
        infoPrint = []

        for a in infoTable.find_all("tr"):
            infolist = []
            for b in a.find_all("td"):
                info = b.get_text().strip()
                infolist.append(info)

            if(len(infolist)):
                infoPrint.append(infolist)

        print(infoPrint)


