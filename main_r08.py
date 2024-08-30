import pandas as pd

# specify the path to the CSV file
file_path = r"C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0084__Day80_Handwashing_tTests_and_Distributions__240829\NewProject\r00_env_START\monthly_deaths.csv"

# load the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# extract the month from the 'date' column
df['month'] = df['date'].dt.month

# approach 1: direct mean of the 'births' column (overall average per month)
overall_monthly_mean = df['births'].mean()

# approach 2: group by the extracted month and calculate the mean for each month
monthly_means = df.groupby('month')['births'].mean()

# approach 2: calculate the overall average of these monthly means
average_of_monthly_means = monthly_means.mean()

# print the results
print("Overall average number of births per month:", overall_monthly_mean)
print("Average number of births per month across all months:")
print(monthly_means)
print("Average of the monthly means:", average_of_monthly_means)
