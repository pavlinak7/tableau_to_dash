from plotly.subplots import make_subplots
import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, dash_table
from tableauToDashFunkce import *
import dash_ag_grid as dag


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
                                       dbc.Row(
                                           style={
                                              "height" : "500px", 
                                              "backgroundColor" : "#2a2b2b",
                                               },
                                           children=[
                                               dbc.Col(
    # dag.AgGrid(
    #     id='ag-grid',
    #     columnDefs=[
    #         {'headerName': 'Employee ID', 'field': 'Employee_ID'},
    #         {'headerName': 'Name', 'field': 'cele_jmeno'},
    #         {
    #             'headerName': 'Job Info',
    #             'field': 'Job_Info',
    #             'cellRenderer': 'function(params) { return params.value ? params.value : ""; }'
    #         },
    #         {'headerName': 'City', 'field': 'City'},
    #         {'headerName': 'Salary', 'field': 'Salary'},
    #         {'headerName': 'Finished', 'field': 'skoncil'}
    #     ],
    #     rowData=hrv.to_dict('records'),
    #     dangerously_allow_code=True, 
    #     defaultColDef={'flex': 1, 'sortable': True, 'filter': True},
    #     style={'height': '600px', 'width': '100%'},
    #     className="ag-theme-alpine-dark",
        
    # )
 
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
        'height': '400px',
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
)                                                 
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





