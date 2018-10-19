import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np

amplitude_risetime = pd.read_csv(
    'static/amplitude_risetime.csv',
    delimiter=',',
    header=0
)
data_amplitude_risetime = [
    go.Scatter(
        x=amplitude_risetime['amplitude'],
        y=amplitude_risetime['rise_time']
    )
]

gmmem_layout = [
    # top controls
    html.Div(
        html.Div([
            dcc.Graph(
                id='time-vs-pulseamp',
                figure={
                    'data': data_amplitude_risetime,
                    'layout': go.Layout(
                        title='Rise Time vs Pulse Amplitude',
                        xaxis={'title': 'Pulse Amplitude'},
                        yaxis={'title': 'Rise Time'},
                        margin={'l': 40, 'b': 40,
                            't': 40, 'r': 40},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                })
            ],
            className="twelve columns",
        ),
        className="row"
    )
]