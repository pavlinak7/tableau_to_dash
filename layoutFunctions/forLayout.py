import dash_bootstrap_components as dbc
from dash import dcc, html
from dash import dash_table
from dataFunctions.dataplotting import *

aktivni = hr['Termdate'].isnull().sum()

pivot_table = pd.DataFrame({
    'Age_bins': ['<25', '25-34', '35-44', '45-54', '54+'],
    'Bachelor': [576, 1351, 1664, 1280, 545],
    'High School': [166, 437, 583, 446, 187],
    'Master': [116, 296, 409, 290, 126],
    'PhD': [0, 97, 121, 116, 144]
})

pivot_table2 = pd.DataFrame({
    'Performance Rating': ['Needs Improvement', 'Satisfactory', 'Good', 'Excellent'],
    'High School': [618, 578, 389, 234],
    'Bachelor': [425, 1619, 2706, 666],
    'Master': [57, 238, 504, 438],
    'PhD': [23, 63, 164, 228]
})

def create_icon_postranniho_panelu(obrazek, mezera_pod_ikonou="0px", vyska_radku="50px", odkaz=None, cil=None):
    return dbc.Row(
        className="S1R1S1R1p",
        style={"margin-bottom": mezera_pod_ikonou,
               "height": vyska_radku
               },
        children=[
            dbc.Col(
                className="S1R1S1R1S1p",
                   children = [
                       html.Div(
                           className="B1E1div",
                           children=[
                                dcc.Link(
                                    html.Img(
                                        src=obrazek,
                                        className="B1E1obr",
                                    ),
                                    href=odkaz,
                                    target=cil
                                ) if odkaz else html.Img(
                                                    src=obrazek,
                                                    className="B1E1obr",
                                                )
                               ]
                       )
                ]
            )
        ]
    )


