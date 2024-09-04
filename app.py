import dash
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
from plotly.subplots import make_subplots
import pandas as pd
from tableauToDashFunkce import *

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], use_pages=True)

from pages.page1_layout import layout as page_1_layout
from pages.page2_layout import layout as page_2_layout

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    #html.Div(id='page-content'),
    dash.page_container
])


# @app.callback(
#     Output('page-content', 'children'),
#     [Input('url', 'pathname')]
# )
# def display_page(pathname):
#     if pathname == '/' or pathname == '/page-1':
#         return page_1_layout
#     elif pathname == '/page-2':
#         return page_2_layout
#     else:
#         return page_1_layout  # Default to Page 1 if path is not recognized


if __name__ == '__main__':
    app.run_server(debug=True)
