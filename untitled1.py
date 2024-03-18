1) import pandas as pd
   data = pd.Series([1, 2, 3, 4], index=['a', 'b', 'a', 'c'])
   print(data)
   print(data['a'])

2) dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
   limited_keys = ['a', 'c', 'e']

   limited_series = pd.Series(dict_data, index=limited_keys)
   print(limited_series)

3) squares_series = pd.Series([i**2 for i in range(1, 21)])
   print(squares_series)
   filltered_series = squares_series[squares_series.index % 3 != 0]
   print(filtered_series)

4) students_df = pd.read_csv("students.csv")
   print(students_df.head(3))
   print(students_df.tall(2))
   students_df.info()
