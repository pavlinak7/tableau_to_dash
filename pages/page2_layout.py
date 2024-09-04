from plotly.subplots import make_subplots
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html
from tableauToDashFunkce import *


##################################################################################################

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path='/page-2')

layout = dbc.Container(
    [
        dbc.Row(  # A1
            className="radekA1",
            children=[
                dbc.Col(  # B1
                    className="oblastB sloupecB1",
                    children=[
                        dbc.Row(  # C1
                            className="B1radekC1",
                            children=[
                                dbc.Col(  # D1
                                    className="B1sloupecD1",
                                    children=[
                                        dbc.Row(  # výplň
                                            className="B1D1vypln",
                                            children=[
                                                dbc.Col(  # výplň
                                                )
                                            ],
                                        ),
                                        dbc.Row(  # B1radekE1
                                            className="B1radekE1",
                                            children=[
                                                dbc.Col(  # B1sloupecE1
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div( #B1E1div
                                                            className="B1E1div",
                                                            children=[
                                                                html.Img(
                                                                    src="/assets/Logo.png",
                                                                    className="B1E1obr",
                                                                )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row(  # výplň
                                            className="B1D1vypln2",
                                            children=[
                                                dbc.Col(  # výplň
                                                )
                                            ],
                                        ),
                                        dbc.Row(  # B1radekE2
                                            className="B1radekE1",
                                            children=[
                                                dbc.Col(  # B1sloupecE2
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div(
                                                            className="B1E1div",
                                                            children=[
                                                                dcc.Link(
                                                                html.Img(
                                                                    src="/assets/dashboard-summary-inactive.png", 
                                                                    className="B1E2obr",
                                                                    ),
                                                                    href="/"
                                                                )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row(  # B1radekE3
                                            className="B1radekE3",
                                            children=[
                                                dbc.Col(  # B1sloupecE3
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div(
                                                            className="B1E1div",
                                                            children=[
                                                                dcc.Link(
                                                                html.Img(
                                                                    src="/assets/dashboard-records-active1.png", 
                                                                    className="B1E3obr",
                                                                    ),
                                                                    href="/page-2"
                                                                )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row(  # výplň
                                            className="B1D1vypln2",
                                            children=[
                                                dbc.Col(  # vypln
                                                )
                                            ],
                                        ),
                                        dbc.Row( # B1radekE4
                                            className="B1radekE4",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div("Info", 
                                                                 style={
                                                                        "textAlign": "center", "fontSize": "9px", "color": "white"}
                                                                 ),
                                                        html.Div(
                                                            style={
                                                                'width': '80%',
                                                                # Simulating horizontal line with bottom border
                                                                'border-bottom': '0.3px solid white',
                                                                # Scale it down to make it 0.5px
                                                                'transform': 'scaleY(0.5)',
                                                                'transform-origin': 'bottom',  # Ensure it scales from the bottom
                                                                'margin': '0 auto'  # 'margin': '0 auto'
                                                                # 'margin': '10px 0'
                                                            }
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #B1radekE5
                                            className="B1radekE5",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div(
                                                            className="B1E1div",
                                                            children=[
                                                                html.Img(
                                                                    src="/assets/info-hidden.png", 
                                                                    className="B1E5obr",
                                                                    )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #vypln
                                            className="B1D1vypln3",
                                            children=[
                                                dbc.Col(
                                                )
                                            ],
                                        ),
                                        dbc.Row( #B1radekE6
                                            className="B1radekE4",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div("Export", style={
                                                            "textAlign": "center", "fontSize": "9px", "color": "white"}
                                                                 ),
                                                        html.Div(
                                                            style={
                                                                'width': '80%',
                                                                # Simulating horizontal line with bottom border
                                                                'border-bottom': '0.3px solid white',
                                                                # Scale it down to make it 0.5px
                                                                'transform': 'scaleY(0.5)',
                                                                'transform-origin': 'bottom',  # Ensure it scales from the bottom
                                                                'margin': '0 auto'  # 'margin': '0 auto'
                                                                # 'margin': '10px 0'
                                                            }
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #B1radekE7
                                            className="B1radekE1",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div(
                                                            className="B1E1div",
                                                            children=[
                                                                html.Img(
                                                                    src="/assets/download pdf.png", 
                                                                    className="B1E7obr",
                                                                    )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #B1radekE8
                                            className="B1radekE1",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div(
                                                            className="B1E1div",
                                                            children=[
                                                                html.Img(
                                                                    src="/assets/download image.png", 
                                                                    className="B1E7obr",
                                                                    )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #vypln
                                            className="B1D1vypln3",
                                            children=[
                                                dbc.Col(
                                                )
                                            ],
                                        ),
                                        dbc.Row(#B1radekE9
                                            className="B1radekE4",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div("Follow", 
                                                                 style={
                                                            "textAlign": "center", "fontSize": "9px", "color": "white"}
                                                                 ),
                                                        html.Div(
                                                            style={
                                                                'width': '80%',
                                                                # Simulating horizontal line with bottom border
                                                                'border-bottom': '0.3px solid white',
                                                                # Scale it down to make it 0.5px
                                                                'transform': 'scaleY(0.5)',
                                                                'transform-origin': 'bottom',  # Ensure it scales from the bottom
                                                                'margin': '0 auto'  # 'margin': '0 auto'
                                                                # 'margin': '10px 0'
                                                            }
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #B1radekE10
                                            className="B1radekE10",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div(
                                                            className="B1E1div",
                                                            children=[
                                                                html.Img(
                                                                    src="/assets/contact-channel.png", 
                                                                    className="B1E10obr",
                                                                    )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #B1radekE11
                                            className="B1radekE5",
                                            children=[
                                                dbc.Col(
                                                    className="B1sloupecE1",
                                                    children=[
                                                        html.Div(
                                                            className="B1E1div",
                                                            children=[
                                                                html.Img(
                                                                    src="/assets/contact-linkedin.png", 
                                                                    className="B1E10obr",
                                                                    )
                                                            ]
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dbc.Row( #vypln
                                            className="B1D1vypln5",
                                            children=[
                                                dbc.Col(
                                                )
                                            ],
                                        ),
                                    ],

                                )
                            ]
                        )
                    ],
                    width=1,
                ),
                dbc.Col(
                    className="oblastB sloupecB2",
                )
            ],
        ),
        # Placeholder for callback
    ],
    fluid=True
)





