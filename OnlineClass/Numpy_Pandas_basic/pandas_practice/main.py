import os
import create_data

current_path = os.getcwd()
data_path_name = 'example_data'


if __name__ == "__main__":

    data_path = os.path.join(current_path, data_path_name)

    df = create_data.example_df_data()
    print(f"output data : {create_data.output_csv_file(df, data_path, 'csv')}")
