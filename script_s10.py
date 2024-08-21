import pandas as pd
import seaborn as sns
import plotly_express as px
from plotly import graph_objects as go

data = pd.read_csv('rest_data_us_upd.csv')
display(data)
data.info()
data_columns = data.columns.values
print(data[data['chain'].isna()])
print(data_columns)
#for i, columns in enumerate(data[data_columns]):
#    print(data[data[columns].duplicated()])


print(data[data.duplicated()])
### Sin duplicados
# Investiga las proporciones de los distintos tipos de establecimientos. Traza un gráfico.
type_data = data.groupby('object_type').agg({'object_name' : pd.Series.nunique}).reset_index()
print(type_data)
fig = go.Figure(data=[go.Pie(labels=type_data['object_type'], values= type_data['object_name'])])
fig.show()

#sns.barplot(data = data, x = 'object_type', y = 'object_name')
