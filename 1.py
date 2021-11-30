import qrcode
import requests
from bs4 import BeautifulSoup
data = "https://www.google.com/search?q=купить"
stuff = input()
stuff = stuff.split()
for i in stuff:
    data = data + "+" + i
HEADERS = {'user-agent' : 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36','accept' : '*/*'}
def get_html(data1):
    r = requests.get(data1, headers = HEADERS)
    return r
def get_content(html1):
    soup = BeautifulSoup(html1.text, 'html.parser')
    item = soup.find(id="vplaurlt0").get('href')
    global data
    data = item
def parse():
    html = get_html(data)
    get_content(html)
parse()
filename = "site.png"
img = qrcode.make(data)
img.save(filename)

