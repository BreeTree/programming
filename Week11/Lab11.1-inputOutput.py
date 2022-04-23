# Program for messing with pandas
# Author: Breeda Herlihy

from pydoc import describe
import pandas as pd

list_data = [
    [5.1,3.5,1.4,0.2,'Iris-setosa'], 
    [4.9,3.0,1.4,0.2,'Iris-setosa'], 
    [4.7,3.2,1.3,0.2,'Iris-setosa'],
    [7.0,3.2,4.7,1.4,'Iris-versicolor'],
    [6.4,3.2,4.5,1.5,'Iris-versicolor'],
    [6.9,3.1,4.9,1.5,'Iris-versicolor'],
    [6.3,3.3,6.0,2.5,'Iris-virginica'],
    [5.8,2.7,5.1,1.9,'Iris-virginica'],
    [7.1,3.0,5.9,2.1,'Iris-virginica']
]
df = pd.DataFrame(list_data, columns=['sepal_length','sepal_width','petal_length','petal_width','class'])
print(df.head(5))
#https://stackoverflow.com/questions/33575587/pandas-dataframe-how-to-apply-describe-to-each-group-and-add-to-new-columns
#print (df.groupby('class').describe().unstack(1))

path = "./data/"
csvFilename = path + 'analysis.csv'
df.groupby('class').describe().unstack(1).to_csv(csvFilename)

path = "./data/"
csvFilename = path + 'iris.csv'
df.to_csv(csvFilename, index=False)

excelFilename = path +'iris.xlsx'
df.to_excel(excelFilename, index=False, sheet_name='data')

with pd.ExcelWriter(excelFilename, engine='openpyxl', mode='a') as writer:df.describe().to_excel(writer, sheet_name="summary")

mean = df.describe().loc['mean','sepal_length']
print(mean)
