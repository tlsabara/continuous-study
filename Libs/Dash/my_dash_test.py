from dash import Dash
from dash_html_components import H1, Div, P
from dash_core_components import Graph

app = Dash(__name__)


grafico1 = Graph(
    figure={
        'data':[
            {
                'y': [0, 25, 59, 75, 100], 'type': 'lines'
            }
        ],
        "layout": {}
    }
)


app.layout = Div(
    children=[
        H1("Boas Vindas!!!"),
        P("este é um paragrafo."),
        grafico1
    ]
)

app.run_server(debug=True)
