import pandas as pd

#load the dataset
df = pd.read_csv("Sample Dataset.csv")

print(df.head()) # display the first few rows of the dataframe
print(df.shape) # display the shape of the dataframe
print(df.info()) # display the summary information of the dataframe
print(df['Price'].describe()) # display the statistical summary of the 'Price' column
print(df.isnull().sum()) # display the count of missing values in each column  

