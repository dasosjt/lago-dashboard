import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from app import app
from views.vem import vem_layout
from views.gmmem import gmmem_layout

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
                        src='http://lagoproject.org/images/lago-logo-90.png',
                        height="100%"
                    ),
                    style={"float": "right", "height": "100%"}
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
                    style={"height": "20", "verticalAlign": "middle"},
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
        html.Div(id="tab_content", className="row",
                    style={"margin": "2% 3%"}),

        # CSS references
        html.Link(
            href="https://use.fontawesome.com/releases/v5.2.0/css/all.css",
            rel="stylesheet"
        ),
        html.Link(
            href="https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css",
            rel="stylesheet"
        ),
        html.Link(
            href="https://fonts.googleapis.com/css?family=Dosis",
            rel="stylesheet"
        ),
        html.Link(
            href="https://fonts.googleapis.com/css?family=Open+Sans", rel="stylesheet"),
        html.Link(
            href="https://fonts.googleapis.com/css?family=Ubuntu", rel="stylesheet"),
        html.Link(
            href="https://cdn.rawgit.com/amadoukane96/8a8cfdac5d2cecad866952c52a70a50e/raw/cd5a9bf0b30856f4fc7e3812162c74bfc0ebe011/dash_crm.css",
            rel="stylesheet"
        )
    ],
    className="row",
    style={"margin": "0%"}
)


@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def render_content(tab):
    if tab == "vem_tab":
        return vem_layout
    elif tab == "gmmem_tab":
        return gmmem_layout
    return "Hello"

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')