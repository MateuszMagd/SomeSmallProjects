import pandas as pd

# Reading csv data
data = pd.read_csv('data/csvdata.csv')
print(data)

# Most pricy product
biggest_price = data['Price'].max()
print(f'Biggest price in market: {biggest_price:.2f}')

# Getting all products that indexes are bigger then 2 and saving it to csv file
biggest_indexes = data[data['Index'] > 2]
biggest_indexes.to_csv('data/biggest_indexes.csv', index=False)

