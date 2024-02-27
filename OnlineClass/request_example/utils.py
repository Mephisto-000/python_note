import os
import requests
from bs4 import BeautifulSoup


def read_headers_ua(headers_path: str) -> dict:
    """
    讀取 Headers 內的 "User-Agent"。

    :param headers_path: Headers 的路徑
    :type headers_path: str
    :return: User-Agent
    :rtype: str
    """
    with open(headers_path) as f:
        lines = f.readlines()
        headers_dict = {'User-Agent': lines[0].strip()}
        return headers_dict


def show_new_anime(url: str, ua: dict) -> None:
    r = requests.get(url, headers=ua)
    if r.status_code == 200:
        print(f'請求成功: {r.status_code}')

        soup = BeautifulSoup(r.text, 'html5lib')
        new_anime_item = soup.select_one('.timeline-ver > .newanime-block')
        anime_items = new_anime_item.select('.newanime-date-area:not(.premium-block)')

        for anime_item in anime_items:
            anime_name = anime_item.select_one('.anime-name > p').text.strip()
            print(f'Name: {anime_name}')
            anime_watch_number = anime_item.select_one('.anime-watch-number > p').text.strip()
            print(f'Watch number: {anime_watch_number}  人')
            anime_episode = anime_item.select_one('.anime-episode > p').text.strip()
            print(f'Episode: {anime_episode}')
            anime_href = anime_item.select_one('a.anime-card-block').get('href')
            print(f'Href: {os.path.join(url, anime_href)}')
            print('------------------------')
    else:
        print(f'請求失敗: {r.status_code}')


# test :
# if __name__ == '__main__':
#     url = 'https://ani.gamer.com.tw/'
#
#     headers = os.path.join(os.getcwd(), 'header_UA.txt')
#     user_agent = read_headers_ua(headers)
#
#     show_new_anime(url, ua=user_agent)

