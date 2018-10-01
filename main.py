import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

data = [go.Histogram(x=random_x)]
data_scatter = [
	go.Scatter(
    	x = random_x,
    	y = random_y,
    	mode = 'markers'
	)
]
data_line = [
	go.Scatter(
    	x = random_x,
    	y = random_y
	)
]

app = dash.Dash()

app.layout = html.Div(
    [
    	# Header
		html.Div(
			[
				html.Span(
					"LAGO UVG",
					className='app-title',
					style={'color': '#2a3f5f'}
				),
			
				html.Div(
					html.Img(
						src='http://wiki.lagoproject.org/images/lago-logo-90.png?86ebb',
						height="100%"
					),
					style={"float":"right","height":"100%"}
				)
			],
			className="row header",
			style={"backgroundColor": "white", "padding": "1%"}
		),

		# Tabs
		html.Div(
			[
				dcc.Tabs(
					id="tabs",
					style={"height":"20","verticalAlign":"middle"},
					children=[
						dcc.Tab(label="VEM", value="vem_tab"),
						dcc.Tab(label="GMM-EM", value="gmmem_tab"),
						dcc.Tab(label="ML", value="ml_tab"),
					],
					value="vem_tab",
				)
			],
			className="row tabs_div"
		),
		# Tab content
        html.Div(id="tab_content", className="row", style={"margin": "2% 3%"}),

		# CSS references
        html.Link(href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Dosis", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css", rel="stylesheet")
	],
	className="row",
	style={"margin": "0%"}
)

@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def render_content(tab):
    if tab == "vem_tab":
        return vem_layout

vem_layout = [
	# top controls
    html.Div(
        [
			html.H4("Filtrar por:"),
            html.Div(
                dcc.Dropdown(
                    id="date_dropdown",
					placeholder="Fecha",
                    options=[
                        {"label": "Dia", "value": "D"},
                        {"label": "Semana", "value": "W-MON"},
                        {"label": "Mes", "value": "M"},
						{"label": "Año", "value": "M"},
                    ],
                ),
                className="two columns",
                style={"marginBottom": "10"},
            ),
            html.Div(
                dcc.Dropdown(
                    id="location_dropdown",
					placeholder="Lugar",
                    options=[
                        {"label": "Todo", "value": "all"},
                        {"label": "UVG Guatemala", "value": "Phone"},
                        {"label": "Atitlán", "value": "Web"},
                    ],
                ),
                className="two columns",
            ),

            # add button
            #html.Div(
            #    html.Span(
            #        "Add new",
            #        id="new_case",
            #        n_clicks=0,
            #        className="button button--primary add",
            #        
            #    ),
            #    className="two columns",
            #    style={"float": "right"},
            #),
        ],
        className="row",
    ),
	html.Div([
		html.Div([
			dcc.Graph(
				id='life-exp-vs-gdp',
				figure={
					'data': data,
					'layout': go.Layout(
						xaxis={'title': 'GDP Per Capita'},
						yaxis={'title': 'Life Expectancy'},
						margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
						legend={'x': 0, 'y': 1},
						hovermode='closest'
					)
				}
			)],
			className="four columns chart_div",
		),
		html.Div([
			dcc.Graph(
				id='life-exp-vs-gdp2',
				figure={
					'data': data_scatter,
					'layout': go.Layout(
						xaxis={'title': 'GDP Per Capita'},
						yaxis={'title': 'Life Expectancy'},
						margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
						legend={'x': 0, 'y': 1},
						hovermode='closest'
					)
				}
			)],
			className="four columns chart_div",
		),
		html.Div([
			dcc.Graph(
				id='life-exp-vs-gdp3',
				figure={
					'data': data_line,
					'layout': go.Layout(
						xaxis={'title': 'GDP Per Capita'},
						yaxis={'title': 'Life Expectancy'},
						margin={'l': 40, 'b': 40, 't': 40, 'r': 40},
						legend={'x': 0, 'y': 1},
						hovermode='closest'
					)
				}
			)],
			className="four columns chart_div",
		),
	])
]


if __name__ == '__main__':
    app.run_server(debug=True)