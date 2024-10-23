import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset with a specific encoding
file_path = 'Gym.csv'  # Gym.csv can be replace with your CSV file path
df = pd.read_csv(file_path)  # allows the file to be read and used in python


# Displays the first 5 rows of the datafile
print("Initial Data:")
print(df.head(5)) 

# Identifies the different data types
print("\nData Types:")
print(df.dtypes) # displays all the data types

# Handles any missing data
print("\nMissing Values Before Handling:")
print(df.isnull().sum()) # counts all the missing data

# Remove duplicated data
print("\nNumber of Duplicates Before Removal:", df.duplicated().sum()) # checks and counts the duplicates before duplicate deletion
df.drop_duplicates(inplace=True) # Removes the duplicates
print("Number of Duplicates After Removal:", df.duplicated().sum()) # checks and counts the duplicates after duplicate deletions

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe()) # shows a box and whisker in table form regarding the Gym.csv

# Visualization
# Box and whiskers to compare the ages of men and women in the gym
column_x = 'Gender' #can use any text based category/column
column_y = 'Age' #can use any number based category/column
plt.figure(figsize=(10, 6))
sns.boxplot(x=df[column_x], y=df[column_y])  
plt.title('Ages comparision between genders in the gym')
plt.xlabel(column_x)
plt.ylabel(column_y)
plt.show()

# Bar graph to compare the calories burned at the gym between the genders
plt.figure(figsize=(10, 6))
column_x = 'Gender'  #can use any text based category/column
column_y = 'Calories_Burned' #can use any number based category/column
sns.barplot(data=df, x=df[column_x], y=df[column_y]) # Replace with your specific columns
plt.title('Gender-Based Analysis of Calories Burned')
plt.xlabel('Gender')
plt.ylabel('Calories Burned')
plt.show()
