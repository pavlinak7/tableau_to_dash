import dash
from dash import callback
from dash.dependencies import Input, Output, State
from layoutFunctions.forLayout import *



dash.register_page(__name__, path='/')

layout = dbc.Container(
    [
    dbc.Row(  # radek1
        className="radek1",
        children=[
            # postranní panel
            dbc.Col(  # oblastB sloupecS1
                className="oblastB sloupecS1",
                children=[
                    dbc.Row( #S1R1
                        className="S1R1",
                        children=[
                            dbc.Col( #S1R1S1
                                className="S1R1S1",
                                children=[
                                    create_icon_postranniho_panelu("/assets/Logo.png", "72px"),
                                    create_icon_postranniho_panelu("/assets/dashboard-summary-active.png", odkaz="/"),
                                    create_icon_postranniho_panelu("/assets/dashboard-records-inactive.png", "60px", odkaz="/page-2"),
                                    create_text_postranniho_panelu("Info", mezera_pod_ikonou="0px"),
                                    create_icon_postranniho_panelu("/assets/info-hidden.png", "60px"),
                                    create_text_postranniho_panelu("Export", mezera_pod_ikonou="0px"),
                                    create_icon_postranniho_panelu("/assets/download pdf.png"),
                                    create_icon_postranniho_panelu("/assets/download image.png", "50px"),
                                    create_text_postranniho_panelu("Follow", mezera_pod_ikonou="0px"),
                                    create_icon_postranniho_panelu("/assets/contact-channel.png", odkaz="https://www.youtube.com/watch?v=UcGF09Awm4Y&t=1497s", cil="_blank"),
                                    create_icon_postranniho_panelu("/assets/contact-linkedin.png", odkaz="https://www.linkedin.com/in/pavlina-kurkova-a30939109", cil="_blank"),
                                ]
                            )
                        ]
                    )
                ]
            ),
            # hlavní část
            dbc.Col(  # oblastB sloupecS2
                className="oblastB sloupecS2",
                children=[
                    dbc.Row( #S2R1 - nadpis, filtr
                        className="S2R1",
                        style={
                            "height": "9%"
                        },
                        children=[
                            dbc.Col( #S2R1S1
                                className="S2R1S1",
                                children=[
                                    dbc.Row( #S2R1S1R1
                                        className="S2R1S1R1",
                                        children=[
                                            dbc.Col( #S2R1S1R1S1
                                            className="S2R1S1R1S1",
                                            children=[
                                                html.Div(  #S2R1S1R1S1div
                                                    className="S2R1S1R1S1div",
                                                    children=[
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
                                                )
                                            ],
                                            ),
                                            dbc.Col( #S2R1S1R1S2 filter
                                                className="S2R1S1R1S2",
                                                children=[
                                                    dbc.Row( #S2R1S1R1S2R1
                                                        className="S2R1S1R1S2R1",
                                                        children=[
                                                            dbc.Col( #S2R1S1R1S2R1S1
                                                                className="S2R1S1R1S2R1S1",
                                                                id = "filter_panel",
                                                                children=[
                                                                    create_filter_row1(),
                                                                    dbc.Row(  # S2R1S1R1S2R1S1R2
                                                                        className="S2R1S1R1S2R1S1R2",
                                                                        children=[
                                                                            create_filter_dropdown(
                                                                                dropdown_data["gender"]["button_id"],
                                                                                dropdown_data["gender"]["div_id"],
                                                                                dropdown_data["gender"]["checklist_id"],
                                                                                dropdown_data["gender"]["options"]),
                                                                            create_filter_dropdown(
                                                                                dropdown_data["status"]["button_id"],
                                                                                dropdown_data["status"]["div_id"],
                                                                                dropdown_data["status"]["checklist_id"],
                                                                                dropdown_data["status"]["options"]),
                                                                            create_filter_dropdown(
                                                                                dropdown_data["location"]["button_id"],
                                                                                dropdown_data["location"]["div_id"],
                                                                                dropdown_data["location"]["checklist_id"],
                                                                                dropdown_data["location"]["options"]),
                                                                            create_filter_dropdown(
                                                                                dropdown_data["hiredate"]["button_id"],
                                                                                dropdown_data["hiredate"]["div_id"],
                                                                                dropdown_data["hiredate"]["checklist_id"],
                                                                                dropdown_data["hiredate"]["options"]),
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            ),
                                            dbc.Col( #S2R1S1R1S3
                                                className="S2R1S1R1S3",
                                                children=[
                                                    html.Img(
                                                        src='/assets/filter-inactive.png',
                                                        id='toggle-button',
                                                        className="B2D3button",
                                                        style={'cursor': 'pointer'}  # To make it look like a button
                                                    ),
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]
                    ),
                    dbc.Row( #S2R2 grafy
                        className="S2R1",
                        style={
                            "height": "91%"
                        },
                        children=[
                            dbc.Col( #S2R2S1 grafy vlevo
                                className="S2R2S1",
                                children=[
                                    dbc.Row( #S2R2S1R1 vymezení levé sekce
                                        className="S2R2S1R1",
                                        children=[
                                            dbc.Col(
                                                className="S2R2S1R1S1",
                                                children=[
                                                    dbc.Row( #S2R2S1R1S1R1 nadpis sekce
                                                        className="S2R2S1R1S1R1",
                                                        children=[
                                                            dbc.Col(
                                                                className="S2R2S1R1S1R1S1",
                                                                children=[
                                                                    html.Div( #S2R2S1R1S1R1S1div
                                                                        className="S2R2S1R1S1R1S1div",
                                                                        children=[
                                                                            html.Div(  #S2R2S1R1S1R1S1text
                                                                                "Overview",
                                                                                className="S2R2S1R1S1R1S1text",
                                                                            ),
                                                                        ],
                                                                    )
                                                                ],
                                                            )
                                                        ]
                                                    ),
                                                    create_nadpis_a_cislo("Active Employees", "all", "70px", include_last_div=True), #S2R2S1R1S1R2
                                                    dbc.Row(  # S2R2S1R1S1R3
                                                        className="S2R2S1R1S1R2",
                                                        style={"height": "140px",
                                                                "padding-top": "20px"
                                                                },
                                                        children=[
                                                            dbc.Col(
                                                                className="S2R2S1R1S1R1S2",
                                                                style={"padding-top": "10px"},
                                                                children=[
                                                                    create_nadpis_a_cislo("Hired", 'hire-date-count',"49%", "0", vyska_mezery="20px", include_last_div=False),
                                                                    create_graph_box("chart2_1", vyska_radku="51%")
                                                                ]
                                                            ),
                                                            create_vertical_divider(),
                                                            dbc.Col(
                                                                className="S2R2S1R1S1R1S2",
                                                                style={"padding-top": "10px"},
                                                                children=[
                                                                    create_nadpis_a_cislo("Terminated", 'hire-date-count2', "50%", "0", vyska_mezery="20px", include_last_div=False),
                                                                    create_graph_box("chart2_2", vyska_radku="50%")
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    create_nadpis_podsekce("Departments"),
                                                    dbc.Row(  # S2R2S1R1S1R5
                                                        className="S2R2S1R1S1R2",
                                                        style={"height": "170px",
                                                                },
                                                        children=[
                                                            dbc.Col(
                                                                className="S2R2S1R1S1R1S2",
                                                                style={"padding-top": "10px"},
                                                                children=[
                                                                create_graph_box("chart4")
                                                                ]
                                                            )
                                                        ]
                                                    ),
                                                    create_nadpis_podsekce("Location"),
                                                    dbc.Row(  # S2R2S1R1S1R7
                                                        className="S2R2S1R1S1R2",
                                                        style={"height": "160px",
                                                                "padding-top": "20px"
                                                                },
                                                        children=[
                                                            dbc.Col(
                                                                className="S2R2S1R1S1R1S2",
                                                                style={"flex": "0 0 75%",
                                                                        "padding": "0px"
                                                                       },
                                                                children=[
                                                                create_graph_box("chart5", sirka="99%")
                                                                ]
                                                            ),
                                                            dbc.Col(
                                                                className="S2R2S1R1S1R1S2",
                                                                style={"flex": "0 0 25%",
                                                                       "padding": "0px"
                                                                       },
                                                                children=[
                                                                create_graph_box("chart6")
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )
                                        ]
                                    )
                                ]
                            ),
                            dbc.Col( #S2R2S2 grafy vpravo
                                className="S2R2S2",
                                children=[
                                    dbc.Row(  # S2R2S2R1 první řádek
                                        className="S2R2S2R1",
                                        children=[
                                            dbc.Col( #S2R2S2R1S1
                                                className="S2R2S2R1S1",
                                                children=[
                                                    dbc.Row( #S2R2S2R1S1R1
                                                        className="S2R2S2R1S1R1",
                                                        children=[
                                                            dbc.Col( #S2R2S2R1S1R1S1
                                                                className="S2R2S2R1S1R1S1",
                                                                children=[
                                                                    create_nadpis_sekci("Demographics"),
                                                                    dbc.Row(  # S2R2S2R1S1R1S1R2
                                                                        className="S2R2S2R1S1R1S1R2",
                                                                        children=[
                                                                            dbc.Col(  #S2R2S2R1S1R1S1R2S1
                                                                                className="S2R2S1R1S1R1S1",
                                                                                style={"flex": "0 0 16%"},
                                                                                children=[
                                                                                    create_nadpis_grafu("Gender", font_size="14px", color="white"),
                                                                                    dbc.Row( #S2R2S2R1S1R1S1R2S1R2
                                                                                        className="S2R2S2R1S1R1S1R2S1R2",
                                                                                        children=[
                                                                                            dbc.Col(
                                                                                                className="S2R2S1R1S1R1S1",
                                                                                                children=[
                                                                                                    #create_graph_box(fig_women,"chart7_1"),
                                                                                                    #create_graph_box(fig_men,"chart7_2")
                                                                                                    create_graph_box("chart7_1"),
                                                                                                    create_graph_box("chart7_2")
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    )
                                                                                ]
                                                                            ),
                                                                            create_vertical_divider(),
                                                                            dbc.Col(  # S2R2S2R1S1R1S1R1S1
                                                                                className="S2R2S1R1S1R1S1",
                                                                                style={"flex": "0 0 40%"},
                                                                                children=[
                                                                                    create_nadpis_grafu("Education & Age"),
                                                                                    #create_graph_box(create_education_level_chart(hr), "chart8_1","100%", "100%", "30%", "0 0 75%"),
                                                                                    create_graph_box("chart8_1","100%", "100%", "30%", "0 0 75%"),
                                                                                    dbc.Row(  # S2R2S2R1S1R1S1R2S1R2
                                                                                            className="S2R2S2R1S1R1S1R2S1R2",
                                                                                            children=[
                                                                                                dbc.Col(
                                                                                                    className="S2R2S1R1S1R1S1",
                                                                                                    style={"flex": "0 0 75%"},
                                                                                                    children=[
                                                                                                    dcc.Graph(
                                                                                                        #figure=create_scatter_plot_with_text(pivot_table),
                                                                                                        id='chart8_2',
                                                                                                        style={
                                                                                                            "height": "100%",
                                                                                                            "width": "100%",
                                                                                                            "display": "block"
                                                                                                        }
                                                                                                    ),
                                                                                                    ]
                                                                                                        ),
                                                                                                dbc.Col(
                                                                                                    className="S2R2S1R1S1R1S1",
                                                                                                    children=[
                                                                                                        dcc.Graph(
                                                                                                            #figure=create_age_distribution_chart(hr),
                                                                                                            id='chart8_3',
                                                                                                            style={
                                                                                                                "height": "100%",
                                                                                                                "width": "100%",
                                                                                                                "display": "block"
                                                                                                            }
                                                                                                        ),
                                                                                                    ]
                                                                                                )
                                                                                                    ],
                                                                                                )
                                                                                    ]
                                                                            ),
                                                                            create_vertical_divider(),
                                                                            dbc.Col(  # S2R2S2R1S1R1S1R1S1
                                                                                className="S2R2S1R1S1R1S1",
                                                                                style={"flex": "0 0 38%"},
                                                                                children=[
                                                                                    create_nadpis_grafu("Education & Performance"),
                                                                                    #create_graph_box(create_scatter_plot_with_text2(pivot_table2), "chart9","100%", "100%", "100%", "0 0 100%"),
                                                                                    create_graph_box("chart9","100%", "100%", "100%", "0 0 100%"),
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            ),
                                        ]
                                    ),
                                    dbc.Row(  # S2R2S2R2 druhý řádek
                                        className="S2R2S2R1",
                                        children=[
                                            dbc.Col(  #S2R2S2R2S1
                                                className="S2R2S2R1S1",
                                                children=[
                                                    dbc.Row( #S2R2S2R2S1R1
                                                        className="S2R2S2R1S1R1",
                                                        children=[
                                                            dbc.Col(  #S2R2S2R2S1R1S1
                                                                className="S2R2S2R1S1R1S1",
                                                                children=[
                                                                    create_nadpis_sekci("Income"),
                                                                    dbc.Row(  #S2R2S2R2S1R1S1R2
                                                                        className="S2R2S2R1S1R1S1R2",
                                                                        children=[
                                                                            dbc.Col(  #S2R2S2R2S1R1S1R2S1
                                                                                className="S2R2S2R2S1R1S1R2S1", #"S2R2S2R1S1R1S1R1S1",
                                                                                children=[
                                                                                    create_nadpis_grafu("Education & Gender"),
                                                                                    #create_graph_box(plot_salary_distribution(hr), "chart10")
                                                                                    create_graph_box("chart10")
                                                                                ]
                                                                            ),
                                                                            create_vertical_divider(),
                                                                            dbc.Col(  # S2R2S2R2S1R1S1R2S2
                                                                                className="S2R2S1R1S1R1S1",
                                                                                children=[
                                                                                    create_nadpis_grafu("Age & Salary"),
                                                                                    #create_graph_box(create_scatter_plot(hr), "chart11", vyska_radku="90%", sirka_sloupce="0 0 90%")
                                                                                    create_graph_box("chart11")
                                                                                ]
                                                                            )
                                                                        ]
                                                                    )
                                                                ]
                                                            )
                                                        ]
                                                    )
                                                ]
                                            ),
                                        ]
                                    )
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )
    ]
)


##################################################################################################
@callback(
    [Output('filter_panel', 'style'),
     Output('toggle-button', 'src')],
    Input('toggle-button', 'n_clicks'),
    State('filter_panel', 'style'),
    State('toggle-button', 'src')
)
def toggle_filter_panel(n_clicks, current_style, current_src):
    # Initialize current_style if it is None (initial load)
    if current_style is None:
        current_style = {"display": "none"}

    # Initialize default state for the image (initial load)
    if current_src is None:
        current_src = '/assets/image1.png'  # Image 1 for hidden panel

    # Toggle the display of the filter panel and the button image
    if n_clicks:
        if current_style["display"] == "none":
            # Show the panel and switch to image2
            new_style = {
                "display": "block",
                "backgroundColor": "rgb(85, 85, 85)",
               # "flex-basis": "44%",  # Maintain the width
                #"max-width": "44%",  # Maintain the width
                "position": "relative",  # Ensure it doesn't overlap with the button
            }
            new_src = '/assets/filter-active.png'  # Change to image2 when panel is shown
        else:
            # Hide the panel and switch to image1
            new_style = {
                "display": "none",
                "backgroundColor": "rgb(85, 85, 85)",
                #"flex-basis": "44%",  # Maintain the width
                #"max-width": "44%",  # Maintain the width
                "position": "relative",  # Ensure it doesn't overlap with the button
            }
            new_src = '/assets/filter-inactive.png'  # Change back to image1 when panel is hidden
    else:
        # If no clicks, keep the current style and source (initial load)
        new_style = current_style
        new_src = current_src

    return new_style, new_src


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
def update_charts_and_toggle_menu(n_clicks1, n_clicks2, n_clicks3, n_clicks4, selected_genders, selected_status,
                                  selected_location, selected_hiredate, current_style1, current_style2, current_style3,
                                  current_style4):
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
    # print(filtered_hr.head())
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

    # print(f"Selected Genders: {selected_genders}")
    fig_men, fig_women = generate_donut_charts(hr)



    # Generate charts with the filtered dataset or the original dataset if no filter is applied
    aktivni = filtered_hr['Termdate'].isnull().sum()
    # print(aktivni)

    hire_date_count = filtered_hr['Hiredate'].value_counts().sum()

    terminated_count = filtered_hr.loc[filtered_hr.skoncil == "ano", "skoncil"].shape[0]

    figure1 = create_hire_trend_figure(
        filtered_hr) if not filtered_hr.empty else {}
    figure2 = create_termination_trend_figure(
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
        pivot_table2) if not filtered_hr.empty else {}
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
