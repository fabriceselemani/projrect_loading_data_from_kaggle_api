import kaggle
import pandas as pd
import os
from datetime import datetime
from plyer import notification



kaggle.api.authenticate()


try:
    def download_dataset():  # download the dataset

        # Download the file to the current directory.
        kaggle.api.dataset_download_files('denkuznetz/traffic-accident-prediction', path='.', unzip=True)


    def process_data():  # clean the dataset.

        # Read the downloaded CSV file into a DataFrame.
        df = pd.read_csv("C:/Users/jeffr/pythonProject16/dataset_traffic_accident_prediction1.csv")

        # Drop all duplicate records and remove rows with null values.
        df = df.drop_duplicates().dropna()

        # Create a temporary column to filter the dataset and reduce its size, as this is a demo project.
        df["ID"] = range(1, len(df) + 1)
        df = df[[str(i) for i in df.columns.to_list()]]

        # create a filter to reduce the size of the dataset
        filtered_df = df["ID"] < 60
        df = df.loc[filtered_df]

        # Dropping the temporary column created for filtering to reduce the size of the dataset.
        df = df.drop(columns=["ID"])

        return df


    def send_to_home_dir(df):  # save the dataset to the home directory
        # Define the path and filename
        file_path = r"C:\Users\fabri\my_project_csv_files"

        # create a CSV file named
        file_name = f"dataset_traffic_accident_prediction1 {datetime.now().strftime('%d-%b-%Y_%H%M%S')}.csv"

        full_path = os.path.join(file_path, file_name)

        # Save the DataFrame to a CSV file without the index
        df.to_csv(full_path, index=False)

        print(f"Data saved to {full_path}")

        # display notification (if the data has been saved and also the number of rows and columns)
        notification.notify(title="report status!",
                            message=f"dataset_traffic_accident_prediction1 has been successfully saved into excel.\
                                                        Total rows: {df.shape[0]}   total columns: {df.shape[1]}",
                            timeout=60)


    def main():
        download_dataset()
        processed_data = process_data()
        send_to_home_dir(processed_data)


    if __name__ == "__main__":
        main()


except Exception as e:
    if e != 200:
        print("Something went wrong!; the dataset was not downloaded.")
