import sqlite3
import pandas as pd

if __name__ == '__main__':
    ###################################################################################################################
    ## 建立 SQLite 資料庫，並在 SQLite 資料庫中準備模擬資料

    # 建立 SQLite 資料庫連線
    conn = sqlite3.connect('test.db')

    # 建立一個名為 students 的資料表
    conn.execute('''CREATE TABLE IF NOT EXISTS students
                (ID INT PRIMARY KEY NOT NULL, 
                NAME TEXT NOT NULL, 
                AGE INT NOT NULL, 
                GRADE INT NOT NULL);''')

    # 插入資料
    conn.execute("INSERT or REPLACE INTO students (ID, NAME, AGE, GRADE) VALUES (1, 'John', 20, 85)")
    conn.execute("INSERT or REPLACE INTO students (ID, NAME, AGE, GRADE) VALUES (2, 'May', 21, 90)")
    conn.execute("INSERT or REPLACE INTO students (ID, NAME, AGE, GRADE) VALUES (3, 'Tom', 19, 78)")
    conn.execute("INSERT or REPLACE INTO students (ID, NAME, AGE, GRADE) VALUES (4, 'Lily', 22, 95)")

    # 提交更改
    conn.commit()

    # 關閉資料庫連線
    conn.close()
    ###################################################################################################################
    ## 利用 Pandas 操作 SQLite 資料庫

    # 建立 SQLite 資料庫連線
    conn = sqlite3.connect('test.db')

    # 讀取資料表資料
    df = pd.read_sql_query("SELECT * from students", conn)

    # 關閉資料庫連線
    conn.close()

    # 顯示 DataFrme
    print("\n")
    print(df)
    ###################################################################################################################
    ## 利用 Pandas 寫入資料庫

    conn = sqlite3.connect('test.db')

    # 將 DataFrame 的資料寫入資料庫
    df.to_sql('students_new', conn, if_exists='replace', index=False)

    conn.close()

