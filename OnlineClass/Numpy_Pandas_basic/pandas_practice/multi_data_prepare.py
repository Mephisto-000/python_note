import pandas as pd


data1 = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
         'age': [25, 32, 18, 47],
         'city': ['New York', 'Paris', 'London', 'Berlin']}


data2 = {'name': ['Eva', 'Frank', 'Grace', 'Henry'],
         'age': [29, 23, 37, 31],
         'city': ['Rome', 'Sydney', 'Tokyo', 'Moscow']}

data3 = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
         'salary': [5000, 6000, 7000, 8000]}

data4 = {'salary': [5000, 6000, 7000, 8000]}

group_data = {'name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank'],
              'age': [25, 32, 18, 47, 23, 31],
              'gender': ['female', 'male', 'female', 'male', 'female', 'male'],
              'city': ['New York', 'Paris', 'London', 'Berlin', 'New York', 'Paris'],
              'salary': [50000, 80000, 25000, 100000, 35000, 75000]}


if __name__ == "__main__":
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    df3 = pd.DataFrame(data3)
    df4 = pd.DataFrame(data4,
                       index=['Alice', 'Bob', 'Charlie', 'David'])
    df_gp = pd.DataFrame(group_data)

    print(f"Original Data : \n\n df1:\n{df1} \n\n df2:\n{df2}")
    print("\n")

    # 使用 concat()
    # 列軸合併
    print(pd.concat([df1, df2], axis=0))
    print("\n")

    # 行軸合併
    print(pd.concat([df1, df2], axis=1))
    print("\n")

    # 使用 merge()
    # 根據 name 欄位合併
    print(pd.merge(df1, df3, on='name'))
    print("\n")

    # 使用 join()
    # 按照索引合併
    df1.set_index('name', inplace=True)
    print(df1.join(df4))
    print("\n")

    # 使用 groupby()
    print(f"Original Data : \n {df_gp}")
    print("\n")

    # 按照 "city" 列的值進行分組，並對每個城市的人口數、平均年齡、平均薪資做統計
    grouped = df_gp.groupby('city')
    gp_result = grouped.agg({'name': 'count',
                             'age': 'mean',
                             'salary': 'mean'})
    print(gp_result)
    print("\n")

    # 按照城市和性別進行分組
    grouped2 = df_gp.groupby(['city', 'gender'])
    gp_result2 = grouped2.agg({'name': 'count',
                               'age': 'mean',
                               'salary': 'mean'})
    print(gp_result2)
    print("\n")
