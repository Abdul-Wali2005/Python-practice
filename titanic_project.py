import pandas as pd 

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)
df.to_csv("titanic.csv", index=False)
print(df.shape)
print(df.columns.tolist())
print (df.isna().sum())
print (df['Survived'].sum())
print (df['Survived'].value_counts())
print (df ['Survived']. mean())
rate = df.groupby('Pclass')['Survived'].mean()
print(rate)

import matplotlib.pyplot as plt

plt.bar(rate.index, rate.values)
plt.title("Survival Rate by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Survival Rate")
plt.savefig("survival_by_pclass.png")
plt.show()