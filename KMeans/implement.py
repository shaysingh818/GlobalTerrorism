
"""

For each location, we can create three classes

High Lethality
Medium Lethality
Low Lethality

We'll use the Y axis as the amount of attacks
We'll use the X axis as the total property value in damage

# example code
data = {
    'x' : [10, 12, 13, 20, 40, 50],
    'y' :[10, 14, 56, 12, 14, 40]
}

df = pd.DataFrame(data, columns=['x', 'y'])
kmeans = KMeans(n_clusters=2).fit(df)
centroids = kmeans.cluster_centers_
print(centroids)

# get the two most lethal terrorist groups ever


plt.scatter(df['x'], df['y'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.show()

"""


import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from pprint import pprint
import matplotlib.pyplot as plt


# United States
df = pd.read_csv('../data.csv', encoding="latin-1")
#df = df.dropna(subset=['propvalue'])


def unique_filter(dataframe, column_value: str): 
    result_dict = {}
    for item in dataframe[column_value]:
        if item in result_dict:
            result_dict[item] += 1
        else:
            result_dict[item] = 1

    return result_dict

    
def prop_value_by_year(year):
    year_data = df[df['iyear'] == year]
    prop_val = year_data["propvalue"].sum()
    return prop_val

def harmed_monthly(year, month):
    yearly = df[df['iyear'] == year]
    monthly = yearly[yearly['imonth'] == month] 
    killed = monthly ["nkill"].sum()
    wounded = monthly["nwound"].sum()
    return killed + wounded

def prop_value_monthly(year, month):
    yearly = df[df['iyear'] == year]
    monthly = yearly[yearly['imonth'] == month] 
    prop_value = monthly['propvalue'].sum()
    #print("Property Damage {} : {} : {} ".format(year, month, prop_value))
    return prop_value

X = []  
y = []

for i in range(1970, 2017):
    for j in range(1, 13):
        results = prop_value_monthly(i, j)
        harmed = harmed_monthly(i, j)
        if results > 0:
            y.append(results)

        if harmed > 0:
            X.append(harmed)
        

X = X[1:300]
y = y[1:300]

data = {}
data['harmed'] = X
data['property_value'] = y


my_data = pd.DataFrame(data, columns=['harmed', 'property_value'])
kmeans = KMeans(n_clusters=3).fit(my_data)
centroids = kmeans.cluster_centers_
print(centroids)


plt.scatter(my_data['harmed'], my_data['property_value'], c=kmeans.labels_.astype(float), s=50, alpha=0.5)
plt.show()
