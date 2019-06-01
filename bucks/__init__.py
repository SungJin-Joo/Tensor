from bucks.crawler import Bucks
import datetime

if __name__ == "__main__":
    dt = datetime.datetime(2019, 5, 31)

    url = 'https://music.bugs.co.kr/chart/track/day/total?chartdate=' + dt.strftime("%Y%m%d")
    bucks = Bucks(url)

