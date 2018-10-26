from datetime import datetime as dt
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import numpy as np

time_pulseamp = pd.read_csv(
    'static/time_pulseamp.csv',
    delimiter=',',
    header=0
)
data_time_pulseamp = [
    go.Scatter(
        x=time_pulseamp['pulse_index'],
        y=time_pulseamp['pulse_amp']
    )
]

adcq_count = pd.read_csv('static/adcq_count.csv', delimiter=',', header=0)
data_adcq_count = [
    go.Bar(
        x=adcq_count['startValues'],
        y=adcq_count['count']
    )
]

log_adcq_count = pd.read_csv('static/log_adcq_count.csv', delimiter=',', header=0)
data_log_adcq_count = [
    go.Bar(
        x=log_adcq_count['startValues'],
        y=log_adcq_count['count']
    )
]

df_log_adcq = pd.read_csv('static/df_one.csv', delimiter=',', header=0)
data_df_log_adcq = [
    go.Scatter(
        x=df_log_adcq['x'],
        y=df_log_adcq['y']
    )
]

df_second_log_adcq = pd.read_csv('static/df_second.csv', delimiter=',', header=0)
data_df_second_log_adcq = [
    go.Scatter(
        x=df_second_log_adcq['x'],
        y=df_second_log_adcq['y']
    )
]

df_log_adcq_count = pd.read_csv('static/df_log_adcq_count.csv', delimiter=',', header=0)
data_df_log_adcq_count = [
    go.Histogram2d(
        x=df_log_adcq_count['_1'],
        y=df_log_adcq_count['_2'],
        nbinsx=14,
        nbinsy=14   
    )
]

sme_layout = [
    # top controls
    html.Div([
        html.H4("Filtrar por:"),
        html.Div([
            html.Div([
                html.Span(
                    "Fecha: ",
                    style={ 
                        'margin': '0.5rem',
                        'font-weight': 'bold'
                    }
                ),
                dcc.DatePickerSingle(
                    id='my-date-picker-single',
                    placeholder='Fecha: ',
                    min_date_allowed=dt(1995, 8, 5),
                    max_date_allowed=dt(2017, 9, 19),
                    initial_visible_month=dt(2017, 8, 5),
                    date=dt(2017, 8, 25),
                )
            ],
            className="two columns"
            ),
            html.Div([
                html.Span(
                    "Lugar: ",
                    style={ 
                        'margin': '0.5rem',
                        'font-weight': 'bold'
                    }
                ),
                dcc.Dropdown(
                    id="location_dropdown",
                    options=[
                        {"label": "Todo", "value": "all"},
                        {"label": "UVG Guatemala", "value": "Phone"},
                        {"label": "Atitlán", "value": "Web"},
                    ],
                    style={
                        'padding': '0.5rem 0',
                        'font-weight': '200',
                        'font-size': '18px',
                        'line-height': '24px'
                    },
                    value="Phone"
                )
            ],
            className="two columns"
            ),
        ],
        className="row",
        style={"marginBottom": "10"},
        ),
    ]),
    html.Div(
        html.Div([
            dcc.Graph(
                id='time-vs-pulseamp',
                figure={
                    'data': data_time_pulseamp,
                    'layout': go.Layout(
                        title='Time vs Pulse Amplitude',
                        xaxis={'title': 'Time'},
                        yaxis={'title': 'Pulse Amplitude'},
                        margin={'l': 40, 'b': 40,
                            't': 40, 'r': 40},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                })
            ],
            className="twelve columns chart",
        ),
        className="row"
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id='adcq-vs-count',
                figure={
                    'data': data_adcq_count,
                    'layout': go.Layout(
                        title='Histogram ADCq',
                        
                        xaxis={'title': 'ADCq'},
                        yaxis={'title': 'Count'},
                        margin={'l': 40, 'b': 40,
                                't': 40, 'r': 40},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                }
            )],
            className="six columns chart",
        ),
        html.Div([
            dcc.Graph(
                id='log-adcq-vs-count',
                figure={
                    'data': data_log_adcq_count,
                    'layout': go.Layout(
                        title='Histogram log_10(ADCq)',
                        xaxis={'title': 'Log10(ADCq)'},
                        yaxis={'title': 'Count'},
                        margin={'l': 40, 'b': 40,
                                't': 40, 'r': 40},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                }
            )], 
            className="six columns chart",
        )], 
        className='row'    
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id='df-log-adcq',
                figure={
                    'data': data_df_log_adcq,
                    'layout': go.Layout(
                        title='First Derivative log10(ADCq)',
                        xaxis={'title': 'x'},
                        yaxis={'title': 'y'},
                        margin={'l': 40, 'b': 40,
                                't': 40, 'r': 40},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                }
            )],
            className="six columns chart",
        ),
        html.Div([
            dcc.Graph(
                id='df2-log-adcq',
                figure={
                    'data': data_df_second_log_adcq,
                    'layout': go.Layout(
                        title='Second Derivative log10(ADCq)',
                        xaxis={'title': 'x'},
                        yaxis={'title': 'y'},
                        margin={'l': 40, 'b': 40,
                                't': 40, 'r': 40},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest'
                    )
                }
            )], 
            className="six columns chart",
        )], 
        className='row'    
    ),
    html.Div([ 
        html.Div([
            dcc.Graph(
                id='df-log-adcq-vs-count',
                figure={
                    'data': data_df_log_adcq_count,
                    'layout': go.Layout(
                        title='Histogram: Count DF(log(adcq))',
                        xaxis={'title': 'DF(log(adcq))'},
                        yaxis={'title': 'log(adcq)'},
                        margin={'l': 40, 'b': 40,
                            't': 40, 'r': 40},
                        legend={'x': 0, 'y': 1},
                        hovermode='closest',
                    )
                })
            ],
            className="twelve columns chart",
        ),
    ],
    className='row'
    )
]