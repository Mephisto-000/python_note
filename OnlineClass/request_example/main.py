"""
練習：

參考自 https://blog.jiatool.com/posts/gamer_ani_spider/
哈姆特 動畫瘋：新手入門基礎網路爬蟲教學。

爬取"巴哈姆特 動畫瘋"的本季新番動畫資訊

Hint : 先安裝 html5lib 解析器

"""
import os
import utils

url = 'https://ani.gamer.com.tw/'  # "巴哈姆特 動漫瘋" 網址

if __name__ == '__main__':

    headers = os.path.join(os.getcwd(), 'header_UA.txt')
    user_agent = utils.read_headers_ua(headers)

    utils.show_new_anime(url, ua=user_agent)
