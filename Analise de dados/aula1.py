import aula1
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

df = pd.read_csv("cancelamentos_sample.csv")

app = aula1.Dash(__name__)
fig = px.bar(df, x="idade", y="cancelou", color = "cancelou", barmode= "group")
app.layout = html.Div
([
    html.H1('Cancelamentos Academia'),
    html.H2('analise de taxa de cancelamento de clientes da academia'),
])