import pandas as pd

#load the dataset
df = pd.read_csv("Sample Dataset.csv")

print(df.head()) # display the first few rows of the dataframe
print(df.shape) # display the shape of the dataframe
print(df.info()) # display the summary information of the dataframe
print(df['Price'].describe()) # display the statistical summary of the 'Price' column
print(df.isnull().sum()) # display the count of missing values in each column  

# Select only the columns we want
features = ['Brand', 'Year', 'Model', 'Car/Suv', 'UsedOrNew', 
            'Transmission', 'Engine', 'DriveType', 'FuelType', 
            'FuelConsumption', 'Kilometres', 'Location', 'CylindersinEngine']

target = 'Price'

df_model = df[features + [target]].copy()# Create a smaller dataframe with just these columns
print(df_model.head())
print(df_model.isnull().sum())


