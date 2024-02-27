import requests
from bs4 import BeautifulSoup



headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}







# test :
if __name__ == '__main__':
    url = 'https://ani.gamer.com.tw/'
    r = requests.get(url, headers=headers)

    if r.status_code == 200:
        print(f'請求成功: {r.status_code}')
    else:
        print(f'請求失敗: {r.status_code}')
