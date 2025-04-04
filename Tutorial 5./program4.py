import pandas as pd


df = pd.read_csv('auto.csv')


df = df.dropna()  
df = df.drop_duplicates()  
df['price'] = pd.to_numeric(df['price'], errors='coerce') 
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')  
df['average-mileage'] = pd.to_numeric(df['average-mileage'], errors='coerce') 

df.to_csv('auto_cleaned.csv', index=False)


print("Cleaned data saved to 'auto_cleaned.csv'")


most_expensive_car = df.loc[df['price'].idxmax()]
most_expensive_company = most_expensive_car['company']
print(f"The most expensive car company is: {most_expensive_company}")


toyota_cars = df[df['company'] == 'toyota']
print(toyota_cars)


company_counts = df['company'].value_counts()
print(company_counts)


highest_priced_car = df.loc[df['price'].idxmax()]
print(f"The highest priced car is:\n{highest_priced_car}")


average_mileage_by_company = df.groupby('company')['average-mileage'].mean()
print(average_mileage_by_company)


sorted_by_price = df.sort_values(by='price', ascending=False)
print(sorted_by_price)
