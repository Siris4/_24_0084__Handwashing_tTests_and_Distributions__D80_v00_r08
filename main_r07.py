import pandas as pd

# specify the path to the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"

# load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# check for NaN values in the DataFrame
nan_exists = "Yes" if df.isnull().any().any() else "No"

# check for duplicates in the DataFrame
duplicates_exist = "Yes" if df.duplicated().any() else "No"

# print the results
print("Are there any NaN values in the DataFrame?", nan_exists)
print("Are there any duplicate rows in the DataFrame?", duplicates_exist)
