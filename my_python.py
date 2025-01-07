import kaggle
import pandas as pd
import os                        # this the library that allows us to save to out desktop
from datetime import datetime
from plyer import notification


kaggle.api.authenticate()

# this is to download the file and that dot (.) means in download in this current directory
kaggle.api.dataset_download_files('denkuznetz/traffic-accident-prediction', path='.', unzip=True)

# Load the dataset into a DataFrame from this path (since the current folder for this project is
# where we download the csv file into this folder "C:/Users/jeffr/pythonProject16/ ")
df = pd.read_csv("C:/Users/jeffr/pythonProject16/dataset_traffic_accident_prediction1.csv")


# Define the path and filename
file_path = r"C:\Users\fabri\my_project_csv_files"

# This will create a CSV file named
file_name = f"dataset_traffic_accident_prediction1 {datetime.now().strftime('%d-%b-%Y_%H%M%S')}.csv"


full_path = os.path.join(file_path, file_name)


# Save the DataFrame to a CSV file without the index
df.to_csv(full_path, index=False)

print(f"Data saved to {full_path}")


# display notification to user (if the data has been saved and also the number of rows and columns
notification.notify(title="report status!",
                    message=f"dataset_traffic_accident_prediction1 has been successfully saved into excel.\
                                            Total rows: {df.shape[0]}   total columns: {df.shape[1]}", timeout=60)
