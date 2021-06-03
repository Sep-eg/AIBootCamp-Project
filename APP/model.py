from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import joblib
import csv

regressor = RandomForestRegressor()

df = pd.read_csv('my_app/model/data.csv')
lable = df['사망자연령']
data = df.drop('사망자연령', axis=1)

regressor.fit(data, lable)

joblib.dump(regressor, 'model.pkl')