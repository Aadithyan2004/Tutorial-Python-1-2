
import pandas as pd


df = pd.read_csv('stud.csv')


print("File contents:")
print(df)


df.set_index('rollno', inplace=True)
print("\nData with rollno set as index:")
print(df)


print("\nName and mark of students:")
print(df[['name', 'mark']])


df_sorted_by_name = df[['name', 'mark']].sort_values(by='name')
print("\nData sorted by name:")
print(df_sorted_by_name)


df_sorted_by_mark_desc = df[['name', 'mark']].sort_values(by='mark', ascending=False)
print("\nData sorted by mark (descending order):")
print(df_sorted_by_mark_desc)


average_mark = df['mark'].mean()
median_mark = df['mark'].median()
mode_mark = df['mark'].mode()[0]  

print(f"\nAverage mark: {average_mark}")
print(f"Median mark: {median_mark}")
print(f"Mode mark: {mode_mark}")

min_mark = df['mark'].min()
max_mark = df['mark'].max()
print(f"\nMinimum mark: {min_mark}")
print(f"Maximum mark: {max_mark}")


variance_mark = df['mark'].var()
std_dev_mark = df['mark'].std()
print(f"\nVariance of marks: {variance_mark}")
print(f"Standard deviation of marks: {std_dev_mark}")


import matplotlib.pyplot as plt

plt.hist(df['mark'], bins=5, edgecolor='black')
plt.title('Histogram of Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()


df.drop('place', axis=1, inplace=True)
print("\nData after removing the 'place' column:")
print(df)
