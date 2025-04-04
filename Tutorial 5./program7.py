import pandas as pd


df = pd.read_csv('employee.csv')


print("First 7 records:")
print(df.head(7))


print("\nEmployee names in alphabetical order:")
sorted_names = df['name'].sort_values()
print(sorted_names)


highest_salary_employee = df.loc[df['salary'].idxmax()]
print("\nEmployee with the highest salary:")
print(highest_salary_employee['name'])


male_employees = df[df['gender'] == 'Male']['name']
print("\nMale employees:")
print(male_employees)


teams = df['team'].unique()
print("\nTeams employees belong to:")
print(teams)
