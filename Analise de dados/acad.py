import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from dash import dcc, Input, Output


# Carregue seus dados
tabela = pd.read_csv("cancelamentos_sample.csv")
tabela = tabela.drop(columns="CustomerID")
tabela = tabela.dropna()


# Crie o layout do seu dashboard
app = dash.Dash(__name__, external_stylesheets=['style.css'])

app.layout = html.Div([
    html.H1('Cancelamentos Academia', id= 'h1'),
    html.H2('Análise de taxa de cancelamento de clientes da academia', id = 'h2'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': i, 'value': i} for i in tabela.columns],
        value='duracao_contrato',
        style={'width': '50%', 'margin': 'auto'}
    ),
    dcc.Graph(id='grafico')
])

# Callback para atualizar o gráfico baseado no dropdown
@app.callback(
    dash.dependencies.Output('grafico', 'figure'),
    [dash.dependencies.Input('dropdown', 'value')]
)
def update_graph(coluna_selecionada):
    return px.histogram(tabela, x=coluna_selecionada, color="cancelou",
                        title='Histograma de {}'.format(coluna_selecionada),
                        labels={'cancelou': 'Cancelou (Sim/Não)', coluna_selecionada: 'Valor'})

if __name__ == '__main__':
    app.run_server(debug=True)
