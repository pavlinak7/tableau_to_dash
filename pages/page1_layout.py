from plotly.subplots import make_subplots
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, callback, clientside_callback
import pandas as pd
from dash.dependencies import Input, Output, State
from tableauToDashFunkce import *


##################################################################################################

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path='/')

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
                                                                    src="/assets/dashboard-summary-active.png", 
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
                                                                    src="/assets/dashboard-records-inactive.png", 
                                                                    className="B1E3obr",
                                                                    ),
                                                                href = "/page-2"
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
                                                                        id="download-pdf",
                                                                        #style={'cursor': 'pointer'}
                                                                    ),
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
                                                                    id="download-image",
                                                                    #style={'cursor': 'pointer'} 
                                                                    )
                                                            ]
                                                        ),
                                                        #html.Div(id='download-image-link', style={'display': 'none'})
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
                                                                dcc.Link(
                                                                children=html.Img(
                                                                    src="/assets/contact-channel.png", 
                                                                    className="B1E10obr",
                                                                    style={'cursor': 'pointer'}
                                                                    ),
                                                                href="https://www.youtube.com/watch?v=UcGF09Awm4Y&t=1497s",
                                                                target="_blank"  # Opens the link in a new tab
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
                                                                dcc.Link(
                                                                children=html.Img(
                                                                    src="/assets/contact-linkedin.png", 
                                                                    className="B1E10obr",
                                                                    style={'cursor': 'pointer'}
                                                                    ),
                                                                href="https://www.linkedin.com/in/pavlina-kurkova-a30939109",
                                                                target="_blank"  # Opens the link in a new tab
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
                dbc.Col( #sloupecB2
                    className="oblastB sloupecB2",
                    children=[
                        dbc.Row( #B2radekC1 
                            className="B2radekC1",
                            children=[ 
                                dbc.Col( #B2sloupecD1
                                    className="B2sloupecD1",
                                    children=[
                                        html.Div( #B2D1div
                                            [
                                                html.Span("Human Resources Dashboard | ", 
                                                          style={
                                                          "fontWeight": "bold",
                                                          'font-size': '26px', 
                                                          }
                                                          ),
                                                html.Span("Overview", 
                                                          style={
                                                          "fontWeight": "normal",
                                                          'font-size': '18px', 
                                                          }
                                                          )
                                            ],
                                            className="B2D1div",

                                        )
                                    ],
                                ),
                                dbc.Col( #B2sloupecD2
                                    id = "filter_panel",
                                    style={
                                        "display": "none",
                                        # "border": "2px dashed yellow",
                                        "backgroundColor": "rgb(85, 85, 85)",
                                        # "padding": "10px",
                                        "flex-basis": "44%", "max-width": "44%",
                                        "position": "relative",
                                    },
                                    children=[
                                        dbc.Row( #B2radekE1
                                            className="B2radekE1",
                                            children=[
                                                dbc.Col( #B2E1sloupecF1
                                                    html.Div( #B2E1F1div
                                                        "Gender", 
                                                        className="B2E1F1div",
                                                             ),
                                                    className="B2E1sloupecF1",
                                                ),
                                                dbc.Col( #B2E1sloupecF2
                                                    html.Div(
                                                        "Status", 
                                                        className="B2E1F1div",
                                                        ),
                                                    className="B2E1sloupecF1",
                                                ),
                                                dbc.Col( #B2E1sloupecF3
                                                    html.Div("Location", 
                                                             className="B2E1F1div",
                                                             ),
                                                    className="B2E1sloupecF1",
                                                ),
                                                dbc.Col( #B2E1sloupecF4
                                                    html.Div("Hiredate", 
                                                             className="B2E1F1div",
                                                             ),
                                                    className="B2E1sloupecF1",
                                                ),
                                            ]
                                        ),
                                        dbc.Row( #B2radekE2
                                            className="B2radekE2",
                                            children=[
                                                dbc.Col( #B2E2sloupecF1
                                                    className="B2E1sloupecF1",
                                                    children=[
                                                        html.Button(
                                                            [
                                                                "(All)",
                                                                html.Span(
                                                                    className="dropdown-arrow")
                                                            ],
                                                            id="dropdown-button", className="dropdown-button",
                                                            style={
                                                                "border": "1px solid white",
                                                            },
                                                            # n_clicks=0

                                                        ),
                                                        html.Div(
                                                            dcc.Checklist(
                                                                id='gender-dropdown',
                                                                options=[
                                                                    {'label': 'Female',
                                                                        'value': 'Female'},
                                                                    {'label': 'Male',
                                                                        'value': 'Male'}
                                                                ],
                                                                # value=[
                                                                #     'Female', 'Male'],
                                                                labelStyle={
                                                                    'display': 'block'},
                                                                inputStyle={
                                                                    'margin-right': '5px',
                                                                    'transform': 'scale(1.2)',
                                                                },
                                                                style={
                                                                    'backgroundColor': 'rgb(85, 85, 85)',
                                                                    'font-size': '10px',
                                                                    'padding': '5px',
                                                                    'color': 'white',
                                                                    # "border": "2px dashed yellow",
                                                                }
                                                            ),
                                                            id="dropdown-menu",
                                                            className="dropdown-menu",
                                                            # Initially hidden
                                                            style={
                                                                "display": "none",
                                                            }
                                                        )
                                                    ]
                                                ),
                                                dbc.Col( #B2E2sloupecF2
                                                    className="B2E1sloupecF1",
                                                    children=[
                                                        html.Button(
                                                            [
                                                                "(All)",
                                                                html.Span(
                                                                    className="dropdown-arrow")
                                                            ],
                                                            id="dropdown-button2", className="dropdown-button",
                                                            style={
                                                                "border": "1px solid white",
                                                            },
                                                            # n_clicks=0

                                                        ),
                                                        html.Div(
                                                            dcc.Checklist(
                                                                id='status-dropdown',
                                                                options=[
                                                                    {'label': 'ne',
                                                                     'value': 'ne'},
                                                                    {'label': 'ano',
                                                                     'value': 'ano'}
                                                                ],
                                                                # value=[
                                                                #     'Female', 'Male'],
                                                                labelStyle={
                                                                    'display': 'block'},
                                                                inputStyle={
                                                                    'margin-right': '5px',
                                                                    'transform': 'scale(1.2)',
                                                                },
                                                                style={
                                                                    'backgroundColor': 'rgb(85, 85, 85)',
                                                                    'font-size': '10px',
                                                                    'padding': '5px',
                                                                    'color': 'white',
                                                                    # "border": "2px dashed yellow",
                                                                }
                                                            ),
                                                            id="dropdown-menu2",
                                                            className="dropdown-menu",
                                                            # Initially hidden
                                                            style={
                                                                "display": "none",
                                                            }
                                                        )
                                                    ],
                                                ),
                                                dbc.Col( #B2E2sloupecF3
                                                    className="B2E1sloupecF1",
                                                    children=[
                                                        html.Button(
                                                            [
                                                                "(All)",
                                                                html.Span(
                                                                    className="dropdown-arrow")
                                                            ],
                                                            id="dropdown-button3", className="dropdown-button",
                                                            style={
                                                                "border": "1px solid white",
                                                            },
                                                            # n_clicks=0

                                                        ),
                                                        html.Div(
                                                            dcc.Checklist(
                                                                id='location-dropdown',
                                                                options=[
                                                                    {'label': 'HQ',
                                                                     'value': 'HQ'},
                                                                    {'label': 'Branch',
                                                                     'value': 'Branch'}
                                                                ],
                                                                # value=[
                                                                #     'Female', 'Male'],
                                                                labelStyle={
                                                                    'display': 'block'},
                                                                inputStyle={
                                                                    'margin-right': '5px',
                                                                    'transform': 'scale(1.2)',
                                                                },
                                                                style={
                                                                    'backgroundColor': 'rgb(85, 85, 85)',
                                                                    'font-size': '10px',
                                                                    'padding': '5px',
                                                                    'color': 'white',
                                                                    # "border": "2px dashed yellow",
                                                                }
                                                            ),
                                                            id="dropdown-menu3",
                                                            className="dropdown-menu",
                                                            # Initially hidden
                                                            style={
                                                                "display": "none",
                                                            }
                                                        )
                                                    ],
                                                ),
                                                dbc.Col( #B2E2sloupecF4
                                                    className="B2E1sloupecF1",
                                                    children=[
                                                        html.Button(
                                                            [
                                                                "(All)",
                                                                html.Span(
                                                                    className="dropdown-arrow")
                                                            ],
                                                            id="dropdown-button4", className="dropdown-button",
                                                            style={
                                                                "border": "1px solid white",
                                                                "width": "100%",
                                                            },
                                                            # n_clicks=0

                                                        ),
                                                        html.Div(
                                                            dcc.Checklist(
                                                                id='hire-dropdown',
                                                                options=[
                                                                    # {'label': 'All',
                                                                    #  'value': 'All'},
                                                                    {'label': 2015,
                                                                     'value': 2015},
                                                                    {'label': 2016,
                                                                     'value': 2016},
                                                                    {'label': 2017,
                                                                     'value': 2017},
                                                                    {'label': 2018,
                                                                     'value': 2018},
                                                                    {'label': 2019,
                                                                     'value': 2019},
                                                                    {'label': 2020,
                                                                     'value': 2020},
                                                                    {'label': 2021,
                                                                     'value': 2021},
                                                                    {'label': 2022,
                                                                     'value': 2022},
                                                                    {'label': 2023,
                                                                     'value': 2023},
                                                                    {'label': 2024,
                                                                     'value': 2024}
                                                                ],
                                                                # value=[
                                                                #     'Female', 'Male'],
                                                                labelStyle={
                                                                    'display': 'block'},
                                                                inputStyle={
                                                                    'margin-right': '5px',
                                                                    'transform': 'scale(1.2)',
                                                                },
                                                                style={
                                                                    'backgroundColor': 'rgb(85, 85, 85)',
                                                                    'font-size': '10px',
                                                                    'padding': '5px',
                                                                    'color': 'white',
                                                                    # "border": "2px dashed yellow",
                                                                }
                                                            ),
                                                            id="dropdown-menu4",
                                                            className="dropdown-menu",
                                                            # Initially hidden
                                                            style={
                                                                "display": "none",
                                                                "width": "100%",
                                                            }
                                                        )
                                                    ],
                                                ),
                                            ]
                                        )
                                    ],
                                ),
                                dbc.Col(
                                    style={
                                        #"border": "4px dashed yellow",
                                        "backgroundColor": "rgb(85, 85, 85)",
                                        "flex-basis": "6%",  # Adjust the width to ensure button stays in place
                                        "max-width": "6%",  # Adjust the width
                                        "display": "flex",
                                        "justify-content": "center",
                                        "align-items": "center",
                                    },
                                    children=[
                                        html.Button(
                                            'Show Filters', id='toggle-button', 
                                            style={
                                            "fontSize": "12px",
                                            'fontFamily': '"Times New Roman", Times, serif',
                                            }
                                            ),
                                        ],
                                )
                            ]
                        ),
                        dbc.Row(
                            style={
                                # "border": "4px solid red",
                                "box-sizing": "border-box",
                                "height": "710px",
                            },
                            children=[
                                dbc.Col(
                                    style={
                                        # "border": "2px dashed cyan",
                                        "box-sizing": "border-box",
                                        "display": "flex",
                                        "flexDirection": "column",
                                        "backgroundColor": "lightgrey",
                                        "flex-basis": "30.5%",
                                        "max-width": "30.5%",
                                        "border-radius": "10px",
                                        "backgroundColor": "black"
                                        # "padding": "10px"
                                    },
                                    children=[
                                        dbc.Row(
                                            style={
                                                # "border": "2px solid purple",
                                                "height": "120px",
                                                "box-sizing": "border-box",
                                            },
                                            children=[
                                                dbc.Col(
                                                    style={
                                                        "box-sizing": "border-box",
                                                        "padding": "10px",
                                                        # "border": "2px dashed yellow",
                                                        # "backgroundColor": "black"
                                                    },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Div("Overview",
                                                                         style={
                                                                             "textAlign": "left",
                                                                             "fontSize": "18px",
                                                                             "color": "white",
                                                                             "fontWeight": "bold",
                                                                             'fontFamily': '"Times New Roman", Times, serif',
                                                                             "height": "40px",
                                                                         }
                                                                         ),
                                                                html.Div("Active Employees", style={
                                                                    "textAlign": "center", "fontSize": "12px",
                                                                    "color": "white", 'fontFamily': '"Times New Roman", Times, serif',
                                                                    "height": "25px", }),
                                                                html.Div(
                                                                    #f"{aktivni}", 
                                                                         id='all', style={
                                                                    "textAlign": "center", "fontSize": "20px", "color": "white",
                                                                    "height": "35px", }),
                                                                html.Div(
                                                                    style={
                                                                        'width': '95%',
                                                                        # Simulating horizontal line with bottom border
                                                                        'border-bottom': '0.3px solid white',
                                                                        # Scale it down to make it 0.5px
                                                                        'transform': 'scaleY(0.5)',
                                                                        'transform-origin': 'bottom',  # Ensure it scales from the bottom
                                                                        'margin': '0 auto'
                                                                        # 'margin': '10px 0'
                                                                    }
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            # Set the row height and flexbox alignment
                                            style={
                                                # "border": "2px solid purple",
                                                "height": "150px",
                                                "display": "flex", 
                                                "alignItems": "stretch", 
                                                "box-sizing": "border-box", 
                                                },
                                            children=[
                                                dbc.Col(
                                                    style={
                                                        "padding-left": "10px",
                                                        # "border": "2px dashed yellow",
                                                        "backgroundColor": "black",
                                                        "display": "flex",
                                                        "box-sizing": "border-box",
                                                        "flexDirection": "column",
                                                        "justifyContent": "space-between",  # Distribute space between elements
                                                        "height": "100%"
                                                    },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Div("Hired", style={
                                                                    "textAlign": "center", "fontSize": "12px", "color": "white",
                                                                    'fontFamily': '"Times New Roman", Times, serif',
                                                                    "height": "40px", }),
                                                                html.Div(
                                                                    #f"{hire_date_count}",
                                                                         id='hire-date-count',
                                                                         style={
                                                                             "textAlign": "center",
                                                                             "fontSize": "24px",
                                                                             "color": "white",
                                                                             "height": "70px",
                                                                         }
                                                                         ),
                                                                dcc.Graph(
                                                                    id='chart2_1',
                                                                    # Insert the Plotly graph here
                                                                    # figure=create_hire_trend_figure(
                                                                    #     hr),
                                                                    # Adjusted height to fit within the container
                                                                    style={"height": "60%",
                                                                           "width": "100%", "display": "block"}
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black",
                                                                "height": "100%", "display": "flex", "flexDirection": "column", "justifyContent": "space-between"}
                                                        )
                                                    ],
                                                ),
                                                dbc.Col(
                                                    style={
                                                        "display": "flex",
                                                        "box-sizing": "border-box",
                                                        "flexDirection": "column",
                                                        "justifyContent": "center",  # Center content vertically
                                                        "alignItems": "center",  # Center content horizontally
                                                        "height": "100%",
                                                        "flex-basis": "2%",  # Adjusted to a slightly more reasonable width
                                                        "max-width": "2%",  # Adjusted to a slightly more reasonable width
                                                    },
                                                    children=[
                                                        html.Div(
                                                            style={
                                                                'height': '95%',  # Adjust if needed for visual appearance
                                                                'border-right': '1px solid white',  # Keep this at 1px
                                                                # Scale down horizontally
                                                                'transform': 'scaleX(0.5)',
                                                                'transform-origin': 'left',  # Keep the line anchored on the left
                                                                'margin': '0 auto'
                                                            }
                                                        ),
                                                    ]
                                                ),
                                                dbc.Col(
                                                    style={
                                                        "padding-right": "10px",
                                                        # "border": "2px dashed yellow",
                                                        "backgroundColor": "black",
                                                        "display": "flex",
                                                        "flexDirection": "column",
                                                        "justifyContent": "space-between",  # Distribute space between elements
                                                        "height": "100%",
                                                        "box-sizing": "border-box",
                                                    },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Div("Terminated", style={
                                                                    "textAlign": "center", "fontSize": "12px", "color": "white",
                                                                    'fontFamily': '"Times New Roman", Times, serif',
                                                                    "height": "40px", }),
                                                                html.Div(
                                                                    #f"{hire_date_count}",
                                                                    id='hire-date-count2', style={
                                                                        "textAlign": "center", "fontSize": "24px", "color": "white",
                                                                        "height": "70px",}),
                                                                dcc.Graph(
                                                                    id='chart2_2',
                                                                    # Insert the Plotly graph here
                                                                    # figure=create_hire_trend_figure2(
                                                                    #     hr),
                                                                    # Adjusted height to fit within the container
                                                                    style={"height": "60%",
                                                                           "width": "100%", "display": "block"}
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black",
                                                                "height": "100%", "display": "flex", "flexDirection": "column", "justifyContent": "space-between"}
                                                        )
                                                    ],
                                                ),
                                            ]
                                        ),
                                        dbc.Row(
                                            style={
                                                # "border": "2px solid purple",
                                                "height": "200px",
                                                "box-sizing": "border-box", },
                                            children=[
                                                dbc.Col(
                                                    style={"padding": "10px",  # "border": "2px dashed yellow",
                                                           "backgroundColor": "black", "height": "100%", "box-sizing": "border-box", },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                # html.Div(
                                                                #     style={
                                                                #         'width': '100%',
                                                                #         # Simulating horizontal line with bottom border
                                                                #         'border-top': '0.3px solid white',
                                                                #         # Scale it down to make it 0.5px
                                                                #         'transform': 'scaleY(0.5)',
                                                                #         'transform-origin': 'top',  # Ensure it scales from the bottom
                                                                #         'margin': '0 auto 5px auto'
                                                                #     }
                                                                # ),
                                                                html.Div(
                                                                    children=[
                                                                        html.Span(
                                                                            style={'flex': 1, 'border-bottom': '1px solid gray'}),
                                                                        html.Span("Departments", style={
                                                                            'padding': '0 10px', 'color': 'white', 'fontFamily': '"Times New Roman", Times, serif', }),
                                                                        html.Span(
                                                                            style={'flex': 1, 'border-bottom': '1px solid gray'})
                                                                    ],
                                                                    style={
                                                                        'display': 'flex', 'align-items': 'center', "padding": "10px", }
                                                                ),
                                                                dcc.Graph(
                                                                    id='chart4',
                                                                    # figure=plot_department_termination(
                                                                    #     hr),  # Insert the Plotly graph here
                                                                    style={"height": "90%",
                                                                           "width": "100%", "display": "block"}
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            style={
                                                #"border": "2px solid purple",
                                                "height": "55px",
                                                "box-sizing": "border-box", 
                                                "padding-top": "11px"},
                                            children=[
                                                dbc.Col(
                                                    style={"padding": "10px",  
                                                           #"border": "2px dashed yellow",
                                                           "backgroundColor": "black", "height": "100%", "box-sizing": "border-box", 
                                                           },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                # html.Div(
                                                                #     style={
                                                                #         'width': '100%',
                                                                #         # Simulating horizontal line with bottom border
                                                                #         'border-top': '0.3px solid white',
                                                                #         # Scale it down to make it 0.5px
                                                                #         'transform': 'scaleY(0.5)',
                                                                #         'transform-origin': 'top',  # Ensure it scales from the bottom
                                                                #         'margin': '0 auto 5px auto'
                                                                #     }
                                                                # ),
                                                                html.Div(
                                                                    children=[
                                                                        html.Span(
                                                                            style={'flex': 1, 'border-bottom': '1px solid gray'}),
                                                                        html.Span("Location", style={
                                                                            'padding': '0 10px', 'color': 'white', 'fontFamily': '"Times New Roman", Times, serif', }),
                                                                        html.Span(
                                                                            style={'flex': 1, 'border-bottom': '1px solid gray'})
                                                                    ],
                                                                    style={
                                                                        'display': 'flex', 'align-items': 'center', "padding": "10px", }
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black", "height": "100%",
                                                                }
                                                        )
                                                    ],
                                                ),
                                            ],
                                        ),
                                        dbc.Row(
                                            style={
                                                # "border": "2px solid purple",
                                                "flex": "1",
                                                "box-sizing": "border-box", },
                                            children=[
                                                dbc.Col(
                                                    style={"padding": "10px",  # "border": "2px dashed yellow",
                                                           # "backgroundColor": "black",
                                                           "height": "100%", "box-sizing": "border-box", 
                                                           "flex-basis": "71%",  # Adjusted to a slightly more reasonable width
                                                           "max-width": "71%",  # Adjusted to a slightly more reasonable width
                                                           },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                dcc.Graph(id='chart5',
                                                                          # figure=create_zoomed_map_go(hr),  # Insert the Plotly graph here
                                                                          style={"height": "100%", "width": "auto", "display": "block"}, config={'responsive': True},
                                                                          ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                    width=8
                                                ),
                                                dbc.Col(
                                                    style={"padding": "10px",  # "border": "2px dashed yellow",
                                                           # "backgroundColor": "black",
                                                           "height": "100%", "box-sizing": "border-box", 
                                                           "flex-basis": "28%",  # Adjusted to a slightly more reasonable width
                                                           "max-width": "28%",  # Adjusted to a slightly more reasonable width
                                            },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                dcc.Graph(
                                                                    id='chart6',
                                                                    # Insert the Plotly graph here
                                                                    # figure=plot_lokace_distribution(hr),
                                                                    style={"height": "100%",
                                                                           "width": "auto", "display": "block"}
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                ),
                                            ]
                                        ),
                                    ],
                                    # width=3,
                                ),
                                dbc.Col(
                                    style={
                                        # "border": "2px dashed yellow",
                                        # "padding": "10px",
                                        "box-sizing": "border-box", "display": "flex", "flexDirection": "column", "backgroundColor": "rgb(85, 85, 85)",
                                        "flex-basis": "1.6%", "max-width": "1.6%"}),
                                dbc.Col(
                                    style={
                                        #"border": "2px dashed yellow",
                                        "display": "flex", "box-sizing": "border-box",
                                        # "padding": "10px"
                                        "flexDirection": "column", "backgroundColor": "rgb(85, 85, 85)",
                                        "flex-basis": "66%",
                                        "max-width": "66%",
                                        #"border-radius": "10px",
                                    },
                                    children=[
                                        dbc.Row(
                                            style={
                                                 #"border": "2px solid red",
                                                "backgroundColor": "black", 
                                                "height": "40px",
                                                "border-top-left-radius": "10px",
                                                "border-top-right-radius": "10px",
                                                },
                                            children=[
                                                dbc.Col(
                                                    style={
                                                        "padding": "10px",
                                                        # "border": "2px dashed yellow"
                                                    },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Div("Demographics", style={
                                                                    "textAlign": "left", "fontSize": "18px", "color": "white",
                                                                    'fontFamily': '"Times New Roman", Times, serif', "fontWeight": "bold", }),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", #"backgroundColor": "black", 
                                                                "height": "100%"}
                                                        )
                                                    ],
                                                )
                                            ]
                                        ),
                                        dbc.Row(
                                            style={
                                                #"border": "2px solid purple",
                                                "box-sizing": "border-box",
                                                "height": "325px",
                                                "border-bottom-left-radius": "10px",
                                                "border-bottom-right-radius": "10px",
                                                "backgroundColor": "black",
                                                "padding-top": "5px",
                                                "padding-bottom": "20px",
                                            },
                                            children=[
                                                dbc.Col(
                                                    style={
                                                       # "padding": "5px",
                                                        # "border": "2px dashed yellow",
                                                        "box-sizing": "border-box",
                                                        #"backgroundColor": "black",
                                                        "height": "100%", "flex-basis": "17.6%", "max-width": "17.6%",
                                                        #"border-radius": "10px",
                                                    },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Div("Gender", style={
                                                                    "textAlign": "center", "fontSize": "14px", "color": "white",
                                                                    'fontFamily': '"Times New Roman", Times, serif'}),
                                                                dcc.Graph(
                                                                    id='chart7_2',
                                                                    # figure=fig_men,
                                                                    style={
                                                                        "height": "43%", "width": "120%", "display": "block"}
                                                                ),
                                                                dcc.Graph(
                                                                    id='chart7_1',
                                                                    # figure=fig_women,
                                                                    style={
                                                                        "height": "43%", "width": "120%", "display": "block"}
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                    width=3
                                                ),
                                                dbc.Col(
                                                    style={
                                                        "display": "flex",
                                                        "box-sizing": "border-box",
                                                        "flexDirection": "column",
                                                        "justifyContent": "center",  # Center content vertically
                                                        "alignItems": "center",  # Center content horizontally
                                                        "height": "100%",
                                                        "flex-basis": "2%",  # Adjusted to a slightly more reasonable width
                                                        "max-width": "2%",  # Adjusted to a slightly more reasonable width
                                                    },
                                                    children=[
                                                        html.Div(
                                                            style={
                                                                'height': '95%',  # Adjust if needed for visual appearance
                                                                'border-right': '1px solid white',  # Keep this at 1px
                                                                # Scale down horizontally
                                                                'transform': 'scaleX(0.5)',
                                                                'transform-origin': 'left',  # Keep the line anchored on the left
                                                                'margin': '0 auto'
                                                            }
                                                        ),
                                                    ]
                                                ),
                                                dbc.Col(
                                                    style={#"padding": "5px",  # "border": "2px dashed yellow",
                                                           "box-sizing": "border-box",
                                                           "backgroundColor": "black", 
                                                           "height": "100%",
                                                        "flex-basis": "39%",  # Adjusted to a slightly more reasonable width
                                                        "max-width": "39%",  # Adjusted to a slightly more reasonable width
                                                           },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            html.Div("Education & Age", style={
                                                                                "textAlign": "center", "fontSize": "14px", "color": "white",
                                                                                'fontFamily': '"Times New Roman", Times, serif'}),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=12
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "10%", "box-sizing": "border-box", }
                                                                ),
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            dcc.Graph(
                                                                                id='chart8_1',
                                                                                # figure=create_education_level_chart(hr),
                                                                                # Adjust height and width as needed
                                                                                style={
                                                                                    "height": "100%", "width": "100%"}
                                                                            ),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=9
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "25%", "box-sizing": "border-box", }
                                                                ),
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            dcc.Graph(
                                                                                id='chart8_2',
                                                                                # figure=create_scatter_plot_with_text(pivot_table),
                                                                                # Adjust height and width as needed
                                                                                style={
                                                                                    "height": "100%", "width": "100%"}
                                                                            ),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=9
                                                                        ),
                                                                        dbc.Col(
                                                                            dcc.Graph(
                                                                                id='chart8_3',
                                                                                # figure=create_age_distribution_chart(hr),
                                                                                # Adjust height and width as needed
                                                                                style={
                                                                                    "height": "100%", "width": "100%"}
                                                                            ),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=3
                                                                        )
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "65%"}
                                                                )
                                                            ],
                                                            style={  # "border": "2px solid green",
                                                                "textAlign": "center", "box-sizing": "border-box",
                                                                "backgroundColor": "black", "height": "100%", "box-sizing": "border-box", }
                                                        )
                                                    ],
                                                    width=4
                                                ),
                                                dbc.Col(
                                                    style={
                                                        "display": "flex",
                                                        "box-sizing": "border-box",
                                                        "flexDirection": "column",
                                                        "justifyContent": "center",  # Center content vertically
                                                        "alignItems": "center",  # Center content horizontally
                                                        "height": "100%",
                                                        "flex-basis": "2%",  # Adjusted to a slightly more reasonable width
                                                        "max-width": "2%",  # Adjusted to a slightly more reasonable width
                                                    },
                                                    children=[
                                                        html.Div(
                                                            style={
                                                                'height': '95%',  # Adjust if needed for visual appearance
                                                                'border-right': '1px solid white',  # Keep this at 1px
                                                                # Scale down horizontally
                                                                'transform': 'scaleX(0.5)',
                                                                'transform-origin': 'left',  # Keep the line anchored on the left
                                                                'margin': '0 auto'
                                                            }
                                                        ),
                                                    ]
                                                ),
                                                dbc.Col(
                                                    style={#"padding": "5px",  # "border": "2px dashed yellow",
                                                           "box-sizing": "border-box",
                                                           #"backgroundColor": "black", 
                                                           "height": "100%"},
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            html.Div("Education & Performance", style={
                                                                                "textAlign": "center", "fontSize": "14px", "color": "white",
                                                                                'fontFamily': '"Times New Roman", Times, serif'}),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=12
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "10%", "box-sizing": "border-box", }
                                                                ),
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            dcc.Graph(
                                                                                id='chart9',
                                                                                # figure=create_scatter_plot_with_text2(pivot_table2, hr),  # Insert the Plotly graph here
                                                                                style={
                                                                                    "height": "100%", "width": "100%", "display": "block"}
                                                                            ),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=12
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "90%", "box-sizing": "border-box", }
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "box-sizing": "border-box", "textAlign": "center", #"backgroundColor": "black", 
                                                                "height": "100%"}
                                                        )
                                                    ],
                                                ),
                                            ]
                                        ),
                                        dbc.Row(
                                            style={
                                                # "border": "2px solid red",
                                                "backgroundColor": "rgb(85, 85, 85)", "height": "20px"},
                                            children=[
                                                dbc.Col(
                                                    style={"padding": "10px",
                                                           # "border": "2px dashed yellow"
                                                           },
                                                )
                                            ]
                                        ),
                                        dbc.Row(
                                            style={
                                                # "border": "2px solid red",
                                                "backgroundColor": "black", "height": "40px",
                                                'border-top-left-radius': '10px', 
                                                'border-top-right-radius': '10px',},
                                            children=[
                                                dbc.Col(
                                                    style={
                                                        "padding": "10px",
                                                        # "border": "2px dashed yellow"
                                                    },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Div("Income", style={
                                                                    "textAlign": "left", "fontSize": "18px", "color": "white",
                                                                    'fontFamily': '"Times New Roman", Times, serif', "fontWeight": "bold", }),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                )
                                            ]
                                        ),
                                        dbc.Row(
                                            style={
                                                #"border": "2px solid purple",
                                                "box-sizing": "border-box",
                                                "flex": "1"},
                                            children=[
                                                dbc.Col(
                                                    style={"padding": "10px",  # "border": "2px dashed yellow",
                                                           "box-sizing": "border-box",
                                                           "backgroundColor": "black", 
                                                           "height": "100%", "flex-basis": "48.5%", "max-width": "48.5%",
                                                           'border-bottom-left-radius': '10px', },
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            html.Div("Education & Gender", style={
                                                                                "textAlign": "center", "fontSize": "14px", "color": "white",
                                                                                'fontFamily': '"Times New Roman", Times, serif'}),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=12
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "10%"}
                                                                ),
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            dcc.Graph(
                                                                                id='chart10',
                                                                                # Insert the Plotly graph here
                                                                                # figure=plot_salary_distribution(hr),
                                                                                style={
                                                                                    "height": "100%", "width": "100%", "display": "block"}
                                                                            ),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=12
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "90%", "box-sizing": "border-box", }
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "box-sizing": "border-box", "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                    width=6
                                                ),
                                                dbc.Col(
                                                    style={
                                                        "display": "flex",
                                                        "box-sizing": "border-box",
                                                        "flexDirection": "column",
                                                        "justifyContent": "center",  # Center content vertically
                                                        "alignItems": "center",  # Center content horizontally
                                                        "height": "100%",
                                                        "backgroundColor": "black",
                                                        "flex-basis": "2%",  # Adjusted to a slightly more reasonable width
                                                        "max-width": "2%",  # Adjusted to a slightly more reasonable width
                                                    },
                                                    children=[
                                                        html.Div(
                                                            style={
                                                                'height': '95%',  # Adjust if needed for visual appearance
                                                                'border-right': '1px solid white',  # Keep this at 1px
                                                                # Scale down horizontally
                                                                'transform': 'scaleX(0.5)',
                                                                'transform-origin': 'left',  # Keep the line anchored on the left
                                                                'margin': '0 auto'
                                                            }
                                                        ),
                                                    ]
                                                ),
                                                dbc.Col(
                                                    style={"padding": "10px", "box-sizing": "border-box",  # "border": "2px dashed yellow",
                                                           "backgroundColor": "black", "height": "100%", "flex-basis": "48.%", "max-width": "48.5%",
                                                           'border-bottom-right-radius': '10px',},
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            html.Div("Age & Salary", style={
                                                                                "textAlign": "center", "fontSize": "14px", "color": "white",
                                                                                'fontFamily': '"Times New Roman", Times, serif'}),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=12
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "10%", "box-sizing": "border-box", }
                                                                ),
                                                                dbc.Row(
                                                                    children=[
                                                                        dbc.Col(
                                                                            dcc.Graph(
                                                                                id='chart11',
                                                                                # Insert the Plotly graph here
                                                                                # figure=create_scatter_plot(hr),
                                                                                style={
                                                                                    "height": "100%", "width": "100%", "display": "block"}
                                                                            ),
                                                                            # Adjust width as needed (50% of the column)
                                                                            width=12
                                                                        ),
                                                                    ],
                                                                    # Ensure the row takes up the full height
                                                                    style={
                                                                        "height": "90%", "box-sizing": "border-box", }
                                                                ),
                                                            ],
                                                            style={
                                                                # "border": "2px solid green",
                                                                "box-sizing": "border-box", "textAlign": "center", "backgroundColor": "black", "height": "100%"}
                                                        )
                                                    ],
                                                    width=6
                                                ),
                                            ]
                                        ),
                                    ],
                                    width=8,
                                ),
                            ],
                        ),
                    ],
                    # width=10,
                ),
            ],
        ),
        # Placeholder for callback
    ],
    fluid=True
)

