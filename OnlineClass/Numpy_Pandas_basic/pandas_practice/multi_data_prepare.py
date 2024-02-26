import pandas as pd


data1 = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
         'age': [25, 32, 18, 47],
         'city': ['New York', 'Paris', 'London', 'Berlin']}


data2 = {'name': ['Eva', 'Frank', 'Grace', 'Henry'],
         'age': [29, 23, 37, 31],
         'city': ['Rome', 'Sydney', 'Tokyo', 'Moscow']}


if __name__ == "__main__":
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)

    print(f"Original Data : \n\n df1:\n{df1} \n\n df2:\n{df2}")
    print("\n")

    # 列軸合併
    print(pd.concat([df1, df2], axis=0))
    print("\n")

    # 行軸合併
    print(pd.concat([df1, df2], axis=1))
