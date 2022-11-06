from matplotlib.pyplot import connect
import mysql.connector
import dash
from dash import Dash, dcc, html, Input, Output
import plotly.graph_objs as go
import pandas as pd

#iniciamos con maduras 0 y inmaduras 1
maduras=3
inmaduras=10

#inciamos el html con estos headers y grafica
app = dash.Dash()

app.layout = html.Div(children=[
    html.H1(children='Dashboard AIvocado'),
    dcc.Graph(id='maduracion'), 
    dcc.Interval(
        id='interval-component',
        interval=5*1000, # intervalo de refresco en milisegundos
        n_intervals=0
    )
])

@app.callback(Output("maduracion","figure"),Input('interval-component','n_intervals'))

def actualizacion_datos(n):
    cnn = mysql.connector.connect(host="localhost", user="root", 
    passwd="paltas", database="aivocado")

    cur = cnn.cursor()
    cur.execute("SELECT * FROM maduracion")
    datos = cur.fetchall()

    id,maduras,inmaduras = datos[0]

    print('TENEMOS',maduras,'PALTAS MADURAS')
    print('TENEMOS',inmaduras,'PALTAS INMADURAS')

    fig = {
        'data': [
            {'x': ['Maduro','Inmaduro'], 'y': [maduras, inmaduras], 'type': 'bar', 'name': 'Paltas Analizadas por AIvocado'},
        ],
        'layout': {
            'title': 'Madurez de la palta'
        }
    }
    
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)

