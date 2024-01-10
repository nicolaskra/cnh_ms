

# Importando PANDAS para ler CSV
from subprocess import list2cmdline
from turtle import title
import pandas as pd

df = pd.read_csv('FatoCondutorCNH1.CSV', delimiter = ';')
df.head()

# Confirmando tamanho do DF
df.shape

# Nomes das colunas
df.columns

# Tipo de dados
df.info()

# Temos 79 cidades
qtde_por_cidade.info()

# Media de idade dos condutores por cidade 
avg_condutor = df.groupby('MUNICIPIO')['IDADE'].mean().sort_values(ascending=False)
avg_condutor = avg_condutor.reset_index(name='Total')
avg_condutor

# Verificando cidades
cidades = df['MUNICIPIO'].unique()
print(cidades)

# Agrupando por municipio e sexo e contando os valores 
condut_sexo = df.groupby(['MUNICIPIO','SEXO'])['SEXO'].count()
condut_sexo = condut_sexo.reset_index(name='Total')
condut_sexo

# Deletando variaveis 
del df_agrupado
del df_top10

# Agrupando por cidade e renomeando a coluna que conterá os valores para Total
qtde_por_cidade = df.groupby('MUNICIPIO').size().sort_values(ascending=False)
qtde_por_cidade = qtde_por_cidade.reset_index(name='Total')
qtde_por_cidade

# Atribuindo a uma lista as 10 cidades com mais condutores, para no futuro gerar um gráfico top 10 cidades com 2 barrras por sexo
# Aqui reaproveitei as cidades que estavam no top10_qtde para criar a lista com os municipios
lista_cidades = ['CAMPO GRANDE', 'DOURADOS', 'TRES LAGOAS', 'CORUMBA', 'PONTA PORA',
       'NOVA ANDRADINA', 'PARANAIBA', 'NAVIRAI', 'AQUIDAUANA', 'MARACAJU',
       'COXIM']


# Filtrando o DF pela lista de cidades trazendo os valores de um DF ja existente
condut_sexo_filtrado = condut_sexo[condut_sexo['MUNICIPIO'].isin(lista_cidades)]
condut_sexo_filtrado.sort_values(by='Total', ascending=False, inplace=True)
condut_sexo_filtrado


# Pegando a lista top 10 , lembrando que python começa do 0 e não conta o ultimo valor
top10_qtde = qtde_por_cidade.head(11)
top10_qtde['MUNICIPIO'].unique()

# Media de idade dos condutores por cidade 
avg_top10 = avg_condutor[avg_condutor['MUNICIPIO'].isin(lista_cidades)]
avg_top10

# Importando plotly
import plotly.express as px

# GRÁFICOS 
# 1 Total de condutores pelo top 10 municipios(Maior Qtde)
graph_1 = px.bar(x=(top10_qtde['MUNICIPIO']), y=(top10_qtde['Total']),title='Top 10 municipios por qtde')
graph_1.show()
# 2 Total de condutores por sexo e pelos tops 10 municipios
graph_2 = px.bar(condut_sexo_filtrado, x='MUNICIPIO', y='Total', color='SEXO', barmode='group', title='Qtde de condutores por sexo')
graph_2.show()
# 3 Média de idade condutores top 10 city
graph_3 = px.scatter(avg_top10, x='MUNICIPIO', y='Total',  title='Média de idade')
graph_3.show()


# Criando o gráfico de dispersão
graph_3 = px.scatter(avg_top10, x='MUNICIPIO', y='Total',
                     title='Média de idade por Município',
                     labels={'MUNICIPIO': 'Município', 'Total': 'Média de Idade'},
                     color='Total',  # Colorindo os pontos pela média de idade
                     size='Total',   # Ajustando o tamanho dos pontos pela média de idade
                     hover_name='MUNICIPIO')  # Mostrar o nome do município ao passar o mouse

# Personalizando o layout
graph_3.update_layout(
    xaxis_title='Município',
    yaxis_title='Média de Idade',
    coloraxis_colorbar=dict(
        title='Média de Idade'
    ),
    plot_bgcolor='white',
    font=dict(
        family="Arial, sans-serif",
        size=12,
        color="RebeccaPurple"
    )
)

# Mostrando o gráfico
graph_3.show()
