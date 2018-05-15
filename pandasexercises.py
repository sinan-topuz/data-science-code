import pandas as pd


names = pd.Series(['Sinan', 'Fadime', 'Unal', 'Ruhi', 'Seda', 'Ayfer'])
ages = pd.Series([39, 36, 38, 28, 33, 40])

df = pd.DataFrame({'Names': names, 'Ages': ages})

# print(df.describe())

print(df['Names'])

df["Elderly"] = df["Ages"].apply(lambda x: True if x > 35 else False)

print(df)




