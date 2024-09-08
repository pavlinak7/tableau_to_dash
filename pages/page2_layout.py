import dash
import dash_bootstrap_components as dbc
from dash import dash_table
from tableauToDashFunkce import *
from dash.dependencies import Input, Output, State
from dash import dcc, html, callback


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
                dbc.Col(
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
                                                html.Span("Details",
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
                            ]
                        ),
                        dbc.Row(
                            style={
                                "width" : "100%",
                                "height" : "88.5%",
                                "backgroundColor" : "black",
                                "border-radius" : "10px"
                            },
                            children=[
                                dbc.Col(
                                    children=[
                                       dbc.Row(
                                           children=[
                                               dbc.Col(
                                                    html.Div(
                                                        children=[
                                                            html.Div("Employee List",
                                                                     style={
                                                                "textAlign": "left", "fontSize": "18px", "color": "white",
                                                                'fontFamily': '"Times New Roman", Times, serif', "fontWeight": "bold", }),
                                                        ],
                                                        style={
                                                            # "border": "2px solid green",
                                                            "textAlign": "center", #"backgroundColor": "black",
                                                            "height": "100%"}
                                                    ) ,
                                                    style={
                                                        "padding": "10px",
                                                        # "border": "2px dashed yellow"
                                                    },
                                           )
                                           ]
                                       ),
                                       # dbc.Row(
                                       #     style={'height': '30px',
                                       #            #"border": "2px solid purple",
                                       #            },
                                       #     children=[
                                       #          dbc.Col(
                                       #              html.Div(
                                       #                  [
                                       #                      html.Div(
                                       #                          [
                                       #                              html.Span("▸"),
                                       #                              html.Span("ID"),
                                       #
                                       #                          ],
                                       #                         className="S2filter_div",
                                       #                      ),
                                       #                  ],
                                       #                       ),
                                       #              className="S2filter_n",
                                       #          ),
                                       #          dbc.Col( #B2E1sloupecF2
                                       #              html.Div(
                                       #                  "Demographics",
                                       #                  className="S2filter_div",
                                       #                  ),
                                       #              className="S2filter_n",
                                       #          ),
                                       #          dbc.Col( #B2E1sloupecF3
                                       #              html.Div("Role",
                                       #                       className="S2filter_div",
                                       #                       ),
                                       #              className="S2filter_n",
                                       #          ),
                                       #          dbc.Col( #B2E1sloupecF4
                                       #              html.Div("Geographics",
                                       #                       className="S2filter_div",
                                       #                       ),
                                       #              className="S2filter_n",
                                       #          ),
                                       #          dbc.Col( #B2E1sloupecF4
                                       #              html.Div("Salary",
                                       #                       className="S2filter_div",
                                       #                       ),
                                       #              className="S2filter_n",
                                       #          ),
                                       #          dbc.Col( #B2E1sloupecF4
                                       #              html.Div("Status",
                                       #                       className="S2filter_div",
                                       #                       ),
                                       #              className="S2filter_n",
                                       #          ),
                                       #          dbc.Col( #B2E1sloupecF4
                                       #              html.Div("Length of Employment",
                                       #                       className="S2filter_div",
                                       #                       ),
                                       #              className="S2filter_n",
                                       #          ),
                                       #     ]
                                       # ),
                                        dbc.Row(
                                            children=[
                                                html.Div([
                                                    #html.H1("Employee Dashboard", style={'text-align': 'center', 'font-size': '18px'}),

                                                    # Hidden divs to store visibility state
                                                    dcc.Store(id='store-id-visible', data=False),
                                                    dcc.Store(id='store-demographics-visible', data=False),
                                                    dcc.Store(id='store-role-visible', data=False),
                                                    dcc.Store(id='store-geographics-visible', data=False),
                                                    dcc.Store(id='store-salary-visible', data=False),
                                                    dcc.Store(id='store-status-visible', data=False),
                                                    dcc.Store(id='store-length-visible', data=False),

                                                    # Upper row: Titles (ID, Demographics, Role, etc.)
                                                    dbc.Row([
                                                        dbc.Col(html.Div("ID", id="id-title", style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}),
                                                                style={"flex-basis": "8%", "max-width": "8%"}),
                                                        dbc.Col(html.Div("Demographics", id="demographics-title",
                                                                         style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}),
                                                                style={"flex-basis": "13%", "max-width": "13%"}),
                                                        dbc.Col(
                                                            html.Div("Role", id="role-title", style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}),
                                                            style={"flex-basis": "14%", "max-width": "14%"}),
                                                        dbc.Col(html.Div("Geographics", id="geographics-title",
                                                                         style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}),
                                                                style={"flex-basis": "16%", "max-width": "16%"}),
                                                        dbc.Col(html.Div("Salary", id="salary-title",
                                                                         style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}),
                                                                style={"flex-basis": "12%", "max-width": "12%"}),
                                                        dbc.Col(html.Div("Status", id="status-title",
                                                                         style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}),
                                                                style={"flex-basis": "15%", "max-width": "15%"}),
                                                        dbc.Col(html.Div("Length of Employment", id="length-title",
                                                                         style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}),
                                                                style={"flex-basis": "14%", "max-width": "14%"}),
                                                    ], style={'display': 'flex', 'flex-wrap': 'nowrap', 'align-items': 'center', 'gap': '10px', 'margin': '0 auto',
                                                              'width': '100%'}),

                                                    # Lower row: Components (dropdowns, inputs, sliders), initially hidden
                                                    dbc.Row([
                                                        # ID section (hidden by default)
                                                        dbc.Col(html.Div(id="id-content", style={'display': 'none'}, children=[
                                                            dcc.Input(id="input-id", placeholder="ID", type="text", style={'width': '100%', 'font-size': '12px'}),
                                                        ]), style={"flex-basis": "8%", "max-width": "8%"}),

                                                        # Demographics section (hidden by default)
                                                        dbc.Col(html.Div(id="demographics-content", style={'display': 'none'}, children=[
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-name",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-name',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['cele_jmeno'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-name",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-gender",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-gender',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['Gender'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-gender",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-age",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-age',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['Age_bins'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-age",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-education",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-education',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in hr[
                                                                                                 'Education Level'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-education",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ]), style={"flex-basis": "13%", "max-width": "13%"}),

                                                        # Role section (hidden by default)
                                                        dbc.Col(html.Div(id="role-content", style={'display': 'none'}, children=[
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-job",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-job',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['Job Title'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-job",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-department",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-department',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['Department'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-department",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ]), style={"flex-basis": "14%", "max-width": "14%"}),

                                                        # Geographics section (hidden by default)
                                                        dbc.Col(html.Div(id="geographics-content", style={'display': 'none'}, children=[
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-location",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-location',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['lokace'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-location",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-state",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-state',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['State'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-state",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-city",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-city',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['City'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-city",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ]), style={"flex-basis": "16%", "max-width": "16%"}),
                                                        # Salary section (hidden by default)
                                                        dbc.Col(html.Div(id="salary-content", style={'display': 'none'},
                                                                         children=[
                                                                             dcc.RangeSlider(
                                                                                 id="input-salary",
                                                                                 min=hr['Salary'].min(),
                                                                                 max=hr['Salary'].max(),
                                                                                 marks={
                                                                                     int(hr[
                                                                                             'Salary'].min()): f"${int(hr['Salary'].min()):,}",
                                                                                     # Only min and max marks
                                                                                     int(hr[
                                                                                             'Salary'].max()): f"${int(hr['Salary'].max()):,}"
                                                                                 },
                                                                                 step=5000,
                                                                                 value=[int(hr['Salary'].min()),
                                                                                        int(hr['Salary'].max())],
                                                                                 # Two-element list for min and max only
                                                                                 tooltip={"placement": "bottom",
                                                                                          "always_visible": False},
                                                                                 # Tooltip off
                                                                                 allowCross=False,
                                                                             )
                                                                         ]),
                                                                style={"flex-basis": "12%", "max-width": "12%"}),
                                                        # Status section (hidden by default)
                                                        dbc.Col(html.Div(id="status-content", style={'display': 'none'}, children=[
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-status",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-status',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['skoncil'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-status",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-hire-year",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-year-hire',
                                                                                    options=[{'label': i, 'value': i}
                                                                                             for i in
                                                                                             hr['Hiredate'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-hire-year",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                            dbc.Row(
                                                                className="dropdown-row",
                                                                children=[
                                                                    dbc.Col(
                                                                        children=[
                                                                            html.Button(
                                                                                [
                                                                                    "(All)",
                                                                                    html.Span(
                                                                                        className="dropdown-arrow")
                                                                                ],
                                                                                id="dropdown-button-termination-year",
                                                                                className="dropdown-button",
                                                                                style={"border": "1px solid white"},
                                                                            ),
                                                                            html.Div(
                                                                                dcc.Checklist(
                                                                                    id='input-year-term',
                                                                                    options=[{'label': str(i),
                                                                                              'value': i} if pd.notnull(
                                                                                        i) else {'label': 'N/A',
                                                                                                 'value': 'N/A'} for i
                                                                                             in
                                                                                             hr['Termdate'].unique()],
                                                                                    labelStyle={'display': 'block'},
                                                                                    inputStyle={'margin-right': '5px',
                                                                                                'transform': 'scale(1.2)'},
                                                                                    style={
                                                                                        'backgroundColor': 'rgb(85, 85, 85)',
                                                                                        'font-size': '10px',
                                                                                        'padding': '5px',
                                                                                        'color': 'white',
                                                                                    }
                                                                                ),
                                                                                id="dropdown-menu-termination-year",
                                                                                className="dropdown-menu",
                                                                                style={"display": "none"}
                                                                                # Initially hidden
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            ),
                                                        ]), style={"flex-basis": "15%", "max-width": "15%"}),

                                                        # Length of Employment section (hidden by default)
                                                        dbc.Col(html.Div(id="length-content", style={'display': 'none'},
                                                                         children=[
                                                                             dcc.RangeSlider(
                                                                                 id="input-length",
                                                                                 min=0,
                                                                                 # Minimum value for years (0 years)
                                                                                 max=int(hr['delka_prac_pomeru'].max()),
                                                                                 # Maximum years from your dataset
                                                                                 marks={
                                                                                     0: "0",
                                                                                     # Only show marks for start (0 years)
                                                                                     int(hr[
                                                                                             'delka_prac_pomeru'].max()): f"{int(hr['delka_prac_pomeru'].max())}"
                                                                                     # And end values (max years)
                                                                                 },
                                                                                 step=1,  # Step of 1 year
                                                                                 value=[0, int(
                                                                                     hr['delka_prac_pomeru'].max())],
                                                                                 # Initial value (from min to max)
                                                                                 tooltip={"placement": "bottom",
                                                                                          "always_visible": False},
                                                                                 # Tooltip off for a cleaner look
                                                                                 allowCross=False,
                                                                             )
                                                                         ]),
                                                                style={"flex-basis": "15%", "max-width": "15%"}),

                                                    ], style={'display': 'flex', 'flex-wrap': 'nowrap', 'align-items': 'flex-start', 'gap': '10px', 'margin': '0 auto',
                                                              'width': '100%'}),

                                                    html.Div(id="output", style={'margin-top': '20px'})
                                                ])
                                            ],
                                        ),
                                       dbc.Row(
                                           style={
                                              "height" : "450px",
                                              "backgroundColor" : "#2a2b2b",
                                               },
                                           children=[
                                               dbc.Col(
                                                    dash_table.DataTable(
                                                        id='datatable',
                                                        columns=[
                                                            {'name': 'Employee ID', 'id': 'Employee_ID'},
                                                            {'name': 'personal_info', 'id': 'personal_info', 'presentation': 'markdown'},
                                                            {
                                                                'name': 'Job Info',
                                                                'id': 'Job Info',
                                                                'presentation': 'markdown'
                                                            },
                                                            {'name': 'bydliste', 'id': 'bydliste', 'presentation': 'markdown'},
                                                            {'name': 'Salary2', 'id': 'Salary2'},
                                                            {'name': 'pracovni_pomer', 'id': 'pracovni_pomer', 'presentation': 'markdown'},
                                                            {'name': 'delka_prac_pomeru_text', 'id': 'delka_prac_pomeru_text'},
                                                        ],
                                                        data=hrv.to_dict('records'),
                                                        fixed_rows={'headers': True},  # This will freeze the header row
                                                        style_data_conditional=[
                                                            {
                                                                'if': {'column_id': 'Job_Info'},
                                                                'whiteSpace': 'normal',
                                                                'height': 'auto',
                                                            },
                                                            {
                                                                'if': {'column_id': 'pracovni_pomer'},
                                                                'whiteSpace': 'normal',
                                                                'height': 'auto',
                                                            },
                                                        ],
                                                        style_table={
                                                        'min-height': '450px',
                                                        'height': '450px',
                                                            'overflowY': 'auto',
                                                            'overflowX': 'auto',
                                                            'backgroundColor': 'rgba(255, 255, 255, 0)',  # Transparent table background
                                                        },
                                                            style_cell={
                                                                'backgroundColor': 'rgba(255, 255, 255, 0)',  # Transparent cell background
                                                                #'border': '1px solid black',  # Border color (optional)
                                                                'color': 'white',
                                                                'fontSize': '12px',
                                                                'border-bottom': '1px solid black',  # Keep only the bottom border (row lines)
                                                                'border-left': 'none',  # No left border (remove column lines)
                                                                'border-right': 'none',  # No right border (remove column lines)
                                                                'border-top': 'none',  # No top border (remove column lines)
                                                                'textAlign': 'left',
                                                                # 'transform': 'scaleY(0.5)',  # Scale the border to make it thinner
                                                                # 'transform-origin': 'bottom',  # Ensure scaling affects only the bottom part
                                                            },
                                                        # style_header={
                                                        #     'display': 'none',  # Hide the header
                                                        #     'min-height': '0px',  # Remove any space reserved for the header
                                                        #     'height': '0px',  # Ensures no space is taken up
                                                        #     'padding': '0px',  # Remove padding to eliminate extra space
                                                        #     'margin': '0px',  # Remove margin for any remaining spacing
                                                        # },
                                                        style_cell_conditional=[
                                                            {
                                                                'if': {'column_id': 'Employee_ID'},
                                                                'width': '90px',  # Exact width for Employee ID column
                                                                #'textAlign': 'left',
                                                            },
                                                            {
                                                                'if': {'column_id': 'personal_info'},
                                                                'width': '200px'  # Exact width for personal_info column
                                                            },
                                                            {
                                                                'if': {'column_id': 'Job Info'},
                                                                'width': '150px',  # Exact width for Job Info column
                                                            },
                                                            {
                                                                'if': {'column_id': 'bydliste'},
                                                                'width': '200px'  # Exact width for bydliste column
                                                            },
                                                            {
                                                                'if': {'column_id': 'Salary2'},
                                                                'width': '150px'  # Exact width for Salary column
                                                            },
                                                            {
                                                                'if': {'column_id': 'pracovni_pomer'},
                                                                'width': '210px'  # Exact width for pracovni_pomer column
                                                            },
                                                            {
                                                                'if': {'column_id': 'delka_prac_pomeru_text'},
                                                                'width': '190px'  # Exact width for delka_prac_pomeru_text column
                                                            }
                                                        ],
                                                        markdown_options={"html": True}
                                                    )                                               ,
                                                                                              style={
                                              "height" : "100%",
                                               },
                                               )
                                           ]
                                           ),
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ],
        ),
        # Placeholder for callback
    ],
    fluid=True
)






@callback(
    Output('id-content', 'style'),
    [Input('id-title', 'n_clicks')],
    [State('id-content', 'style')]
)
def toggle_id(n_clicks, current_style):
    if n_clicks is None:
        return {'display': 'none'}
    if current_style['display'] == 'none':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    Output('demographics-content', 'style'),
    [Input('demographics-title', 'n_clicks')],
    [State('demographics-content', 'style')]
)
def toggle_demographics(n_clicks, current_style):
    if n_clicks is None:
        return {'display': 'none'}
    if current_style['display'] == 'none':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    Output('role-content', 'style'),
    [Input('role-title', 'n_clicks')],
    [State('role-content', 'style')]
)
def toggle_role(n_clicks, current_style):
    if n_clicks is None:
        return {'display': 'none'}
    if current_style['display'] == 'none':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    Output('geographics-content', 'style'),
    [Input('geographics-title', 'n_clicks')],
    [State('geographics-content', 'style')]
)
def toggle_geographics(n_clicks, current_style):
    if n_clicks is None:
        return {'display': 'none'}
    if current_style['display'] == 'none':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    Output('salary-content', 'style'),
    [Input('salary-title', 'n_clicks')],
    [State('salary-content', 'style')]
)
def toggle_salary(n_clicks, current_style):
    if n_clicks is None:
        return {'display': 'none'}
    if current_style['display'] == 'none':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    Output('status-content', 'style'),
    [Input('status-title', 'n_clicks')],
    [State('status-content', 'style')]
)
def toggle_status(n_clicks, current_style):
    if n_clicks is None:
        return {'display': 'none'}
    if current_style['display'] == 'none':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    Output('length-content', 'style'),
    [Input('length-title', 'n_clicks')],
    [State('length-content', 'style')]
)
def toggle_length(n_clicks, current_style):
    if n_clicks is None:
        return {'display': 'none'}
    if current_style['display'] == 'none':
        return {'display': 'block'}
    else:
        return {'display': 'none'}


