import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200309', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
# body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
# album = #body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.albumtitle.ellipsis
# rank = soup.select('tr:nth-child(1) > td.number')
# title = soup.select('td.info > a.title')
# singer = soup.select('td.info > a.artist')
# song ='[{}] / {} / {})'.format(rank,title,singer)

# print(rank)

chart = soup.select("tr.list")
rank = 0
for music in chart:
    rank += 1
    if rank >50:
        break
    title = music.select('a.title')[0].text.strip()
    artist = music.select('a.artist')[0].text.strip()
    album = music.select('a.albumtitle')[0].text.strip()
    song = '[{}] {} / {} / {}'.format(rank, title, artist, album)
    print(song)