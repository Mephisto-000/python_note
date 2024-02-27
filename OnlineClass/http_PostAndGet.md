# http Post 與 Get

參考自 : https://totoroliu.medium.com/http-post-%E5%92%8C-get-%E5%B7%AE%E7%95%B0-928829d29914

## 1. http

- HTTP是客戶端與伺服器端進行請求和應答交流的標準協議。
- 在HTTP/1.1協定中，定義了八種方法（動作），包括：GET、HEAD、POST、PUT、DELETE、TRACE、OPTIONS、CONNECT，用於以不同方式操作資源。
- 每種方法原本有其特定用途，例如**GET用於發出顯示特定資源的請求**，**POST用於向指定資源提交資料請求伺服器進行處理**，可能包括建立新資源、修改現有資源或兩者都有。
- 然而，在實際開發中，這些方法的原始定義可能會因為各種原因而被混用或失去，例如GET方法有時也能實現POST的功能，而且還可以避免使用表單。



## 2. Get Method

**向指定的資源要求資料，類似於查詢操作。**

- 資料傳遞方式 — 將參數以 Query String方式(name/value)，由URL帶至Server端，EX: /test/demo_get**?name1=value1&name2=value2**。
- 參數長度限制 — 長度限制根據瀏覽器、Server 的不同會有所不同。
- 安全性 — 較POST不安全，因為傳遞的參數會在URL上顯示。
- 資料種類 — 只允許 ASCII。
- **可以**重新載入或按上一頁並不會有任何問題。
- 傳遞的參數**會**被儲存在瀏覽器的歷史紀錄中。
- **可以**加入瀏覽器書籤。



## 3. Post Method

**將要處理的資料提交給指定的資源，類似於更新操作。**

- 資料傳遞方式 — 將參數放至 Request 的 message body 中，因此不會在URL看到參數，適合用於隱密性較高的資料，EX: Signup、Signin帳號、密碼等。
- 參數長度限制 — 長度不受限制。
- 安全性 — 較POST安全，實際上傳遞的參數皆可以在封包(Request- line 和 Message-body)上看到。
- 資料種類 — 無限制。
- 重新載入或按上一頁瀏覽器會出現將重新提交(re-submitted)資料的提示。
- 傳遞的參數**不會**被儲存在瀏覽器的歷史紀錄中。
- **無法**加入瀏覽器書籤。



