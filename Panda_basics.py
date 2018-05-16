import pandas

food_info=pandas.read_csv("food_info.csv")

print(type(food_info))

print(food_info.head(3))
dimensions = food_info.shape
print(dimensions)
num_rows = dimensions[0]
print(num_rows)
num_cols = dimensions[1]
print(num_cols)
first_twenty=food_info.head(20)
print(first_twenty)

hundredth_row=food_info.loc[99]
print(hundredth_row)
print(food_info.dtypes)
print("Rows 3, 4, 5 and 6")
print(food_info.loc[3:6])
print(food_info.shape)
print("Rows 2, 5, and 10")
two_five_ten = [2,5,10]
print(food_info.loc[two_five_ten])
last_rows=food_info.iloc[-5:]
print(last_rows)
# Series object.
ndb_col = food_info["NDB_No"]
print(ndb_col)

# Display the type of the column to confirm it's a Series object.
print(type(ndb_col))

saturated_fat=food_info["FA_Sat_(g)"]
cholesterol=food_info["Cholestrl_(mg)"]
zinc_copper = food_info[["Zinc_(mg)", "Copper_(mg)"]]

columns = ["Zinc_(mg)", "Copper_(mg)"]
zinc_copper = food_info[columns]
selenium_thiamin=food_info[["Selenium_(mcg)","Thiamin_(mg)"]]
print(selenium_thiamin)
print(food_info.columns)
print(food_info.head(2))
x=food_info.columns.tolist()
gram_columns=[]
for y in x:
    if y.endswith("(g)"):
        gram_columns.append(y)
print(gram_columns)
gram_df=food_info[gram_columns]
gram_df.head(3)
