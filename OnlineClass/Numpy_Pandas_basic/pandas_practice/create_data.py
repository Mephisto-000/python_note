import pandas as pd


def example_series_data():
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


def output_csv_file(data, path, file_type="csv") -> bool:
    """
    輸出 .csv 檔案

    :param data: 欲儲存的資料。
    :type data: DataFrame or Series
    :param path: 欲儲存的路徑。
    :type path: str
    :param file_type: 欲儲存的資料類型。
    :type file_type: str
    :return: True 資料匯出成功， False 資料匯出失敗
    :rtype: bool
    """

    if file_type == "csv":
        data.to_csv(path + '.csv')
        return True
    elif file_type == "xlsx":
        data.to_excel(path + '.xlsx')
        return True
    else:
        return False

