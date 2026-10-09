import pandas as pd
df = pd.read_csv('students.csv')
print(df.head())
print(df.shape)
print(df[['name', 'GPA']])
print(df[df['GPA'] >= 3.5])
print(df.sort_values('GPA', ascending=False))
print(df.groupby('major')['GPA'].mean())