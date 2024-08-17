import pandas as pd
import seaborn as sns
import plotly_express as px

data = pd.read_csv('rest_data_us_upd.csv')
display(data)
data.info()
data_columns = data.columns.values
print(data[data['chain'].isna()])
print(data_columns)
#for i, columns in enumerate(data[data_columns]):
#    print(data[data[columns].duplicated()])


print(data[data.duplicated()])