import dash
from dash.dependencies import Input, Output, State
from dash import callback, callback_context
from layoutFunctions.forLayout import *

##################################################################################################

#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
dash.register_page(__name__, path='/page-2')

layout = dbc.Container(
    [
        dbc.Row(  # A1
            className="radek1",
            children=[
                # postranní panel
                dbc.Col(  # oblastB sloupecS1
                    className="oblastB sloupecS1",
                    children=[
                        dbc.Row(  # S1R1
                            className="S1R1",
                            children=[
                                dbc.Col(  # S1R1S1
                                    className="S1R1S1",
                                    children=[
                                        create_icon_postranniho_panelu("/assets/Logo.png", "72px"),
                                        # create_icon_postranniho_panelu("/assets/dashboard-summary-active.png"),
                                        create_icon_postranniho_panelu("/assets/dashboard-summary-inactive.png",
                                                                       odkaz="/"),
                                        create_icon_postranniho_panelu("/assets/dashboard-records-active1.png", "60px",
                                                                       "/page-2"),
                                        create_text_postranniho_panelu("Info", mezera_pod_ikonou="0px"),
                                        create_icon_postranniho_panelu("/assets/info-hidden.png", "60px"),
                                        create_text_postranniho_panelu("Export", mezera_pod_ikonou="0px"),
                                        create_icon_postranniho_panelu("/assets/download pdf.png"),
                                        create_icon_postranniho_panelu("/assets/download image.png", "50px"),
                                        create_text_postranniho_panelu("Follow", mezera_pod_ikonou="0px"),
                                        create_icon_postranniho_panelu("/assets/contact-channel.png",
                                                                       odkaz="https://www.youtube.com/watch?v=UcGF09Awm4Y&t=1497s",
                                                                       cil="_blank"),
                                        create_icon_postranniho_panelu("/assets/contact-linkedin.png",
                                                                       odkaz="https://www.linkedin.com/in/pavlina-kurkova-a30939109",
                                                                       cil="_blank"),
                                    ]
                                )
                            ]
                        )
                    ]
                ),
                dbc.Col(
                    className="oblastB sloupecB2",
                    children=[
                        dbc.Row( #S2R1
                            className="S2R1",
                            style={
                                "height": "9%"
                            },
                            children=[
                                dbc.Col( #B2sloupecD1
                                    className="S2R1S1",
                                    children=[
                                        html.Div( #B2D1div
                                            [
                                                html.Span("Human Resources Dashboard | ",
                                                          style={
                                                          "fontWeight": "bold",
                                                          'font-size': '26px',
                                                            'line-height': '1',  # Ensures text aligns on the same baseline
                                                             'display': 'inline-block',  # Keeps the span from altering the block layout
                                                          }
                                                          ),
                                                html.Span("Details",
                                                          style={
                                                          "fontWeight": "normal",
                                                          'font-size': '18px',
                                                            'line-height': '1',  # Ensures text aligns on the same baseline
                                                            'display': 'inline-block',  # Keeps the span from altering the block layout
                                                          }
                                                          )
                                            ],
                                            className="S2R1S1R1S1div",

                                        )
                                    ],
                                ),
                            ]
                        ),
                        dbc.Row( #S2R2
                            style={
                                "width" : "100%",
                                "height" : "88.5%",
                                "backgroundColor" : "black",
                                "border-radius" : "10px"
                            },
                            children=[
                                dbc.Col( #S2R2S1
                                    children=[
                                       dbc.Row( #S2R2S1R1
                                           children=[
                                               dbc.Col( #S2R2S1R1S1
                                                   style={
                                                       "padding": "10px",
                                                       # "border": "2px dashed yellow"
                                                   },
                                                   children=[
                                                    html.Div( #S2R2S1R1S1div
                                                        style={
                                                            # "border": "2px solid green",
                                                            "textAlign": "center",  # "backgroundColor": "black",
                                                            "height": "100%"},
                                                        children=[
                                                            html.Div( #S2R2S1R1S1div2
                                                                "Employee List",
                                                                style={
                                                                    "textAlign": "left", "fontSize": "18px", "color": "white",
                                                                    'fontFamily': '"Times New Roman", Times, serif', "fontWeight": "bold", }),
                                                        ],
                                                    ),
                                                   ]
                                               )
                                           ]
                                       ),
                                        dbc.Row( #S2R2S1R2
                                            children=[
                                                html.Div( #S2R2S1R2div
                                                    [
                                                    # Hidden divs to store visibility state
                                                    dcc.Store(id='store-id-visible', data=False),
                                                    dcc.Store(id='store-demographics-visible', data=False),
                                                    dcc.Store(id='store-role-visible', data=False),
                                                    dcc.Store(id='store-geographics-visible', data=False),
                                                    dcc.Store(id='store-salary-visible', data=False),
                                                    dcc.Store(id='store-status-visible', data=False),
                                                    dcc.Store(id='store-length-visible', data=False),

                                                    dbc.Row( #S2R2S1R2R1
                                                        [
                                                        dbc.Col( #S2R2S1R2R1S1
                                                            html.Div( #S2R2S1R2R1S1div
                                                                "ID",
                                                                id="id-title",
                                                                style={'font-size': '14px', 'text-align': 'left', 'cursor': 'pointer', "color": "white",}
                                                            ),
                                                            style={"flex-basis": "8%", "max-width": "8%"}
                                                        ),
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
                                                        ],
                                                        style={'display': 'flex', 'flex-wrap': 'nowrap', 'align-items': 'center', 'gap': '10px', 'margin': '0 auto',
                                                              'width': '100%', "height": "20px"}
                                                    ),
                                                    dbc.Row( #S2R2S1R2R2
                                                        [
                                                        dbc.Col( #S2R2S1R2R2S1 ID section (hidden by default)
                                                            html.Div(
                                                                id="id-content",
                                                                style={'display': 'none'},
                                                                children=[
                                                                    dcc.Input(
                                                                        id="input-id",
                                                                        placeholder="ID",
                                                                        type="text",
                                                                        style={'width': '100%', 'font-size': '12px'}
                                                                    ),
                                                                ]
                                                            ),
                                                            style={"flex-basis": "8%", "max-width": "8%"}
                                                        ),
                                                        dbc.Col( #S2R2S1R2R2S2 Demographics section (hidden by default)
                                                            html.Div( #S2R2S1R2R2S2div
                                                                id="demographics-content",
                                                                style={'display': 'none'},
                                                                children=[
                                                                    create_dropdown_druha_strana("dropdown-button-name", 'input-name', 'cele_jmeno', "dropdown-menu-name", "Name"),
                                                                    create_dropdown_druha_strana("dropdown-button-gender", 'input-gender', 'Gender', "dropdown-menu-gender", "Gender"),
                                                                    create_dropdown_druha_strana("dropdown-button-age", 'input-age', 'Age_bins', "dropdown-menu-age", "Age"),
                                                                    create_dropdown_druha_strana("dropdown-button-education", 'input-education', 'Education Level', "dropdown-menu-education", "Education"),
                                                                    ]
                                                            ),
                                                        style={"flex-basis": "13%", "max-width": "13%"}
                                                        ),
                                                        dbc.Col( #S2R2S1R2R2S3 Role section (hidden by default)
                                                            html.Div(
                                                                id="role-content",
                                                                style={'display': 'none'},
                                                                children=[
                                                                    create_dropdown_druha_strana("dropdown-button-job", 'input-job','Job Title', "dropdown-menu-job", "Position"),
                                                                    create_dropdown_druha_strana("dropdown-button-department",'input-department','Department',"dropdown-menu-department", "Department"),
                                                                ]
                                                            ),
                                                            style={"flex-basis": "14%", "max-width": "14%"}
                                                        ),
                                                        dbc.Col( #S2R2S1R2R2S4 Geographics section (hidden by default)
                                                            html.Div(
                                                                id="geographics-content",
                                                                style={'display': 'none'},
                                                                children=[
                                                                    create_dropdown_druha_strana("dropdown-button-location",'input-location', 'lokace',"dropdown-menu-location","Location"),
                                                                    create_dropdown_druha_strana("dropdown-button-state",'input-state', 'State',"dropdown-menu-state", "State"),
                                                                    create_dropdown_druha_strana("dropdown-button-city",'input-city', 'City',"dropdown-menu-city", "City"),
                                                                ]
                                                            ),
                                                            style={"flex-basis": "16%", "max-width": "16%"}
                                                        ),
                                                        dbc.Col( #S2R2S1R2R2S5 Salary section (hidden by default)
                                                            html.Div(
                                                                id="salary-content",
                                                                style={'display': 'none'},
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
                                                                 ]
                                                            ),
                                                                style={"flex-basis": "12%", "max-width": "12%"}
                                                        ),
                                                        dbc.Col( #S2R2S1R2R2S5 Status section (hidden by default)
                                                            html.Div(
                                                                id="status-content",
                                                                style={'display': 'none'},
                                                                children=[
                                                                    create_dropdown_druha_strana("dropdown-button-status",'input-status', 'skoncil',"dropdown-menu-status", "Status"),
                                                                    create_dropdown_druha_strana("dropdown-button-hire-year",'input-year-hire', 'Hireyear',"dropdown-menu-hire-year", "Hire"),
                                                                    create_dropdown_druha_strana("dropdown-button-termination-year",'input-year-term', 'Termyear',"dropdown-menu-termination-year","Termination",
                                                                                                 [{'label': str(i),
                                                                                              'value': i} if pd.notnull(
                                                                                        i) else {'label': 'N/A',
                                                                                                 'value': 'N/A'} for i
                                                                                             in
                                                                                             sorted(hr['Termyear'].unique())]
                                                                                                 ),
                                                                ]
                                                            ),
                                                            style={"flex-basis": "15%", "max-width": "15%"}
                                                        ),
                                                        dbc.Col( #S2R2S1R2R2S5 Length of Employment section (hidden by default)
                                                            html.Div(
                                                                id="length-content",
                                                                style={'display': 'none'},
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
                                                                 ]
                                                            ),
                                                                style={"flex-basis": "15%", "max-width": "15%"}
                                                        ),

                                                    ],
                                                        style={'display': 'flex', 'flex-wrap': 'nowrap', 'align-items': 'flex-start', 'gap': '10px', 'margin': '0 auto',
                                                              'width': '100%'}
                                                    ),
                                                    html.Div(
                                                        id="output",
                                                        style={'margin-top': '20px'}
                                                    )
                                                ]
                                                )
                                            ],
                                        ),
                                       dbc.Row( #S2R2S1R3
                                           style={
                                              "height" : "450px",
                                              #"backgroundColor" : "#2a2b2b",
                                              "backgroundColor" : "black",
                                               },
                                           children=[
                                               dbc.Col(
                                                    create_table(),
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
    ],
)
############################################################################################################

@callback(
    Output('id-content', 'style'),
    Output('demographics-content', 'style'),
    Output('role-content', 'style'),
    Output('geographics-content', 'style'),
    Output('salary-content', 'style'),
    Output('status-content', 'style'),
    Output('length-content', 'style'),
    Input('id-title', 'n_clicks'),
    Input('demographics-title', 'n_clicks'),
    Input('role-title', 'n_clicks'),
    Input('geographics-title', 'n_clicks'),
    Input('salary-title', 'n_clicks'),
    Input('status-title', 'n_clicks'),
    Input('length-title', 'n_clicks'),
    State('id-content', 'style'),
    State('demographics-content', 'style'),
    State('role-content', 'style'),
    State('geographics-content', 'style'),
    State('salary-content', 'style'),
    State('status-content', 'style'),
    State('length-content', 'style'),
)
def toggle_contents(id_n_clicks, demo_n_clicks, role_n_clicks, geo_n_clicks, salary_n_clicks, status_n_clicks, length_n_clicks,
                    id_style, demo_style, role_style, geo_style, salary_style, status_style, length_style):

    ctx = callback_context
    if not ctx.triggered:
        # No clicks yet; hide all content
        return ({'display': 'none'},) * 7
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]

        # Map content IDs to their current styles
        styles = {
            'id-content': id_style,
            'demographics-content': demo_style,
            'role-content': role_style,
            'geographics-content': geo_style,
            'salary-content': salary_style,
            'status-content': status_style,
            'length-content': length_style
        }

        # Determine which content to toggle
        content_id = button_id.replace('-title', '-content')
        current_style = styles.get(content_id, {'display': 'none'})

        # Toggle the display style
        if current_style['display'] == 'none':
            styles[content_id] = {'display': 'block'}
        else:
            styles[content_id] = {'display': 'none'}

        # Return the updated styles for all content sections
        return (
            styles['id-content'],
            styles['demographics-content'],
            styles['role-content'],
            styles['geographics-content'],
            styles['salary-content'],
            styles['status-content'],
            styles['length-content']
        )


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
        filtered_data.loc[:, 'Salary2_int'] = filtered_data['Salary2'].replace({r'\$': '', ',': ''}, regex=True).astype(int)
        filtered_data = filtered_data[
            (filtered_data['Salary2_int'] >= salary_values[0]) &
            (filtered_data['Salary2_int'] <= salary_values[1])
            ]

    # Handle length of employment filtering
    if length_values:
        filtered_data = filtered_data.copy()
        filtered_data['Length_int'] = filtered_data['delka_prac_pomeru_text'].str.extract(r'(\d+)').astype(int)
        filtered_data = filtered_data[
            (filtered_data['Length_int'] >= length_values[0]) &
            (filtered_data['Length_int'] <= length_values[1])
            ]

    if status_values:
        filtered_data = filtered_data[filtered_data['skoncil'].isin(status_values)]
    if hire_year_values:
        filtered_data = filtered_data[filtered_data['Hireyear'].isin(hire_year_values)]
    if term_year_values:
        if 'N/A' in term_year_values:
            filtered_data = filtered_data[filtered_data['Termyear'].isna()]
        else:
            filtered_data = filtered_data[filtered_data['Termyear'].isin(term_year_values)]

    # Filtered data for the table
    filtered_data = filtered_data.loc[:, [
                                             "Employee_ID", "personal_info", "Job Info", "bydliste", "Salary2",
                                             "pracovni_pomer", "delka_prac_pomeru_text"
                                         ]]

    return updated_style_gender, updated_style_age, updated_style_education, updated_style_job, updated_style_department, \
        updated_style_location, updated_style_state, updated_style_city, updated_style_status, updated_style_hire_year, \
        updated_style_term_year, updated_style_name, filtered_data.to_dict('records')