def create_text_postranniho_panelu(text, vyska_radku="30px",mezera_pod_ikonou="0px"):
    return dbc.Row(
        className="S1R1S1R1p",
        style={"margin-bottom": mezera_pod_ikonou,
               "height": vyska_radku
               },
        children=[
            dbc.Col(
                className="S1R1S1R1S1p",
                children = [
                   html.Div(
                       text,
                       style={
                           "textAlign": "center", "fontSize": "9px", "color": "white"},
                       className="B1E1div",
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
                ]
            )
        ]
    )


def create_filter_row1():
    return dbc.Row(  # S2R1S1R1S2R1S1R1
    className="S2R1S1R1S2R1S1R1",
    children=[
        dbc.Col(  # S2R1S1R1S2R1S1R1S1
            className="S2R1S1R1S2R1S1R1S1",
            children=[
                html.Div(
                    "Gender",
                    className="B2E1F1div",
                ),
            ]
        ),
        dbc.Col(  # S2R1S1R1S2R1S1R1S1
            className="S2R1S1R1S2R1S1R1S1",
            children=[
                html.Div(
                    "Status",
                    className="B2E1F1div",
                ),
            ]
        ),
        dbc.Col(  # S2R1S1R1S2R1S1R1S1
            className="S2R1S1R1S2R1S1R1S1",
            children=[
                html.Div(
                    "Location",
                    className="B2E1F1div",
                ),
            ]
        ),
        dbc.Col(  # S2R1S1R1S2R1S1R1S1
            className="S2R1S1R1S2R1S1R1S1",
            children=[
                html.Div(
                    "Hiredate",
                    className="B2E1F1div",
                ),
            ]
        )
    ]
    )

dropdown_data = {
    "gender": {
        "button_id": "dropdown-button",
        "div_id": "dropdown-menu",
        "checklist_id": "gender-dropdown",
        "options": [
            {'label': 'Female', 'value': 'Female'},
            {'label': 'Male', 'value': 'Male'}
        ]
    },
    "status": {
        "button_id": "dropdown-button2",
        "div_id": "dropdown-menu2",
        "checklist_id": "status-dropdown",
        "options": [
            {'label': 'ne', 'value': 'ne'},
            {'label': 'ano', 'value': 'ano'}
        ]
    },
    "location": {
        "button_id": "dropdown-button3",
        "div_id": "dropdown-menu3",
        "checklist_id": "location-dropdown",
        "options": [
            {'label': 'HQ', 'value': 'HQ'},
            {'label': 'Branch', 'value': 'Branch'}
        ]
    },
    "hiredate": {
        "button_id": "dropdown-button4",
        "div_id": "dropdown-menu4",
        "checklist_id": "hire-dropdown",
        "options": [
            {'label': '2015', 'value': 2015},
            {'label': '2016', 'value': 2016},
            {'label': '2017', 'value': 2017},
            {'label': '2018', 'value': 2018},
            {'label': '2019', 'value': 2019},
            {'label': '2020', 'value': 2020},
            {'label': '2021', 'value': 2021},
            {'label': '2022', 'value': 2022},
            {'label': '2023', 'value': 2023},
            {'label': '2024', 'value': 2024}
        ]
    }
}

def create_filter_dropdown(button_id, div_id, checklist_id, moznosti):
    return dbc.Col(  # S2R1S1R1S2R1S1R2S1
            className="S2R1S1R1S2R1S1R1S1",
            children=[
                html.Button(
                    [
                        "(All)",
                        html.Span(
                            className="dropdown-arrow")
                    ],
                    id=button_id,
                    className="dropdown-button",
                    style={
                        "border": "1px solid white",
                    },
                ),
                html.Div(
                    dcc.Checklist(
                        id=checklist_id,
                        options=moznosti,
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
                    id=div_id,
                    className="dropdown-menu",
                    style={
                        "display": "none", # Initially hidden
                    }
                )
            ]
        )

def create_nadpis_sekci(text):
    return dbc.Row( #S2R2S2R1S1R1S1R1
                className="S2R2S1R1S1R1",
                children=[
                    dbc.Col( #S2R2S2R1S1R1S1R1S1
                        className="S2R2S1R1S1R1S1",
                        children=[
                            html.Div(
                                className="S2R2S1R1S1R1S1div",
                                children=[
                                    html.Div(text,
                                             className="S2R2S1R1S1R1S1text"
                                             ),
                                ],
                            )
                        ],
                    )
                ]
            )

def create_nadpis_podsekce(text):
    return dbc.Row(  # S2R2S1R1S1R6
    className="S2R2S1R1S1R4",
    children=[
        dbc.Col(
            className="S2R2S1R1S1R1S2",
            children=[
                html.Div(  # B2D4F5divG1
                    className="S2R2S1R1S1R1S2div",
                    children=[
                        html.Span(
                            style={
                                'flex': 1,
                                'border-bottom': '1px solid gray',
                            }
                        ),
                        html.Span(text,
                                  style={
                                      'padding': '0 10px',
                                      'color': 'white',
                                      'fontFamily': '"Times New Roman", Times, serif',
                                  }
                                  ),
                        html.Span(
                            style={
                                'flex': 1,
                                'border-bottom': '1px solid gray',
                            }
                        )
                    ],
                ),
            ],
        )
    ]
)

def create_nadpis_grafu(text, font_size="14px", color="white"):
    return dbc.Row(
        className="S2R2S2R2S1R1S1R2S1R1",
        children=[
            dbc.Col(
                className="S2R2S1R1S1R1S1",
                children=[
                    html.Div(
                        text,
                        style={
                            "textAlign": "center",
                            "fontSize": font_size,
                            "color": color,
                            'fontFamily': '"Times New Roman", Times, serif'
                        }
                    ),
                ]
            ),
        ],
    )


def create_nadpis_a_cislo(text, ident, vyska_radku, okraj=None, vyska_mezery="0px", include_last_div=True):
    margin_style = {"margin": okraj, "height": vyska_radku} if okraj is not None else {"height": vyska_radku}

    children_divs = [
        html.Div(
            text,
            className="S2R2S1R1S1R1S1textin"
        ),
        html.Div(
            id=ident,
            className="B2D4divG3",
            #style={"marginBottom": vyska_mezery}
        ),
    ]

    # Conditionally add the last div based on include_last_div
    if include_last_div:
        children_divs.append(
            html.Div(  # B2D4divG4
                className="B2D4divG4",
            )
        )

    return dbc.Row(  # S2R2S2R1S1R1S1R1
        className="S2R2S1R1S1R1in",
        style=margin_style,
        children=[
            dbc.Col(  # S2R2S2R1S1R1S1R1S1
                className="S2R2S1R1S1R1S1",
                children=[
                    html.Div(
                        className="S2R2S1R1S1R1S1div",
                        children=children_divs,
                    )
                ],
            )
        ]
    )

def create_graph_box(graf_id, vyska="100%", sirka="100%", vyska_radku="100%", sirka_sloupce="0 0 100%"):
    return dbc.Row(  # S2R2S2R1S1R1S1R2S1R2
        className="S2R2S2R1S1R1S1R2S1R2grafy",
        style={"height": vyska_radku,
              },
        children=[
            dbc.Col(
                className="S2R2S1R1S1R1S1graf",
                style={"flex": sirka_sloupce,
                       },
                children=[
                dcc.Graph(
                    #figure=graf,
                    figure={},
                    id=graf_id,
                    style={
                        #"border": "2px solid green",
                        "height": vyska,
                        "width": sirka,
                        "display": "block",
                    }
                ),
                ]
            )
        ],
    )

def create_vertical_divider():
    return dbc.Col(
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
            )

def create_dropdown_druha_strana(button_id, checklist_id, promenna, div_id, custom, options_list=None):
    options = options_list if options_list else [{'label': i, 'value': i} for i in sorted(hr[promenna].unique())]
    return dbc.Row( #S2R2S1R2R2S2R1
        className="dropdown-row",
        children=[
            dbc.Col( #S2R2S1R2R2S2R1S1
                children=[
                    html.Button(
                        [
                            custom,
                            html.Span(
                                className="dropdown-arrow_strana2")
                        ],
                        id=button_id,
                        className="dropdown-button_strana2",
                        style={"border": "1px solid white"},
                    ),
                    html.Div( #S2R2S1R2R2S2R1S1div
                        dcc.Checklist(
                            id=checklist_id,
                            options=options,
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
                        id=div_id,
                        className="dropdown-menu_strana2",
                        style={"display": "none"}
                    )
                ]
            )
        ]
    )

def create_table():
    return dash_table.DataTable(
        id='datatable',
        columns=[
            {'name': 'Employee ID', 'id': 'Employee_ID'},
            {'name': 'personal_info', 'id': 'personal_info', 'presentation': 'markdown'},
            {'name': 'Job Info', 'id': 'Job Info', 'presentation': 'markdown'},
            {'name': 'bydliste', 'id': 'bydliste', 'presentation': 'markdown'},
            {'name': 'Salary2', 'id': 'Salary2'},
            {'name': 'pracovni_pomer', 'id': 'pracovni_pomer', 'presentation': 'markdown'},
            {'name': 'delka_prac_pomeru_text', 'id': 'delka_prac_pomeru_text'},
        ],
        data=hrv.to_dict('records'),
        # fixed_rows={'headers': True},  # Commented out since there's no header
        style_header={
            #'display': 'none',  # Add this line to remove the header
            'backgroundColor': 'black',
            'color': 'black',
        },
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
            'color': 'white',
            'fontSize': '12px',
            'border-bottom': '1px solid black',  # Keep only the bottom border (row lines)
            'border-left': 'none',  # No left border (remove column lines)
            'border-right': 'none',  # No right border (remove column lines)
            'border-top': 'none',  # No top border (remove column lines)
            'textAlign': 'left',
        },
        style_cell_conditional=[
            {
                'if': {'column_id': 'Employee_ID'},
                'width': '90px',
            },
            {
                'if': {'column_id': 'personal_info'},
                'width': '200px'
            },
            {
                'if': {'column_id': 'Job Info'},
                'width': '150px',
            },
            {
                'if': {'column_id': 'bydliste'},
                'width': '200px'
            },
            {
                'if': {'column_id': 'Salary2'},
                'width': '150px'
            },
            {
                'if': {'column_id': 'pracovni_pomer'},
                'width': '210px'
            },
            {
                'if': {'column_id': 'delka_prac_pomeru_text'},
                'width': '190px'
            }
        ],
        markdown_options={"html": True}
    )


