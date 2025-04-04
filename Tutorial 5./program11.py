import pandas as pd


df = pd.read_csv('student.csv')


df['CGPA'] = df['CGPA'].astype(float)


average_cgpa = df['CGPA'].mean()
print(f"Average CGPA of all students: {average_cgpa:.2f}")


high_cgpa_students = df[df['CGPA'] > 9]
print("\nStudents with CGPA > 9:")
print(high_cgpa_students)


cse_high_cgpa_students = df[(df['Branch'] == 'CSE') & (df['CGPA'] > 9)]
print("\nCSE Students with CGPA > 9:")
print(cse_high_cgpa_students)


max_cgpa_student = df.loc[df['CGPA'].idxmax()]
print("\nStudent with maximum CGPA:")
print(max_cgpa_student)


average_cgpa_by_branch = df.groupby('Branch')['CGPA'].mean()
print("\nAverage CGPA of each branch:")
print(average_cgpa_by_branch)