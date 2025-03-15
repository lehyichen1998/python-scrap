from bs4 import BeautifulSoup
import requests

url = 'https://maoyan.com/board/2'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    'Cookie': '__mta=150770953.1621258013213.1621426943663.1621426965317.11; uuid_n_v=v1; uuid=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; _lxsdk_cuid=1797a820414c8-018cb8505dda1a-2363163-144000-1797a820414c8; _lxsdk=80C7C710B71311EB9148110DC3B2994760FB01FEEE7341FEB455812A0FCD84F7; _csrf=a369fbea9473b26254da0f271013a4d02862bf75a2d3dc3c64ef53a3b16cfdfc; __mta=150770953.1621258013213.1621424753596.1621425334542.9; _lxsdk_s=17984705a91-d9c-db0-38b%7C%7C13'
}

response = requests.get(url, headers=headers)
# print(response.text)
soup = BeautifulSoup(response.text, 'html5lib')
titles = soup.find_all('p', 'name')
actors = soup.find_all('p', 'star')
for i in range(10):
    print(str(titles[i].string))
for i in range(10):
    print(str(actors[i].string))
