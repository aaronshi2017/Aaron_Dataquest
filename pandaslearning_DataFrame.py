import pandas as pd
fandango=pd.read_csv("fandango_score_comparison.csv")
print(fandango.head(2))
print(fandango.index)
fandango = pd.read_csv('fandango_score_comparison.csv')
first_last=fandango.iloc[[0,len(fandango.index)-1]]
fandango = pd.read_csv('fandango_score_comparison.csv')
fandango_films=fandango.set_index("FILM",inplace=False,drop=False)
print(fandango_films.index)
print(fandango.iloc[5,4])
print(fandango.iloc[[5,4]])
best_movies_ever=fandango_films.loc[['The Lazarus Effect (2015)', 'Gett: The Trial of Viviane Amsalem (2015)', 'Mr. Holmes (2015)']]
import numpy as np

# returns the data types as a Series
types = fandango_films.dtypes
print(types)
# filter data types to just floats, index attributes returns just column names
float_columns = types[types.values == 'float64'].index
print("now print float column")
print(float_columns)
# use bracket notation to filter columns to just float columns
float_df = fandango_films[float_columns]

halved_dfh  = float_df.apply(lambda x: x/2)
print(halved_df.head(1))
rt_mt_user = float_df[['RT_user_norm', 'Metacritic_user_nom']]
rt_mt_deviations = rt_mt_user.apply(lambda x: np.std(x), axis=1)
print(rt_mt_deviations[0:5])

rt_mt_means=rt_mt_user.apply(lambda x: np.mean(x),axis=1)
print(rt_mt_means)
