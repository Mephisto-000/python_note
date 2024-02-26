import os
import pandas as pd
import create_data

current_path = os.getcwd()
data_path_name = 'example_data'


if __name__ == "__main__":
    print("\n")

    # 範例資料路徑
    data_path = os.path.join(current_path, data_path_name)

    if os.path.exists(data_path + ".csv"):
        df = pd.read_csv(data_path + ".csv")

    elif os.path.exists(data_path + ".xlsx"):
        df = pd.read_excel(data_path + ".xlsx")
    else:
        df = create_data.example_df_data()
        print(f"output data : {create_data.output_csv_file(df, data_path, 'csv')}")

    print(f"Original Data : \n{df}")
    print("\n")

    # 列索引選取範例
    print(df[0:3])
    print("\n")

    # 利用索引名稱選取
    df.set_index('name', inplace=True)
    print(df['Alice':'Charlie'])
    print("\n")

    # 二維選取
    certain_choose = df.loc[['Alice', 'Charlie'], ['age', 'city']]
    print(certain_choose)
    print("\n")

    # 使用遮罩 (mask)
    mask1 = df['age'] > 30
    print(df[mask1])
    print("\n")

    # 多組合遮罩
    mask2 = (df['age'] > 30) & (df['city'] == 'Paris')
    print(df[mask2])
    print("\n")

    # 排序
    # 升序排序
    print(df.sort_values(by='age'))
    print("\n")

    # 降序排序
    print(df.sort_values(by='age', ascending=False))
    print("\n")

    # 按照索引排序
    print(df.sort_index())

