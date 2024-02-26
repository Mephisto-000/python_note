import pandas as pd


def example_seri_data():
    """
    創建一個 Series 物件。

    :return:
        Series 物件
    """
    data = [1, 3, 5, 7, 9]

    s = pd.Series(data)

    return s


def example_df_data():
    """
    創建一個 DataFrame 物件。

    :return:
        DataFrame 物件
    """
    data = {'name': ['Alice', 'Bob', 'Charlie', 'David'],
            'age': [25, 32, 18, 47],
            'city': ['New York', 'Paris', 'London', 'Berlin']}

    df = pd.DataFrame(data)

    return df




