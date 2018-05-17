import pandas as pd
all_ages = pd.read_csv("all-ages.csv")
recent_grads = pd.read_csv("recent-grads.csv")
print(all_ages[0:5])
print(recent_grads[0:5])
print(all_ages['Major_category'].unique())

aa_cat_counts = dict()
rg_cat_counts = dict()
def calculate_major_cat_totals(df):
    cats = df['Major_category'].unique()
    counts_dictionary = dict()

    for c in cats:
        d=df[df["Major_category"]==c]
        total=d["Total"].sum()
        counts_dictionary[c]=total
    return counts_dictionary

low_wage_proportion=recent_grads["Low_wage_jobs"].sum()/recent_grads["Total"].sum()
print(low_wage_proportion)
majors = recent_grads['Major'].unique()
rg_lower_count = 0
for major in majors:
    c=all_ages[all_ages["Major"]== major]
    d=recent_grads[recent_grads["Major"]==major]
    if c.iloc[0]["Unemployment_rate"]>d.iloc[0]["Unemployment_rate"]:
        rg_lower_count+=1
print(rg_lower_count)
