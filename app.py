import flask
import dash
import dash_core_components as dcc
import dash_html_components as html

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)
app.config.suppress_callback_exceptions = True

def df_to_table(df):
    return html.Table(
        [html.Tr([html.Th(col) for col in df.columns])] +
        [
            html.Tr(
                [
                    html.Td(df.iloc[i][col])
                    for col in df.columns
                ]
            )
            for i in range(len(df))
        ]
    )
