import pandas as pd
titanic_survival=pd.read_csv("titanic_survival.csv")
age = titanic_survival["age"]
print(age.loc[10:20])
age_null_true=age[pandas.isnull(age)]
age_null_count=len(age_null_true)
print(age_null_count)
age_is_null = pd.isnull(titanic_survival["age"])
age_isnot_null=[]
for x in age_is_null:
    d=not(x)
    age_isnot_null.append(d)
t=titanic_survival["age"]
x=t[age_isnot_null]
correct_mean_age0=sum(x)/len(x)
print(correct_mean_age0)

good_ages = titanic_survival["age"][age_is_null == False]
correct_mean_age1 = sum(good_ages) / len(good_ages)
print(correct_mean_age1)

good_ages = titanic_survival["age"][~(age_is_null)]
correct_mean_age2 = sum(good_ages) / len(good_ages)
correct_mean_age = titanic_survival["age"].mean()
correct_mean_fare=titanic_survival["fare"].mean()
passenger_classes = [1, 2, 3]
fares_by_class = {}
for x in passenger_classes:
    t=titanic_survival["fare"][titanic_survival["pclass"]==x]
    fares_by_class[x]=t.mean()
print(fares_by_class)
import numpy as np
passenger_survival = titanic_survival.pivot_table(index="pclass", values="survived")
passenger_age=titanic_survival.pivot_table(index="pclass",values="age",aggfunc=np.mean)
print(passenger_age)
2
port_stats=titanic_survival.pivot_table(index="embarked",values=["fare","survived"],aggfunc=np.sum)
3
print(port_stats)

drop_na_rows = titanic_survival.dropna(axis=0)
drop_na_columns=titanic_survival.dropna(axis=1)
new_titanic_survival=titanic_survival.dropna(axis=0,subset=["age","sex"])
first_five_rows = new_titanic_survival.iloc[0:5]
first_ten_rows=new_titanic_survival.iloc[0:10]
row_position_fifth=new_titanic_survival.iloc[4]
row_index_25=new_titanic_survival.loc[25]
first_row_first_column = new_titanic_survival.iloc[0,0]
all_rows_first_three_columns = new_titanic_survival.iloc[:,0:3]
row_index_83_age = new_titanic_survival.loc[83,"age"]
row_index_766_pclass = new_titanic_survival.loc[766,"pclass"]
row_index_1100_age=new_titanic_survival.loc[1100,"age"]
row_index_25_survived=new_titanic_survival.loc[25,"survived"]
five_rows_three_cols=new_titanic_survival.iloc[0:5,0:3]
titanic_reindexed=new_titanic_survival.reset_index(drop=True)
print(titanic_reindexed.iloc[0:5,0:3])
def hundredth_row(column):
    hundredth_item = column.iloc[99]
    return hundredth_item

hundredth_row_var = titanic_survival.apply(hundredth_row)
def num_of_nulls(column):
    return len(column[column.isnull()])
column_null_count=titanic_survival.apply(num_of_nulls)
import pandas as pd

def xxx(row):
    age = row["age"]
    if pd.isnull(age):
        return "unknown"
    elif age > 18:
        return "adult"
    else:
        return "minor"

age_labels = titanic_survival.apply(xxx, axis=1)

age_group_survival=titanic_survival.pivot_table(index="age_labels",values="survived",aggfunc=np.mean)
