import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('sales_data.csv')


print(df.head())


plt.figure(figsize=(8, 6))
plt.scatter(df['month_number'], df['toothpaste'], color='red', label='Toothpaste Sales')
plt.title('Toothpaste Sales Data for Each Month')
plt.xlabel('Month Number')
plt.ylabel('Toothpaste Sales')
plt.grid(True)
plt.legend()
plt.show()


plt.figure(figsize=(8, 6))
bar_width = 0.35
index = df['month_number']

plt.bar(index - bar_width/2, df['facecream'], bar_width, label='Facecream', color='blue')
plt.bar(index + bar_width/2, df['facewash'], bar_width, label='Facewash', color='green')

plt.title('Facecream and Facewash Sales Data')
plt.xlabel('Month Number')
plt.ylabel('Sales')
plt.xticks(index)
plt.legend()
plt.show()


total_sales = df[['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']].sum()

plt.figure(figsize=(8, 8))
plt.pie(total_sales, labels=total_sales.index, autopct='%1.1f%%', startangle=90, colors=['blue', 'green', 'red', 'purple', 'orange', 'yellow'])
plt.title('Total Sales for Each Product')
plt.axis('equal')  
plt.show()
