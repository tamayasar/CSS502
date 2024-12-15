import pandas as pd

prices = pd.read_csv("prices.csv").replace({'[.]': '', ' ': '', 'TL': ''},
                                           regex = True).astype(float).astype(int)

# Average rent in Uskudar.
print(prices.mean())
