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
            print(f'Name: {anime_name}')  # 動畫名字
            anime_watch_number = anime_item.select_one('.anime-watch-number > p').text.strip()
            print(f'Watch number: {anime_watch_number}  人')  # 觀看人數
            anime_episode = anime_item.select_one('.anime-episode > p').text.strip()
            print(f'Episode: {anime_episode}')  # 集數
            anime_href = anime_item.select_one('a.anime-card-block').get('href')
            print(f'url: {os.path.join(url, anime_href)}')  # 影片網址
            anime_img_url = anime_item.select_one('img.lazyload').get('data-src')
            print(f'img url: {anime_img_url}')  # 動畫縮圖網址
            anime_date = str(anime_item.select_one('.anime-date-info').contents[-1]).strip()
            print(f'Date: {anime_date}')  # 動畫播放日期
            anime_time = anime_item.select_one('.anime-hours').text.strip()
            print(anime_time)  # 動畫播放時間
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

