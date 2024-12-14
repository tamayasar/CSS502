import pandas as pd
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

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
missing_mask = merged.isna().any(axis=1)
# print(merged[missing_mask].to_string())

# print(cleared.head(5))
# print(cleared.tail(5))

# print(len(cleared.country.unique()))

year_2000 = cleared[cleared.year == "2000"]
# print(year_2000.to_string())

africa = pd.read_csv("africa.csv").country.values.tolist()
africa_data = cleared[cleared.country.isin(africa)]
# print(africa_data)

# Expand abbreviations.
cleared.population = cleared.population.replace({'B': 'e+09', 'M': 'e+06', 'k': 'e+03'},
                                                regex = True).astype(float).astype(int)
less_than_m = cleared[cleared.population < 1000000]
# print(less_than_m)

life_ascending = cleared.sort_values(by = "life expectancy")
# print(life_ascending)

cleared["pop_category"] = pd.cut(cleared['population'], bins=[2260, 566668173, 1133334086,
                                                           1700000000],
                              include_lowest=True, labels=['Low', 'Medium', 'High'])

europe = pd.read_csv("europe.csv").country.values.tolist()
europe_data = cleared[cleared.country.isin(europe)]

asia = pd.read_csv("asia.csv").country.values.tolist()
asia_data = cleared[cleared.country.isin(asia)]

# Calculate the average GDP per capita for each continent.
africa_gdp_avg = africa_data["gdp per capita"].replace({'B': 'e+09', 'M': 'e+06', 'k':
                                                        'e+03'}, regex =
                                                       True).astype(float).astype(int).mean()
europe_gdp_avg = europe_data["gdp per capita"].replace({'B': 'e+09', 'M': 'e+06', 'k':
                                                        'e+03'}, regex =
                                                       True).astype(float).astype(int).mean()
asia_gdp_avg = asia_data["gdp per capita"].replace({'B': 'e+09', 'M': 'e+06', 'k':
                                                    'e+03'}, regex =
                                                   True).astype(float).astype(int).mean()

# print(africa_gdp_avg)
# print(europe_gdp_avg)
# print(asia_gdp_avg)

# Identify the country with the highest life expectancy in a given year.
# print(year_2000.sort_values(by = "life expectancy").tail(1).country)

# Use basic plotting functions in Pandas (e.g., plot, bar) to visualize the trends in life
# expectancy over the years for a selected country.
turkey = cleared[cleared.country == "Turkey"]
turkey.plot(x = "year", y = "life expectancy")
plt.show()
