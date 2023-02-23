import pandas as pd

df = pd.read_csv('C:/Users/User/Desktop/учеба в GB/ПАКЕТ РАЗРАБОТЧИК-ПРОГРАММИСТ/знакомство с python/lesson_11/california_housing_train.csv')

# средняя стоимость дома, где количество жильцов 0 - 500.
med_h_v = df.groupby(df['population'] < 500.0)['median_house_value'].mean()
print(med_h_v[True])

# максимальная households в зоне минимального значения population
print(df.describe()['population'])
for i in range(4, 7):
  max_households_in_min_population = df.groupby(df['population'] < df.describe()['population'][i])['households'].max()[True]
  print(max_households_in_min_population)