##################################################################################################
@callback(
    Output('filter_panel', 'style'),
    Input('toggle-button', 'n_clicks'),
    State('filter_panel', 'style')
)
def toggle_filter_panel(n_clicks, current_style):
    if n_clicks:
        if current_style["display"] == "none":
            return {
                "display": "block",
                #"border": "2px dashed yellow",
                "backgroundColor": "rgb(85, 85, 85)",
                "flex-basis": "44%",  # Maintain the width
                "max-width": "44%",  # Maintain the width
                "position": "relative",  # Ensure it doesn't overlap with the button
            }
        else:
            return {
                "display": "none",
                #"border": "2px dashed yellow",
                "backgroundColor": "rgb(85, 85, 85)",
                "flex-basis": "44%",  # Maintain the width
                "max-width": "44%",  # Maintain the width
                "position": "relative",  # Ensure it doesn't overlap with the button
            }
    return current_style



@callback(
    [
        Output('dropdown-menu', 'style'),
        Output('dropdown-menu2', 'style'),
        Output('dropdown-menu3', 'style'),
        Output('dropdown-menu4', 'style'),
        Output('all', 'children'),
        Output('hire-date-count', 'children'),
        Output('hire-date-count2', 'children'),
        Output('chart2_1', 'figure'),
        Output('chart2_2', 'figure'),
        Output('chart4', 'figure'),
        Output('chart5', 'figure'),
        Output('chart6', 'figure'),
        Output('chart7_1', 'figure'),
        Output('chart7_2', 'figure'),
        Output('chart8_1', 'figure'),
        Output('chart8_2', 'figure'),
        Output('chart8_3', 'figure'),
        Output('chart9', 'figure'),
        Output('chart10', 'figure'),
        Output('chart11', 'figure'),
    ],
    [
        Input('dropdown-button', 'n_clicks'),
        Input('dropdown-button2', 'n_clicks'),
        Input('dropdown-button3', 'n_clicks'),
        Input('dropdown-button4', 'n_clicks'),
        Input('gender-dropdown', 'value'),
        Input('status-dropdown', 'value'),
        Input('location-dropdown', 'value'),
        Input('hire-dropdown', 'value'),
    ],
    [State('dropdown-menu', 'style'), State('dropdown-menu2', 'style'),
     State('dropdown-menu3', 'style'), State('dropdown-menu4', 'style')]
)
def update_charts_and_toggle_menu(n_clicks1, n_clicks2, n_clicks3, n_clicks4, selected_genders, selected_status, selected_location, selected_hiredate, current_style1, current_style2, current_style3, current_style4):
    ctx = dash.callback_context

    # Initialize display styles if not already set
    if not current_style1:
        current_style1 = {"display": "none"}
    if not current_style2:
        current_style2 = {"display": "none"}
    if not current_style3:
        current_style3 = {"display": "none"}
    if not current_style4:
        current_style4 = {"display": "none"}

    # Determine which button was clicked
    if not ctx.triggered:
        button_id = 'No clicks yet'
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

    # Toggle only on button clicks, ignoring other inputs
    if button_id == 'dropdown-button':
        current_style1 = {"display": "block"} if current_style1["display"] == "none" else {
            "display": "none"}
    elif button_id == 'dropdown-button2':
        current_style2 = {"display": "block"} if current_style2["display"] == "none" else {
            "display": "none"}
    elif button_id == 'dropdown-button3':
        current_style3 = {"display": "block"} if current_style3["display"] == "none" else {
            "display": "none"}
    elif button_id == 'dropdown-button4':
        current_style4 = {"display": "block"} if current_style4["display"] == "none" else {
            "display": "none"}


    # Apply filters only if specific values are selected
    filtered_hr = hr.copy()
    #print(filtered_hr.head())
    if selected_genders and selected_genders != 'All':
        filtered_hr = filtered_hr[filtered_hr['Gender'].isin(selected_genders)]
    # if selected_genders and selected_genders != ['Female', 'Male']:
    #     filtered_hr = filtered_hr[filtered_hr['Gender'].isin(selected_genders)]
    if selected_status and selected_status != 'All':
        filtered_hr = filtered_hr[filtered_hr['skoncil'].isin(selected_status)]
    if selected_location and selected_location != 'All':
        filtered_hr = filtered_hr[filtered_hr['lokace'].isin(selected_location)]
    if selected_hiredate and selected_hiredate != 'All':
        filtered_hr = filtered_hr[filtered_hr['Hireyear'].isin(
            selected_hiredate)]
    
    #print(f"Selected Genders: {selected_genders}")

    pivot_table = pd.DataFrame({
        'Age_bins': ['<25', '25-34', '35-44', '45-54', '54+'],
        'Bachelor': [576, 1351, 1664, 1280, 545],
        'High School': [166, 437, 583, 446, 187],
        'Master': [116, 296, 409, 290, 126],
        'PhD': [0, 97, 121, 116, 144]
    })
    #print(pivot_table)

    pivot_table2 = pd.DataFrame({
        'Performance Rating': ['Needs Improvement', 'Satisfactory', 'Good', 'Excellent'],
        'High School': [618, 578, 389, 234],
        'Bachelor': [425, 1619, 2706, 666],
        'Master': [57, 238, 504, 438],
        'PhD': [23, 63, 164, 228]
    })

    # Generate charts with the filtered dataset or the original dataset if no filter is applied
    aktivni = filtered_hr['Termdate'].isnull().sum()
    #print(aktivni)
    
    hire_date_count = filtered_hr['Hiredate'].value_counts().sum()
    
    terminated_count = filtered_hr.loc[filtered_hr.skoncil == "ano","skoncil"].shape[0]
    
    

    figure1 = create_hire_trend_figure(
        filtered_hr) if not filtered_hr.empty else {}
    figure2 = create_hire_trend_figure2(
        filtered_hr) if not filtered_hr.empty else {}
    figure3 = plot_department_termination(
        filtered_hr) if not filtered_hr.empty else {}
    figure4 = create_zoomed_map_go(
        filtered_hr) if not filtered_hr.empty else {}
    figure5 = plot_lokace_distribution(
        filtered_hr) if not filtered_hr.empty else {}
    # figure6 = fig_men if not filtered_hr.empty else {}
    # figure7 = fig_women if not filtered_hr.empty else {}
    
    fig_men, fig_women = generate_donut_charts(filtered_hr)

    if selected_genders == ['Male']:
        figure6 = fig_men
        figure7 = create_blank_figure()
    elif selected_genders == ['Female']:
        figure6 = create_blank_figure()
        figure7 = fig_women
    else:
        figure6 = fig_men
        figure7 = fig_women
        
    figure8 = create_education_level_chart(
        filtered_hr) if not filtered_hr.empty else {}
    figure9 = create_scatter_plot_with_text(
        pivot_table) if not filtered_hr.empty else {}
    figure10 = create_age_distribution_chart(
        filtered_hr) if not filtered_hr.empty else {}
    figure11 = create_scatter_plot_with_text2(
        pivot_table2, filtered_hr) if not filtered_hr.empty else {}
    figure12 = plot_salary_distribution(
        filtered_hr) if not filtered_hr.empty else {}
    figure13 = create_scatter_plot(
        filtered_hr) if not filtered_hr.empty else {}

    # Return the updated style for dropdown visibility and the updated figures
    return [
        current_style1,
        current_style2,
        current_style3,
        current_style4,
        f"{aktivni}",
        f"{hire_date_count}",
        f"{terminated_count}",
        figure1,
        figure2,
        figure3,
        figure4,
        figure5,
        figure6,
        figure7,
        figure8,
        figure9,
        figure10,
        figure11,
        figure12,
        figure13
    ]
    
# clientside_callback(
#     """
#     function(n_clicks) {
#         if(n_clicks) {
#             // Use html2canvas to capture screenshot
#             html2canvas(document.querySelector("#app-content")).then(canvas => {
#                 // Convert canvas to data URL
#                 var image = canvas.toDataURL("image/png").replace("image/png", "image/octet-stream");
#                 // Create a temporary download link
#                 var link = document.createElement('a');
#                 link.href = image;
#                 link.download = 'screenshot.png';
#                 document.body.appendChild(link);
#                 link.click();
#                 document.body.removeChild(link);
#             });
#         }
#         return '';
#     }
#     """,
#     Output('download-image-link', 'children'),  # Dummy output, not used
#     Input('download-image', 'n_clicks')
# )    

