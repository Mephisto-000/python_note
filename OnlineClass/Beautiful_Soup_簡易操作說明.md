# Beautiful Soup 簡易操作說明

參考自 : https://blog.gtwang.org/programming/python-beautiful-soup-module-scrape-web-pages-tutorial/



1. **安裝 Beautiful Soup**：
   - 使用 pip 安裝 Beautiful Soup 和 lxml 解析器的指令。
     ```python
     pip install beautifulsoup4
     pip install lxml
     ```

2. **導入必要的模組**：
   - 從 bs4 導入 BeautifulSoup，以及用於打開網頁的 urllib.request。
     ```python
     from bs4 import BeautifulSoup
     from urllib.request import urlopen
     ```

3. **打開網頁並讀取內容**：
   - 使用 urlopen 打開網址，並讀取內容到變數 html。
     ```python
     html = urlopen("http://example.com/").read().decode('utf-8')
     ```

4. **創建 BeautifulSoup 物件**：
   - 用讀取到的 HTML 內容創建一個 BeautifulSoup 物件，指定 lxml 作為解析器。
     ```python
     soup = BeautifulSoup(html, features="lxml")
     ```

5. **獲取網頁標題**：
   - 範例中展示了如何獲取網頁的標題。
     ```python
     print(soup.h1)
     ```

6. **查找所有的超連結**：
   - 使用 `soup.find_all('a')` 查找網頁中的所有 `<a>` 標籤（即超連結）。
     ```python
     all_href = soup.find_all('a')
     all_href = [l['href'] for l in all_href]
     print(all_href)
     ```

7. **使用 CSS 選擇器**：
   - 透過 `soup.select()` 使用 CSS 選擇器來選取特定元素。
     ```python
     print(soup.select('.sister'))
     ```

這些範例展示了如何使用 Beautiful Soup 進行基本的網頁抓取和解析操作，從安裝模組、讀取網頁內容、創建 BeautifulSoup 物件、到提取和處理特定資訊的過程。