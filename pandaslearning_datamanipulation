import pandas
food_info=pandas.read_csv("food_info.csv")
col_names=food_info.columns.tolist()
print(col_names)
print(food_info.head(3))
div_1000 = food_info["Iron_(mg)"] / 1000
add_100 = food_info["Iron_(mg)"] + 100
sub_100 = food_info["Iron_(mg)"] - 100
mult_2 = food_info["Iron_(mg)"]*2

sodium_grams=food_info["Sodium_(mg)"]/1000
sugar_milligrams=food_info["Sugar_Tot_(g)"]*1000
water_energy = food_info["Water_(g)"] * food_info["Energ_Kcal"]
print(water_energy[0:5])
grams_of_protein_per_gram_of_water=food_info["Protein_(g)"]/food_info["Water_(g)"]
milligrams_of_calcium_and_iron=food_info["Calcium_(mg)"]+  food_info["Iron_(mg)"]
weighted_protein=food_info["Protein_(g)"]*2
weighted_fat=food_info["Lipid_Tot_(g)"]*(-0.75)
initial_rating=weighted_fat+weighted_protein
print(food_info["Protein_(g)"][0:5])
max_protein = food_info["Protein_(g)"].max()
x=food_info["Protein_(g)"].max()
y=food_info["Protein_(g)"].min()
normalized_protein=(food_info["Protein_(g)"]-y)/(x-y)
x=food_info["Lipid_Tot_(g)"].max()
y=food_info["Lipid_Tot_(g)"].min()
normalized_fat=(food_info["Lipid_Tot_(g)"]-y)/(x-y)
normalized_protein = (food_info["Protein_(g)"] - food_info["Protein_(g)"].min()) / (food_info["Protein_(g)"].max() - food_info["Protein_(g)"].min())
normalized_fat = (food_info["Lipid_Tot_(g)"] - food_info["Lipid_Tot_(g)"].min()) / (food_info["Lipid_Tot_(g)"].max() - food_info["Lipid_Tot_(g)"].min())

food_info["Normalized_Protein"]=normalized_protein
food_info["Normalized_Fat"]=normalized_fat
food_info["Normalized_Protein"] = normalized_protein
food_info["Normalized_Fat"] = normalized_fat
food_info["Norm_Nutr_Index"]=normalized_protein*2-0.75*normalized_fat
food_info["Norm_Nutr_Index"] = 2*food_info["Normalized_Protein"] + (-0.75*food_info["Normalized_Fat"])
food_info.sort_values("Norm_Nutr_Index",inplace=True,ascending=False)
