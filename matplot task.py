import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import chardet
# 'Employee Sample Data - Copy.csv'
file_path='C:\\Users\\User\\Desktop\\Employee Sample Data - Copy.csv'
# df = pd.read_csv(file_path)
# print(df)
with open(file_path, 'rb') as f:
    result = chardet.detect(f.read())
    print(result) # Use the detected encoding
df = pd.read_csv(file_path, encoding=result['encoding'])
print("The original dataset")
print(df.head())
print(df.describe())
print(df.info())
print("Now i will clean the data ")
new_df=df.dropna()
print(new_df.to_string())
print(new_df.head())
#removing the duplicates
print("Removing duplicates")
dup=df.drop_duplicates(inplace=True)
print(dup)
#After cleaning
print("After cleaning")
print(df.head())
print(df.describe())
print(df.info())
new_inputs={
    'EEID':['E01234', 'E04321', 'E01798', 'E02222', 'E09988'],
    'Full Name': ['Saif Attieh', 'Ahmad Mustafa', 'Mohammad Ahmad', 'Ahmad Mohammad', 'Sara Ahmad'],
    'Job Title': ['Data Analys', 'Software Engineer', 'Accountant', 'Coordinator', 'Director'],
    'Department': ['HR', 'IT', 'Finance', 'Marketing', 'Sales'],
    'Business Unit': ['BU1', 'BU2', 'BU3', 'BU1', 'BU4'],
    'Gender': ['Male', 'Male', 'Male', 'Male', 'Female'],
    'Ethnicity': ['White', 'Asian', 'Black', 'Hispanic', 'White'],
    'Age': [35, 25, 42, 33, 45],
    'Hire Date': ['15-01-2020', '15-05-2018', '11-11-2015', '09-08-2017', '25-03-2014'],
    'Annual Salary': [12000, 6000, 15000, 10000, 160000],
    'Bonus %': [6.0, 2.5, 3.0, 1.5, 6.5],
    'Country': ['Jordan', 'Lebanon', 'Saudi Arabia', 'Egypt', 'Jordan'],
    'City': ['Amman', 'Beirut', 'Jeddah', 'Cario', 'Amman'],
    'Exit Date': ['10-5-2022', '19-9-2023', '31-12-2019', '16-6-2021', '25-5-2016'],
}
df_new=pd.DataFrame(new_inputs)
df.loc[:4]=df_new
print("--------Now i will display the first 5 modified rows--------")
print(df.head())
#Largest salary
temp_column = pd.to_numeric(df['Annual Salary'], errors='coerce')
max_salary_row = temp_column.max()
print("the largest salary:")
print(max_salary_row)
#knowing the number of employees by the job title
plt.figure(figsize=(10, 10))
job_counts = df['Job Title'].value_counts()
plt.bar(job_counts.index, job_counts.values, color='blue')
plt.title('Number of Employees by Job Title')
plt.xlabel('Job Title')
plt.ylabel('Number of Employees')
plt.xticks(rotation=75)
plt.grid(axis='y')
plt.tight_layout()
gender_counts = df['Gender'].value_counts()
#Number of male and female
plt.figure(figsize=(6, 5))
gender_counts.plot(kind='bar', color=['blue', 'pink'])
plt.title('Number of Male and Female Employees')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=0)
#Number of employees in each country
country_counts=df['Country'].value_counts()
plt.figure(figsize=(6,6))
plt.bar(country_counts.index, country_counts.values, color='green')
plt.title("Number of employees by country")
plt.xlabel("Country")
plt.ylabel("Number of employees")
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
#Relationship between Annual & Bonus %
df['Annual Salary'] = pd.to_numeric(df['Annual Salary'], errors='coerce')
df['Bonus %'] = pd.to_numeric(df['Bonus %'], errors='coerce')
plt.figure(figsize=(6,6))
plt.plot(df['Annual Salary'], df['Bonus %'], color='blue', alpha=0.6, marker='o', ms=10, mec='r', linestyle='-.')
plt.title('Relationship between Annual Salary and Bonus %', color='blue')
plt.xlabel('Annual Salary')
plt.ylabel('Bonus %')
plt.grid(True)
plt.tight_layout()
#Number of employees in each city
city_count=df['City'].value_counts()
plt.figure(figsize=(6,6))
plt.bar(city_count.index, city_count.values, color='purple', edgecolor='red')
plt.title('Number of Employees in each City', color='r')
plt.xlabel('City', color='purple')
plt.ylabel('Number of employees', color='purple')
plt.xticks(rotation=45)
plt.tight_layout()
# Age distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Age'], bins=10, edgecolor='black', color='skyblue')
plt.title('Age Distribution of Employees')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(axis='y')
plt.tight_layout()
# Calculate counts for each ethnicity
plt.figure(figsize=(8, 6))
ethnicity_counts = df['Ethnicity'].value_counts()
plt.bar(ethnicity_counts.index, ethnicity_counts.values, color='grey')
plt.title('Distribution of Ethnicity')
plt.xlabel('Ethnicity')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()



