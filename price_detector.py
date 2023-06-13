import pandas
from sklearn.linear_model import LinearRegression


data = pandas.read_csv('iphone_price.csv')
# print(data.head())

model = LinearRegression()
model.fit(data[['version']],data[['price']])

# model.pridect([[14]])