@callback(
    [
        Output('dropdown-menu-gender', 'style'),
        Output('dropdown-menu-age', 'style'),
        Output('dropdown-menu-education', 'style'),
        Output('dropdown-menu-job', 'style'),
        Output('dropdown-menu-department', 'style'),
        Output('dropdown-menu-location', 'style'),
        Output('dropdown-menu-state', 'style'),
        Output('dropdown-menu-city', 'style'),
        Output('dropdown-menu-status', 'style'),
        Output('dropdown-menu-hire-year', 'style'),
        Output('dropdown-menu-termination-year', 'style'),
        Output('dropdown-menu-name', 'style'),
        Output('datatable', 'data')
    ],
    [
        Input('dropdown-button-gender', 'n_clicks'),
        Input('dropdown-button-age', 'n_clicks'),
        Input('dropdown-button-education', 'n_clicks'),
        Input('dropdown-button-job', 'n_clicks'),
        Input('dropdown-button-department', 'n_clicks'),
        Input('dropdown-button-location', 'n_clicks'),
        Input('dropdown-button-state', 'n_clicks'),
        Input('dropdown-button-city', 'n_clicks'),
        Input('dropdown-button-status', 'n_clicks'),
        Input('dropdown-button-hire-year', 'n_clicks'),
        Input('dropdown-button-termination-year', 'n_clicks'),
        Input('dropdown-button-name', 'n_clicks'),  # New input for name dropdown
        Input('input-id', 'value'),
        Input('input-name', 'value'),
        Input('input-gender', 'value'),
        Input('input-age', 'value'),
        Input('input-education', 'value'),
        Input('input-job', 'value'),
        Input('input-department', 'value'),
        Input('input-location', 'value'),
        Input('input-state', 'value'),
        Input('input-city', 'value'),
        Input('input-salary', 'value'),  # Salary slider input
        Input('input-status', 'value'),
        Input('input-year-hire', 'value'),
        Input('input-year-term', 'value'),
        Input('input-length', 'value')  # Length of employment slider input
    ],
    [
        State('dropdown-menu-gender', 'style'),
        State('dropdown-menu-age', 'style'),
        State('dropdown-menu-education', 'style'),
        State('dropdown-menu-job', 'style'),
        State('dropdown-menu-department', 'style'),
        State('dropdown-menu-location', 'style'),
        State('dropdown-menu-state', 'style'),
        State('dropdown-menu-city', 'style'),
        State('dropdown-menu-status', 'style'),
        State('dropdown-menu-hire-year', 'style'),
        State('dropdown-menu-termination-year', 'style'),
        State('dropdown-menu-name', 'style')  # New state for name dropdown
    ]
)
def update_table_and_toggle_menus(n_clicks_gender, n_clicks_age, n_clicks_education, n_clicks_job, n_clicks_department,
                                  n_clicks_location, n_clicks_state, n_clicks_city, n_clicks_status, n_clicks_hire_year,
                                  n_clicks_term_year, n_clicks_name, id_value, name_values, gender_values, age_values,
                                  education_values, job_values, department_values, location_values, state_values,
                                  city_values, salary_values, status_values, hire_year_values, term_year_values,
                                  length_values, current_style_gender, current_style_age, current_style_education,
                                  current_style_job, current_style_department, current_style_location,
                                  current_style_state,
                                  current_style_city, current_style_status, current_style_hire_year,
                                  current_style_term_year, current_style_name):
    ctx = dash.callback_context

    # Initialize updated styles with current styles to preserve state
    updated_style_gender = current_style_gender
    updated_style_age = current_style_age
    updated_style_education = current_style_education
    updated_style_job = current_style_job
    updated_style_department = current_style_department
    updated_style_location = current_style_location
    updated_style_state = current_style_state
    updated_style_city = current_style_city
    updated_style_status = current_style_status
    updated_style_hire_year = current_style_hire_year
    updated_style_term_year = current_style_term_year
    updated_style_name = current_style_name  # For name dropdown

    # Toggle the visibility of the corresponding dropdown menu based on which button was clicked
    if ctx.triggered:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        if button_id == 'dropdown-button-gender':
            updated_style_gender = {"display": "block"} if current_style_gender["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-age':
            updated_style_age = {"display": "block"} if current_style_age["display"] == "none" else {"display": "none"}
        elif button_id == 'dropdown-button-education':
            updated_style_education = {"display": "block"} if current_style_education["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-job':
            updated_style_job = {"display": "block"} if current_style_job["display"] == "none" else {"display": "none"}
        elif button_id == 'dropdown-button-department':
            updated_style_department = {"display": "block"} if current_style_department["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-location':
            updated_style_location = {"display": "block"} if current_style_location["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-state':
            updated_style_state = {"display": "block"} if current_style_state["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-city':
            updated_style_city = {"display": "block"} if current_style_city["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-status':
            updated_style_status = {"display": "block"} if current_style_status["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-hire-year':
            updated_style_hire_year = {"display": "block"} if current_style_hire_year["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-termination-year':
            updated_style_term_year = {"display": "block"} if current_style_term_year["display"] == "none" else {
                "display": "none"}
        elif button_id == 'dropdown-button-name':  # New toggle for name dropdown
            updated_style_name = {"display": "block"} if current_style_name["display"] == "none" else {
                "display": "none"}

    # Apply the filters based on user input (same filtering logic as before)
    filtered_data = hr

    if id_value:
        filtered_data = filtered_data[filtered_data['Employee_ID'].str.contains(id_value)]
    if name_values:  # Apply name filter
        filtered_data = filtered_data[filtered_data['cele_jmeno'].isin(name_values)]
    if gender_values:
        filtered_data = filtered_data[filtered_data['Gender'].isin(gender_values)]
    if age_values:
        filtered_data = filtered_data[filtered_data['Age_bins'].isin(age_values)]
    if education_values:
        filtered_data = filtered_data[filtered_data['Education Level'].isin(education_values)]
    if job_values:
        filtered_data = filtered_data[filtered_data['Job Title'].isin(job_values)]
    if department_values:
        filtered_data = filtered_data[filtered_data['Department'].isin(department_values)]
    if location_values:
        filtered_data = filtered_data[filtered_data['lokace'].isin(location_values)]
    if state_values:
        filtered_data = filtered_data[filtered_data['State'].isin(state_values)]
    if city_values:
        filtered_data = filtered_data[filtered_data['City'].isin(city_values)]

    # Handle salary filtering
    if salary_values:
        filtered_data['Salary2_int'] = filtered_data['Salary2'].replace({r'\$': '', ',': ''}, regex=True).astype(int)
        filtered_data = filtered_data[
            (filtered_data['Salary2_int'] >= salary_values[0]) &
            (filtered_data['Salary2_int'] <= salary_values[1])
            ]

    # Handle length of employment filtering
    if length_values:
        filtered_data['Length_int'] = filtered_data['delka_prac_pomeru_text'].str.extract(r'(\d+)').astype(int)
        filtered_data = filtered_data[
            (filtered_data['Length_int'] >= length_values[0]) &
            (filtered_data['Length_int'] <= length_values[1])
            ]

    if status_values:
        filtered_data = filtered_data[filtered_data['skoncil'].isin(status_values)]
    if hire_year_values:
        filtered_data = filtered_data[filtered_data['Hiredate'].isin(hire_year_values)]
    if term_year_values:
        if 'N/A' in term_year_values:
            filtered_data = filtered_data[filtered_data['Termdate'].isna()]
        else:
            filtered_data = filtered_data[filtered_data['Termdate'].isin(term_year_values)]

    # Filtered data for the table
    filtered_data = filtered_data.loc[:, [
                                             "Employee_ID", "personal_info", "Job Info", "bydliste", "Salary2",
                                             "pracovni_pomer", "delka_prac_pomeru_text"
                                         ]]

    return updated_style_gender, updated_style_age, updated_style_education, updated_style_job, updated_style_department, \
        updated_style_location, updated_style_state, updated_style_city, updated_style_status, updated_style_hire_year, \
        updated_style_term_year, updated_style_name, filtered_data.to_dict('records')








