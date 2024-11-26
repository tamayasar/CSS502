import pandas as pd

gdp = pd.read_csv("gdp-pcap.csv")
life = pd.read_csv("life-expectancy.csv")
population = pd.read_csv("population.csv")

# print(gdp)

gdp_long = pd.melt(gdp, id_vars=["country"], var_name="year", value_name="gdp per capita")
life_long = pd.melt(life, id_vars=["country"], var_name="year", value_name="life expectancy")
population_long = pd.melt(population, id_vars=["country"], var_name="year", value_name="population")

# print(gdp_long.to_string())
# print(life_long)
# print(population_long.to_string())

gdp_life = pd.merge(left = gdp_long, right = life_long, on = ["country", "year"])
merged = pd.merge(left = gdp_life, right = population_long, on = ["country", "year"])

# print(merged.to_string())

cleared = merged.dropna()

# We can also see what we removed.
# missing_mask = merged.isna().any(axis=1)
# print(merged[missing_mask].to_string())

# print(cleared.head(5))
# print(cleared.tail(5))

# print(len(cleared.country.unique()))

year_2000 = cleared[cleared.year == "2000"]
print(year_2000.to_string())
