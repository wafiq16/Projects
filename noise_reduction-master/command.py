import pandas as pd
from sklearn import preprocessing

csvFile = pd.read_csv('drop your csv here')
result = preprocessing.normalize(csvFile, axis=0)
print(result)
