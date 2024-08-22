import pandas as pd
import seaborn as sns
import plotly_express as px
from plotly import graph_objects as go
from numpy import median

data = pd.read_csv('rest_data_us_upd.csv')
display(data)
data.info()
data_columns = data.columns.values
print(data[data['chain'].isna()])
print(data_columns)
#for i, columns in enumerate(data[data_columns]):
#    print(data[data[columns].duplicated()])


print(data[data.duplicated()])
print(data[data[['object_name','address']].duplicated()])

print(data[data['object_name'] == 'BLD'])
### Sin duplicados
# Investiga las proporciones de los distintos tipos de establecimientos. Traza un gráfico.
type_data = data.groupby('object_type').agg({'object_name' : pd.Series.nunique}).reset_index()
print(type_data)
fig = go.Figure(data=[go.Pie(labels=type_data['object_type'], values= type_data['object_name'])])
fig.show()
# Investiga las proporciones de los establecimientos que pertenecen a una cadena y de los que no. Traza un gráfico.
chain_data = data[data['chain'] == True].groupby('object_type').agg({'object_name' : pd.Series.nunique}).reset_index()
chain_data.columns = ['object_type', 'chain']
chain_data['no_chain'] = type_data['object_name'] - chain_data['chain']
print(chain_data)
fig = go.Figure(data=[go.Pie(labels=chain_data['object_type'], values= chain_data['chain'])])
fig1 = go.Figure(data=[go.Pie(labels=chain_data['object_type'], values= chain_data['no_chain'])])
fig.show()
fig1.show()
### Estlablecimientos en cadenas


#¿Qué tipo de establecimiento es habitualmente una cadena?
chain = data.groupby(['object_type', 'chain']).agg({'object_name' : pd.Series.nunique}).reset_index()
print(chain)

#sns.barplot(data = chain, x = 'object_type', y = 'object_name', hue='chain')
# Las Bakery son cadenas

# ¿Qué caracteriza a las cadenas: muchos establecimientos con un pequeño número de asientos o unos pocos establecimientos con un montón de asientos?
seats = data.groupby(['object_type', 'chain']).agg({'number' : 'sum', 'object_name' : 'nunique'}).reset_index()
seats.columns = ['object_type', 'chain', 'seats', 'commerce']

#sns.barplot(seats, x = 'object_type', y = 'seats', hue='chain')
# Determina el promedio de número de asientos para cada tipo de restaurante.
seats['seats_per_commerce'] = (seats['seats'] / seats['commerce']).round(0)
print(seats)

#sns.barplot(seats, x = 'object_type', y = 'seats_per_commerce', hue='chain')

#Coloca los datos de los nombres de las calles de la columna address en una columna separada.
address = data['address'].reset_index()
# Traza un gráfico de las diez mejores calles por número de restaurantes.
address_top = address.groupby('address').count().reset_index().sort_values('index', ascending= False).iloc[0:10]
address_top.columns = ['address', 'restaurant']
print(address_top)

#sns.barplot(data = address_top, y = 'address', x = 'restaurant', orient= 'y')

#Encuentra el número de calles que solo tienen un restaurante.
restaurat_by_address = address.groupby('address').count().reset_index()
print('Existen ' + str(restaurat_by_address[restaurat_by_address['index'] == 1]['address'].count()) + ' calles con un solo restaurante.')

# Para las calles con muchos restaurantes, analiza la distribución del número de asientos. ¿Qué tendencias puedes ver?
seats_by_address = data[~data['address'].isin(restaurat_by_address[restaurat_by_address['index'] == 1]['address'])][['address', 'number']].sort_values('number').reset_index(drop= True)
print(seats_by_address)
sns.boxplot(seats_by_address, x = 'number')

sns.histplot(seats_by_address, x = 'number')
