from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.graph_objects as go
import pandas as pd
from dateutil.relativedelta import relativedelta
import base64


HEIGHT = "800px"
WIDTH = "1400px"


hr = pd.read_csv("HumanResources.csv", sep=";")
#print(hr.head())

hr["cele_jmeno"] = hr["First Name"] + " " + hr["Last Name"]

# aktivni = hr['Termdate'].isnull().sum()

# hire_date_count = hr['Hiredate'].value_counts().sum()

hr['Termdate'] = pd.to_datetime(hr['Termdate'], format="%d/%m/%Y", errors='coerce')
hr["skoncil"] = hr.Termdate.apply(lambda x: "ne" if pd.isna(x) else "ano")
# print(hr.loc[:,["Termdate","skoncil"]].head(10))
# print(hr['skoncil'].value_counts(dropna=False))

hr["lokace"] = hr.State.apply(lambda x: "HQ" if x == "New York" else "Branch")
# print(hr["lokace"].head())
hr['Hiredate'] = pd.to_datetime(hr['Hiredate'], format="%d/%m/%Y", errors='coerce')
hr['Hireyear'] = hr['Hiredate'].dt.year
# hr['Hireyar'] = hr['Hiredate'].astype("string")

hr['Birthdate'] = pd.to_datetime(hr['Birthdate'], format="%d/%m/%Y")

# Get today's date
today = pd.to_datetime('today')

# Calculate the age correctly
hr['Age'] = today.year - hr['Birthdate'].dt.year - (
    (today.month < hr['Birthdate'].dt.month) |
    ((today.month == hr['Birthdate'].dt.month)
        & (today.day < hr['Birthdate'].dt.day))
)


#-------------------------
# Define symbols for female and male gender with bold font-weight and adjusted alignment
female_symbol = '<span style="color:#03c4a1; font-size:38px; font-weight:bold; vertical-align: middle;">&#9792;</span>'  # Pink Female Symbol, bold
male_symbol = '<span style="color:#03c4a1; font-size:38px; font-weight:bold; vertical-align: middle;">&#9794;</span>'    # Blue Male Symbol, bold

# Function to assign the symbol based on gender and style the Age and Education Level in grey
def generate_personal_info(row):
    gender_symbol = female_symbol if row['Gender'] == 'Female' else male_symbol
    # Wrapping Age and Education Level in a grey <span> tag and using a small margin for proper alignment
    age_education = f'<div style="margin-left: 1px; color:grey;">{row["Age"]} | {row["Education Level"]}</div>'
    name = f'<div style="font-weight:bold; margin-left: 1px;">{row["cele_jmeno"]}</div>'
    
    # Combine the gender symbol with the name and the age/education info, ensuring proper spacing
    return f'<div style="display:flex; align-items:center;">{gender_symbol}<div>{name}{age_education}</div></div>'
# Create the 'personal_info' column by applying the function to each row
hr['personal_info'] = hr.apply(generate_personal_info, axis=1)
#hr['personal_info'] = hr['cele_jmeno'] + '<br><span style="color: grey;">' + hr['Age'].astype(str) + " | " + hr['Education Level'] + '</span>'
#-----------------------------------------

def generate_job_info(row):
    job_info_vrsek = f'<div style="font-weight:bold; margin-left: 1px;">{row["Job Title"]}</div>'
    job_info_spodek = f'<div style="margin-left: 1px; color:grey;">{row["Department"]}</div>'
    return f'<div style="display:flex; align-items:center;"><div>{job_info_vrsek}{job_info_spodek}</div></div>'
    #hr['Job Info'] = hr['Job Title'] + '<br><span style="color: grey;">' + hr['Department'] + '</span>'
hr['Job Info'] = hr.apply(generate_job_info, axis=1)
#------------------------------------------

HQ_symbol = '<span style="color:#03c4a1; font-size:14px;  vertical-align: middle;">&#11044;</span>'
branch_symbol = '<span style="color:grey; font-size:14px;  vertical-align: middle;">&#11044;</span>'

def generate_bydliste_info(row):
    bydliste_symbol = HQ_symbol if row['lokace'] == 'HQ' else branch_symbol
    bydliste_info_vrsek = f'<div style="font-weight:bold; margin-left: 1px;">{row["City"]}</div>'
    bydliste_info_spodek = f'<div style="margin-left: 1px; color:grey;">{row["State"]}</div>'
    return f'<div style="display:flex; align-items:center;">{bydliste_symbol}<div>{bydliste_info_vrsek}{bydliste_info_spodek}</div></div>'
    #hr['Job Info'] = hr['Job Title'] + '<br><span style="color: grey;">' + hr['Department'] + '</span>'
hr['bydliste'] = hr.apply(generate_bydliste_info, axis=1)
#hr['bydliste'] = hr['City'] + '<br><span style="color: grey;">' + hr['State'] + '</span>'
#-----------------------------------------------------

def format_salary(salary):
    return f"${salary:,.0f}"

# Apply the format_salary function to the 'Salary' column in your DataFrame
hr['Salary2'] = hr['Salary'].apply(format_salary)
#--------------------------------------------
hr['Hiredate2'] = hr['Hiredate'].dt.strftime('%m/%d/%Y')
hr['Termdate2'] = hr['Termdate'].dt.strftime('%m/%d/%Y')

# Create HTML for each row, including a blue or purple circle depending on the "skoncil" column
def generate_employment_status(row):
    # Check the value in "skoncil" and assign the appropriate colored circle
    if row['skoncil'] == 'ne':
        status_symbol = '<span style="color:#03c4a1; font-size:14px;  vertical-align: middle;">&#11044;</span>'  # Blue Circle for "ne"
    elif row['skoncil'] == 'ano':
        status_symbol = '<span style="color:purple; font-size:14px;  vertical-align: middle;">&#11044;</span>'  # Purple Circle for "ano"
    else:
        status_symbol = '<span style="color:grey; font-size:14px;  vertical-align: middle;">&#11044;</span>'  # Default grey circle for other statuses
    
    date_range = f'<div style="margin-left: 1px; color:grey;">{row["Hiredate2"]} - {row["Termdate2"]}</div>'
    #date_range = f'<div style="margin-left: 1px; color:grey;">{row["Hiredate2"].date()} - {row["Termdate2"].date()}</div>'
    #date_range = f'<br><span style="color:grey;">{row["Hiredate"].date()} - {row["Termdate"].date()}</span>'
    esli_skoncil = f'<div style="font-weight:bold; margin-left: 1px;">{row["skoncil"]}</div>'
    
    # Combine the symbol, employment status (from skoncil), and date range
    #return f'{status_symbol} <strong>{row["skoncil"].capitalize()}</strong>{date_range}'
    return f'<div style="display:flex; align-items:center;">{status_symbol}<div>{esli_skoncil}{date_range}</div></div>'
# Apply the function to the "pracovni_pomer" column
hr['pracovni_pomer'] = hr.apply(generate_employment_status, axis=1)
#hr['pracovni_pomer'] = hr['skoncil'] + '<br><span style="color: grey;">' + hr['Hiredate'].astype(str) + " - " + hr['Termdate'].astype(str) + '</span>'
#---------------------------------------


hr['delka_prac_pomeru'] = hr.apply(lambda row: relativedelta(
    pd.Timestamp('today') if pd.isnull(row['Termdate']) else row['Termdate'], 
    row['Hiredate']).years if pd.notnull(row['Hiredate']) else None, axis=1)
hr['delka_prac_pomeru_text'] = hr['delka_prac_pomeru'].astype(str) + ' years'
#----------------------------------------------

hrv = hr.loc[:,["Employee_ID","personal_info", "Job Info", "bydliste", "Salary2", "pracovni_pomer", "delka_prac_pomeru_text"]]

def create_blank_figure():
    fig = go.Figure(go.Scatter(x=[], y=[]))  # Empty scatter plot
    fig.update_layout(
        paper_bgcolor='black',
        plot_bgcolor='black',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig
############################################################################


def create_hire_trend_figure(hr: pd.DataFrame) -> go.Figure:
    """
    Create a Plotly figure showing the number of hires per year.

    Parameters:
    hr (pd.DataFrame): DataFrame with a 'Hiredate' column of datetime type.

    Returns:
    go.Figure: A Plotly figure object.
    """

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=sorted(hr.Hiredate.dt.year.unique()),  # Sorted years
        y=hr.groupby(hr['Hiredate'].dt.year).size().reset_index(
            name='Count').loc[:, "Count"],  # Corresponding counts
        mode='lines',  # 'lines', 'markers', or 'lines+markers'
        line=dict(color='#03c4a1'),
        fill='tozeroy',  # Fill the area under the line
        # Same color as the line but with lower opacity
        fillcolor='rgba(3, 196, 161, 0.2)'
    ))

    fig.update_layout(
        template='plotly_dark',  # bylo tam plotly_white
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
        height=60,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
    )

    fig.update_xaxes(
        visible=False,  # Hide the x-axis
        showticklabels=False  # Hide x-axis tick labels
    )

    fig.update_yaxes(
        visible=False,  # Hide the y-axis
        showticklabels=False,  # Hide y-axis tick labels
        # range=[350, 1600]
    )
    return fig
###########################################################################################################


def create_hire_trend_figure2(hr: pd.DataFrame) -> go.Figure:
    """
    Create a Plotly figure showing the number of hires per year.

    Parameters:
    hr (pd.DataFrame): DataFrame with a 'Hiredate' column of datetime type.

    Returns:
    go.Figure: A Plotly figure object.
    """
    hr['Termdate'] = pd.to_datetime(hr['Termdate'], format="%d/%m/%Y")

    hr = hr.loc[hr.Termdate.notnull(), :]

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=sorted(hr.Termdate.dt.year.unique()),  # Sorted years
        y=hr.groupby(hr['Termdate'].dt.year).size().reset_index(
            name='Count').loc[:, "Count"],  # Corresponding counts
        mode='lines',  # 'lines', 'markers', or 'lines+markers'
        line=dict(color='#c62b88'),
        fill='tozeroy',  # Fill the area under the line
        # Same color as the line but with lower opacity
        fillcolor='rgba(198, 43, 136, 0.2)'
    ))

    fig.update_layout(
        template='plotly_dark',  # bylo tam plotly_white
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
        height=60,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
    )

    fig.update_xaxes(
        visible=False,  # Hide the x-axis
        showticklabels=False  # Hide x-axis tick labels
    )

    fig.update_yaxes(
        visible=False,  # Hide the y-axis
        showticklabels=False  # Hide y-axis tick labels
    )
    return fig


# create_hire_trend_figure2(hr)

#############################################################################################################


def plot_department_termination(hr):
    # Group the data by 'Department' and 'skoncil', then count the occurrences
    grouped_df = hr.groupby(['Department', 'skoncil']
                            ).size().reset_index(name='Count')

    # Pivot the DataFrame for easier plotting
    pivot_df = grouped_df.pivot(
        index='Department', columns='skoncil', values='Count').fillna(0)

    # Ensure the correct order of columns and handle missing columns
    if 'ne' not in pivot_df.columns:
        pivot_df['ne'] = 0
    if 'ano' not in pivot_df.columns:
        pivot_df['ano'] = 0

    pivot_df = pivot_df[['ne', 'ano']]

    # Sort the departments by the sum of 'ne' and 'ano'
    pivot_df = pivot_df.sort_values(by=['ne', 'ano'], ascending=[True, True])

    # Define the colors
    colors = ['#03c4a1', '#c62b88']

    # Create the figure
    fig = go.Figure()

    # Add bars for each 'skoncil' category
    for i, column in enumerate(pivot_df.columns):
        fig.add_trace(go.Bar(
            y=pivot_df.index,
            x=pivot_df[column],
            name=column,
            orientation='h',
            marker=dict(color=colors[i]),
            text=pivot_df[column],
            textposition='auto',  # 'auto' allows text to be inside or outside based on fit
            textfont=dict(size=10),  # Fixed font size
            cliponaxis=False  # Allows text to be outside the bar
        ))

    # Add annotations for padding
    annotations = []
    for i, department in enumerate(pivot_df.index):
        annotations.append(dict(
            x=0,
            y=i,
            xref="paper",
            yref="y",
            text=department,
            showarrow=False,
            xanchor='left',
            xshift=-100  # Adjust this value to increase/decrease the space
        ))

    # Update layout
    fig.update_layout(
        barmode='stack',
        template='plotly_dark',
        margin=dict(l=120, r=20, t=0, b=0),  # Adjust margins if needed
        autosize=True,
        width=390,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        showlegend=False,  # Hide the legend if not needed
        annotations=annotations,
        font=dict(size=10)
    )

    # Update y-axes
    fig.update_yaxes(
        automargin=True,  # Ensures that labels don't overlap with the plot
        showticklabels=False  # Hide the y-axis labels since we are using annotations
    )

    # Update x-axes
    fig.update_xaxes(
        visible=False,  # Hide the x-axis
        showticklabels=False  # Hide x-axis tick labels
    )

    return fig


############################################################################################################
city_coords = {
    'New York City, New York': (40.7128, -74.0060),
    'Charlotte, North Carolina': (35.2271, -80.8431),
    'Grand Rapids, Michigan': (42.9634, -85.6681),
    'Warren, Michigan': (42.5145, -83.0147),
    'Raleigh, North Carolina': (35.7796, -78.6382),
    'Philadelphia, Pennsylvania': (39.9526, -75.1652),
    'Cleveland, Ohio': (41.4993, -81.6944),
    'Detroit, Michigan': (42.3314, -83.0458),
    'Norfolk, Virginia': (36.8508, -76.2859),
    'Allentown, Pennsylvania': (40.6084, -75.4902),
    'Cincinnati, Ohio': (39.1031, -84.5120),
    'Greensboro, North Carolina': (36.0726, -79.7920),
    'Virginia Beach, Virginia': (36.8529, -75.9780),
    'Aurora, Illinois': (41.7606, -88.3201),
    'Chicago, Illinois': (41.8781, -87.6298),
    'Naperville, Illinois': (41.7508, -88.1535),
    'Columbus, Ohio': (39.9612, -82.9988),
    'Richmond, Virginia': (37.5407, -77.4360),
    'Charleston, West Virginia': (38.3498, -81.6326),
    'Huntington, West Virginia': (38.4192, -82.4452),
    'Pittsburgh, Pennsylvania': (40.4406, -79.9959),
    'Morgantown, West Virginia': (39.6295, -79.9559),
    'Rochester, New York': (43.1566, -77.6088),
    'Buffalo, New York': (42.8864, -78.8784)
}

# Function to map city and state to coordinates


def get_coords(city, state):
    return city_coords.get(f'{city}, {state}', (None, None))


# Apply the function to get latitudes and longitudes
hr['latitude'], hr['longitude'] = zip(
    *hr.apply(lambda row: get_coords(row['City'], row['State']), axis=1))

# hr["skoncil"] = hr.Termdate.apply(lambda x: "ne" if pd.isna(x) else "ano")


def create_zoomed_map_go(dataframe, lat_col='latitude', lon_col='longitude',
                         city_col='City', state_col='State',
                         center_lat=40.0, center_lon=-80.0, scope='usa'):
    """
    Creates a zoomed-in geographical map using plotly.graph_objects.

    Parameters:
    - dataframe: pd.DataFrame containing the data.
    - lat_col: str, name of the latitude column in the dataframe.
    - lon_col: str, name of the longitude column in the dataframe.
    - city_col: str, name of the city column in the dataframe.
    - state_col: str, name of the state column in the dataframe.
    - center_lat: float, latitude for the center of the map.
    - center_lon: float, longitude for the center of the map.
    - scope: str, scope of the map (default is 'usa').

    Returns:
    - fig: plotly.graph_objects.Figure object, the map figure.
    """

    # Aggregate data by City and State to count occurrences
    city_counts = dataframe.groupby(
        [city_col, state_col, lat_col, lon_col]).size().reset_index(name='count')

    # Add scatter geo with marker size reflecting the count of each city
    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lat=city_counts[lat_col],
        lon=city_counts[lon_col],
        mode='markers',
        marker=dict(
            size=city_counts['count'],  # Use the count for marker size
            sizemode='area',
            sizeref=2.*max(city_counts['count']) / \
            (20.**2),  # Adjust the size scaling
            symbol='circle',
            color='rgba(3, 196, 161, 0.2)',  # Cyan color with lower opacity
            line=dict(width=1, color='rgba(3, 196, 161, 1)')
        ),
        showlegend=False,
        text=city_counts[city_col] + ', ' + city_counts[state_col] + \
        ': ' + city_counts['count'].astype(str),
        hoverinfo='text'
    ))

    # Highlight the state of New York with cyan color
    fig.add_trace(go.Choropleth(
        locations=['NY'],  # New York state abbreviation
        locationmode='USA-states',
        z=[1],  # Dummy variable for coloring
        colorscale=[[0, 'rgba(0, 255, 255, 0.2)'], [
            1, 'rgba(3, 196, 161, 0.2)']],  # Cyan color
        showscale=False,
        geo='geo',
    ))

    # Add state names at their approximate central coordinates
    state_coords = {
        'New York': (42.1657, -74.9481),
        'North Carolina': (35.7821, -80.7935),
        'Michigan': (44.3148, -85.6024),
        'Pennsylvania': (41.2033, -77.1945),
        'Ohio': (40.4173, -82.9071),
        'Virginia': (37.4316, -78.6569),
        'Illinois': (40.6331, -89.3985),
        'West Virginia': (38.5976, -80.4549),
    }

    for state, coords in state_coords.items():
        fig.add_trace(go.Scattergeo(
            lat=[coords[0]],
            lon=[coords[1]],
            mode='text',
            text=state,
            showlegend=False,
            textfont=dict(
                size=9,
                color='white'
            )
        ))

    # Update layout for centering and scope
    fig.update_layout(
        geo=dict(
            scope=scope,
            center=dict(lat=center_lat, lon=center_lon),
            projection_scale=2.5,  # Scale for zooming in; adjust as necessary
            showland=True,
            landcolor="rgba(211, 211, 211, 0.3)",
            subunitcolor="rgba(211, 211, 211, 0.25)",
            bgcolor='black',
        ),
        margin=dict(l=0, r=0, t=0, b=0),  # Remove margins to maximize map area
        template='plotly_dark',
        autosize=True,
        paper_bgcolor='black',  # Transparent background
        plot_bgcolor='black',    # Transparent plot background
    )

    return fig
####################################################################################################


def plot_lokace_distribution(hr):
    """
    Creates a bar plot showing the distribution of values in the specified column.

    Parameters:
        hr (pd.DataFrame): The DataFrame containing the data.

    Returns:
        fig (go.Figure): The Plotly Figure object.
    """

    # Count the occurrences in the specified column
    count_data = hr["lokace"].value_counts().reset_index()
    count_data.columns = ["lokace", 'count']

    # Calculate percentage of total
    total_count = count_data['count'].sum()
    count_data['percentage'] = (count_data['count'] / total_count) * 100

    # Define colors, default to grey and cyan for "HQ"
    colors = ['#03c4a1' if loc ==
              'HQ' else 'grey' for loc in count_data['lokace']]

    # Create a bar plot
    fig = go.Figure(go.Bar(
        x=count_data["lokace"],
        y=count_data['count'],
        marker_color=colors,
        width=0.6
    ))

    # Update layout to move x-axis to the top
    fig.update_layout(
        xaxis=dict(
            side="top"
        ),
        showlegend=False,
        template='plotly_dark',
    )

    # Add annotations for percentages below each bar
    annotations = []
    for i, row in count_data.iterrows():
        annotations.append(dict(
            x=row["lokace"],
            y=-0.05 * total_count,  # position slightly below the x-axis
            text=f"{int(round(row['percentage'], 0))}%",
            showarrow=False,
            yanchor="top",
            xanchor="center",
            textangle=-90
        ))

    fig.update_layout(
        annotations=annotations,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        margin=dict(l=0, r=0, t=0, b=0),
        yaxis=dict(
            showticklabels=False,  # Remove the tick labels
            showgrid=False,
            zeroline=False
        ),
        font=dict(size=10),

    )

    # Return the figure
    return fig

##########################################################################################################
# def generate_donut_charts(hr_df):
#     # Create the 'skoncil' column based on 'Termdate'
#     hr_df["skoncil"] = hr_df.Termdate.apply(
#         lambda x: "ne" if pd.isna(x) else "ano")

#     def calculate_percentages(gender):
#         gender_data = hr_df[hr_df['Gender'] == gender]
#         total = len(gender_data)
#         active = len(gender_data[gender_data['skoncil'] == 'ne'])
#         inactive = len(gender_data[gender_data['skoncil'] == 'ano'])
#         active_pct = round(active / total * 100, 0)
#         inactive_pct = round(inactive / total * 100, 0)
#         # Total percentage of this gender
#         total_pct = round(total / len(hr_df) * 100, 0)
#         return active_pct, inactive_pct, total_pct

#     def create_donut_chart(active_pct, inactive_pct, total_pct, gender_label):
#         fig = go.Figure(data=[go.Pie(labels=['Active', 'Inactive'],
#                                      values=[active_pct, inactive_pct],
#                                      hole=.7,
#                                      textinfo='percent',  # Display percentages
#                                      textposition='outside'  # Position the text outside the slices
#                                      )])

#         fig.update_traces(marker=dict(colors=['#03c4a1', '#c62b88']))
#         fig.update_layout(showlegend=False,
#                           annotations=[
#                               dict(text=f'{int(total_pct)}%', x=0.5,
#                                    y=0.5, font_size=10, showarrow=False),
#                               dict(text=gender_label, x=-0.14, y=0.5,
#                                    font_size=10, showarrow=False, textangle=-90)
#                           ],
#                           paper_bgcolor='rgba(0,0,0,0)',
#                           template='plotly_dark',
#                           margin=dict(l=0, r=0, t=20, b=15),
#                           font=dict(size=10)
#                           )
#         return fig

#     # Calculate percentages for men and women
#     men_active_pct, men_inactive_pct, men_total_pct = calculate_percentages(
#         'Male')
#     women_active_pct, women_inactive_pct, women_total_pct = calculate_percentages(
#         'Female')

#     # Generate and show the donut charts
#     fig_men = create_donut_chart(
#         men_active_pct, men_inactive_pct, men_total_pct, 'Male')
#     fig_women = create_donut_chart(
#         women_active_pct, women_inactive_pct, women_total_pct, 'Female')

#     return fig_men, fig_women


# fig_men, fig_women = generate_donut_charts(hr)


def generate_donut_charts(hr_df):
    hr_df["skoncil"] = hr_df.Termdate.apply(
        lambda x: "ne" if pd.isna(x) else "ano")

    def calculate_percentages(gender):
        gender_data = hr_df[hr_df['Gender'] == gender]
        total = len(gender_data)

        # Handle the case where total is zero to avoid division by zero
        if total == 0:
            return 0, 0, 0  # or any other values that make sense for your chart

        active = len(gender_data[gender_data['skoncil'] == 'ne'])
        inactive = len(gender_data[gender_data['skoncil'] == 'ano'])
        active_pct = round(active / total * 100, 0)
        inactive_pct = round(inactive / total * 100, 0)
        total_pct = round(total / len(hr_df) * 100, 0)

        return active_pct, inactive_pct, total_pct

    def create_donut_chart(active_pct, inactive_pct, total_pct, gender_label):
        fig = go.Figure(data=[go.Pie(labels=['Active', 'Inactive'],
                                     values=[active_pct, inactive_pct],
                                     hole=.7,
                                     textinfo='percent',  # Display percentages
                                     textposition='outside'  # Position the text outside the slices
                                     )])

        fig.update_traces(marker=dict(colors=['#03c4a1', '#c62b88']))
        fig.update_layout(showlegend=False,
                          annotations=[
                              dict(text=f'{int(total_pct)}%', x=0.5,
                                   y=0.5, font_size=10, showarrow=False),
                              dict(text=gender_label, x=-0.14, y=0.5,
                                   font_size=10, showarrow=False, textangle=-90)
                          ],
                          paper_bgcolor='rgba(0,0,0,0)',
                          template='plotly_dark',
                          margin=dict(l=0, r=0, t=20, b=15),
                          font=dict(size=10)
                          )
        return fig

    men_active_pct, men_inactive_pct, men_total_pct = calculate_percentages(
        'Male')
    women_active_pct, women_inactive_pct, women_total_pct = calculate_percentages(
        'Female')

    fig_men = create_donut_chart(
        men_active_pct, men_inactive_pct, men_total_pct, 'Male')
    fig_women = create_donut_chart(
        women_active_pct, women_inactive_pct, women_total_pct, 'Female')

    return fig_men, fig_women
#######################################################################################################


def create_scatter_plot_with_text(pivot_table):
    # Melt the pivot table to make it suitable for a scatter plot
    melted_df = pivot_table.melt(
        id_vars=['Age_bins'], var_name='Education Level', value_name='Count')

    # Normalize the size of the circles for better visualization
    melted_df['Size'] = melted_df['Count'] / melted_df['Count'].max() * 100

    melted_df['Education Level'] = melted_df['Education Level'].replace({
        'High School': 'High S',
        'Bachelor': 'Bc',
        'Master': 'Msc'
    })

    # Identify the row with the maximum Count
    max_row = melted_df.loc[melted_df['Count'].idxmax()]

    # Calculate the percentage for the maximum value
    total_sum = melted_df['Count'].sum()
    max_percentage = round((max_row['Count'] / total_sum) * 100, 0)

    # Create the scatter plot with circles
    fig = go.Figure()

    # Add a scatter trace for each Age Bin
    for age_bin in melted_df['Age_bins'].unique():
        df = melted_df[melted_df['Age_bins'] == age_bin]

        # Determine the text for each point
        text = []
        for _, row in df.iterrows():
            if (row['Education Level'] == max_row['Education Level']) and (age_bin == max_row['Age_bins']):
                text.append(f"{int(max_percentage)}%")
            else:
                text.append("")  # No text for other points

        fig.add_trace(go.Scatter(
            x=df['Education Level'],
            y=[age_bin] * len(df),
            mode='markers+text',  # Add text mode
            marker=dict(
                size=df['Size'],
                sizemode='area',
                # <----- zmenšení pětky -> větší kruhy
                sizeref=2.*max(melted_df['Size'])/(60.**2)*5,
                sizemin=4,
                color=['#03c4a1' if (row['Education Level'] == max_row['Education Level']) and
                       (age_bin == max_row['Age_bins']) else "#a6a5a2" for _, row in df.iterrows()]
            ),
            text=text,  # Set the text for each point
            textposition="middle center",  # Position the text inside the circle
            name=age_bin
        ))

    # Update layout to ensure correct order of the y-axis and x-axis
    fig.update_layout(
        yaxis=dict(categoryorder='array', categoryarray=[
                   '54+', '45-54', '35-44', '25-34', '<25'], showgrid=False,
                   # ticklabelposition="inside"
                   ),
        xaxis=dict(categoryorder='array', categoryarray=[
                   # Set the x-axis side to top
                   'High S', 'Bc', 'Msc', 'PhD'], side='top', showgrid=False),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        margin=dict(l=0, r=0, t=20, b=0),
        autosize=True,
        template='plotly_dark',
        font=dict(size=10),
    )

    return fig


# Example usage
# pivot_table = pd.DataFrame({
#     'Age_bins': ['<25', '25-34', '35-44', '45-54', '54+'],
#     'Bachelor': [576, 1351, 1664, 1280, 545],
#     'High School': [166, 437, 583, 446, 187],
#     'Master': [116, 296, 409, 290, 126],
#     'PhD': [0, 97, 121, 116, 144]
# })
# ----------------------------------------------------------------------------


def create_education_level_chart(hr):
    """
    Creates a bar chart of the Education Level distribution with a special color for the highest bar.

    Parameters:
    hr_data (DataFrame): The DataFrame containing the 'Education Level' column.

    Returns:
    fig (Figure): A Plotly figure object representing the bar chart.
    """

    # Count the occurrences of each category
    counts = hr['Education Level'].value_counts()
    ordered_counts = counts.reindex(
        ['High School', 'Bachelor', 'Master', 'PhD'], fill_value=0)

    # Determine the index of the bar with the highest count
    colors = ['lightgrey' if count != ordered_counts.max(
    ) else '#03c4a1' for count in ordered_counts.values]

    # Create the bar chart with conditional colors
    fig = go.Figure(data=[
        go.Bar(x=ordered_counts.index, y=ordered_counts.values,
               marker_color=colors, width=0.3)
    ])

    # Set the layout
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        margin=dict(l=30, r=0, t=0, b=0),
        autosize=True,
        template='plotly_dark',
        yaxis=dict(
            showline=False,  # Remove the axis line
            showgrid=False,  # Remove the grid lines
            showticklabels=False,  # Remove the tick labels
            zeroline=False,
            linewidth=0,
        ),
        xaxis=dict(
            showline=False,  # Remove the axis line
            showgrid=False,  # Remove the grid lines
            showticklabels=False,  # Remove the tick labels
            zeroline=False,
            linewidth=0,
        )
    )

    return fig

# --------------------------------------------------------------------------


def create_age_distribution_chart(hr):
    # Convert Birthdate to datetime
    hr['Birthdate'] = pd.to_datetime(hr['Birthdate'], format="%d/%m/%Y")

    # Get today's date
    today = pd.to_datetime('today')

    # Calculate the age correctly
    hr['Age'] = today.year - hr['Birthdate'].dt.year - (
        (today.month < hr['Birthdate'].dt.month) |
        ((today.month == hr['Birthdate'].dt.month)
         & (today.day < hr['Birthdate'].dt.day))
    )

    # Define the bins and labels
    bins = [0, 24, 34, 44, 54, float('inf')]
    labels = ['<25', '25-34', '35-44', '45-54', '54+']

    # Create the "Age_bins" column
    hr['Age_bins'] = pd.cut(hr['Age'], bins=bins,
                            labels=labels, right=True, include_lowest=True)

    # Count the occurrences of each category
    counts = hr['Age_bins'].value_counts()
    ordered_counts = counts.reindex(
        ['<25', '25-34', '35-44', '45-54', '54+'], fill_value=0)

    # Determine the index of the bar with the highest count
    colors = ['lightgrey' if count != ordered_counts.max(
    ) else '#03c4a1' for count in ordered_counts.values]

    # Create the bar chart with conditional colors
    fig = go.Figure(data=[
        go.Bar(x=ordered_counts.values, y=ordered_counts.index,
               marker_color=colors, orientation='h', width=0.4)
    ])

    # Set the layout
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        margin=dict(l=0, r=0, t=25, b=0),
        autosize=True,
        template='plotly_dark',
        yaxis=dict(
            showline=False,  # Remove the axis line
            showgrid=False,  # Remove the grid lines
            showticklabels=False,  # Remove the tick labels
            zeroline=False,
            linewidth=0,
        ),
        xaxis=dict(
            showline=False,  # Remove the axis line
            showgrid=False,  # Remove the grid lines
            showticklabels=False,  # Remove the tick labels
            zeroline=False,
        ),
        font=dict(size=10),
    )

    return fig
#####################################################################################################


def create_scatter_plot_with_text2(pivot_table, hr):
    # Melt the pivot table to make it suitable for a scatter plot
    melted_df = pivot_table.melt(
        id_vars=['Performance Rating'], var_name='Education Level', value_name='Count')

    melted_df['Education Level'] = melted_df['Education Level'].replace({
        'High School': 'High S',
        'Bachelor': 'Bc',
        'Master': 'Msc'
    })

    # Calculate the percentage for each entry, rounding to the nearest whole number
    melted_df['Percentage'] = melted_df.groupby('Education Level', group_keys=False)[
        'Count'].apply(lambda x: round(x / x.sum() * 100))

    # Normalize the size of the squares for better visualization
    melted_df['Size'] = melted_df['Count'] / melted_df['Count'].max() * 100

    # Identify the max value for each Education Level
    max_values = melted_df.groupby('Education Level')['Count'].idxmax()

    # Identify the global max value (biggest square)
    max_value_idx = melted_df['Count'].idxmax()

    # Create a new column for colors, defaulting to light grey
    melted_df['Color'] = 'lightgrey'

    # Set the color to cyan for the rows with the max value for each education level
    melted_df.loc[max_values, 'Color'] = '#03c4a1'

    # Create the text column, with percentage only for the biggest square
    melted_df['Text'] = ""
    melted_df.loc[max_value_idx,
                  'Text'] = f"{int(melted_df.loc[max_value_idx, 'Percentage'])}%"

    # Create the scatter plot with squares
    fig = go.Figure()

    # Add a scatter trace for each Performance Rating
    for rating in melted_df['Performance Rating'].unique():
        df = melted_df[melted_df['Performance Rating'] == rating]

        fig.add_trace(go.Scatter(
            x=df['Education Level'],
            y=[rating] * len(df),
            mode='markers+text',  # Add text mode
            marker=dict(
                size=df['Size'],
                sizemode='area',
                sizeref=2.*max(melted_df['Size'])/(60.**2),
                sizemin=4,
                color=df['Color'],
                symbol='square'  # Change marker symbol to square
            ),
            # Add percentage text only inside the biggest square
            text=df['Text'],
            textposition="middle center",  # Position the text inside the square
            name=rating
        ))

    # Update layout to ensure correct order of the y-axis and x-axis
    fig.update_layout(
        yaxis=dict(
            tickvals=['Needs Improvement',
                      'Satisfactory', 'Good', 'Excellent'],
            ticktext=['Needs<br>Improvement', 'Satisfactory',
                      'Good', 'Excellent'],  # This will force line break
            showgrid=False
        ),
        xaxis=dict(categoryorder='array', categoryarray=[
                   # Set the x-axis side to top
                   'High S', 'Bc', 'Msc', 'PhD'], side='top', showgrid=False),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
        template='plotly_dark',
        font=dict(size=10),
    )

    return fig


# Example usage
# pivot_table2 = pd.DataFrame({
#     'Performance Rating': ['Needs Improvement', 'Satisfactory', 'Good', 'Excellent'],
#     'High School': [618, 578, 389, 234],
#     'Bachelor': [425, 1619, 2706, 666],
#     'Master': [57, 238, 504, 438],
#     'PhD': [23, 63, 164, 228]
# })
###################################################################################################

def plot_salary_distribution(hr):
    hr['Education Level'] = hr['Education Level'].replace({
        'High School': 'High S',
        'Bachelor': 'Bc',
        'Master': 'Msc'
    })
    # Grouping, calculating mean salary, resetting index, and sorting
    grouped_df = hr.groupby(["Education Level", "Gender"])[
        "Salary"].mean().reset_index()

    sorted_df = grouped_df.sort_values(by=["Education Level", "Salary"])

    # Provided data
    tot = hr.groupby(["Education Level", "Gender"])["Salary"].mean().reset_index(
    ).sort_values(by=["Education Level", "Salary"]).loc[:, ["Education Level", "Salary"]]

    # Calculate min and max salaries for each education level
    min_salaries = tot.groupby("Education Level")["Salary"].min().tolist()
    max_salaries = tot.groupby("Education Level")["Salary"].max().tolist()
    education_levels = tot["Education Level"].unique().tolist()

    # Create a subplot figure with 1 row and 1 column
    fig = make_subplots(rows=1, cols=1)

    # Create traces for each education level (min-max lines)
    for i, education in enumerate(education_levels):
        fig.add_trace(go.Scatter(
            x=[min_salaries[i], max_salaries[i]],
            y=[education, education],
            mode='lines+markers',
            name=education,
            marker=dict(size=31),
            line=dict(width=31, color="grey")
        ), row=1, col=1)

    # Function to convert numbers to K format
    def format_salary(salary):
        return f"  {int(round(salary / 1000, 0))}K"

    # Adding male data (scatter plot) with annotations
    male_salaries = sorted_df[sorted_df["Gender"] == "Male"]["Salary"]
    male_education = sorted_df[sorted_df["Gender"]
                               == "Male"]["Education Level"]

    fig.add_trace(go.Scatter(
        x=male_salaries,
        y=male_education,
        mode='markers+text',
        text=[format_salary(sal) for sal in male_salaries],
        textposition="middle right",
        marker=dict(symbol='diamond-open', color='#03c4a1',
                    line=dict(width=2), size=10),
        name='Male'
    ), row=1, col=1)

    # Adding female data (scatter plot) with annotations
    female_salaries = sorted_df[sorted_df["Gender"] == "Female"]["Salary"]
    female_education = sorted_df[sorted_df["Gender"]
                                 == "Female"]["Education Level"]

    fig.add_trace(go.Scatter(
        x=female_salaries,
        y=female_education,
        mode='markers+text',
        text=[format_salary(sal) for sal in female_salaries],
        textposition="middle right",
        marker=dict(symbol='star-open', color='#03c4a1',
                    line=dict(width=2), size=10),
        name='Female'
    ), row=1, col=1)

    # Setting the layout
    fig.update_layout(
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        margin=dict(l=0, r=0, t=0, b=0),
        template='plotly_dark',
        yaxis=dict(
            showline=False,  # Remove the axis line
            categoryorder='array',
            categoryarray=['PhD', 'Msc', 'Bc', 'High S'],
            showgrid=False,  # Remove the grid lines
        ),
        xaxis=dict(
            showline=False,  # Remove the axis line
            showgrid=False,  # Remove the grid lines
            showticklabels=False,  # Remove the tick labels
        ),
        font=dict(size=10),
    )

    # Show the combined plot
    return fig

##################################################################################################


def create_scatter_plot(hr):
    """
    Creates a scatter plot showing the relationship between age and salary for different job titles.

    Parameters:
        hr_data (pd.DataFrame): DataFrame containing HR data with 'Job Title', 'Age', and 'Salary' columns.

    Returns:
        plotly.graph_objects.Figure: The scatter plot figure.
    """

    # Convert Birthdate to datetime
    hr['Birthdate'] = pd.to_datetime(hr['Birthdate'], format="%d/%m/%Y")

    # Get today's date
    today = pd.to_datetime('today')

    # Calculate the age correctly
    hr['Age'] = today.year - hr['Birthdate'].dt.year - (
        (today.month < hr['Birthdate'].dt.month) |
        ((today.month == hr['Birthdate'].dt.month)
         & (today.day < hr['Birthdate'].dt.day))
    )

    # Group by 'Job Title' and calculate the mean 'Age' and 'Salary'
    hr_grouped = hr.groupby('Job Title')[
        ['Age', 'Salary']].mean().reset_index()

    # Calculate the mean values
    mean_age = hr_grouped['Age'].mean()
    mean_salary = hr_grouped['Salary'].mean()

    # Creating the scatter plot
    fig = go.Figure(data=go.Scatter(
        x=hr_grouped['Age'],  # Age on the x-axis
        y=hr_grouped['Salary'],  # Salary on the y-axis
        mode='markers+text',  # Add text labels to the markers
        marker=dict(
            # Adjust the size scaling as necessary
            size=hr_grouped['Salary'] / 10000,
            color='#03c4a1',  # Set the marker color to cyan
            symbol='diamond',  # Set the marker shape to diamond
            line=dict(
                color='#03c4a1',  # Set the border color to cyan
                width=2  # Adjust the width of the border as needed
            )
        ),
        text=hr_grouped['Job Title'],  # Adding job titles as text
        textposition='top center',  # Positioning the text above the markers
        textfont=dict(
            size=10  # Set the font size for the text labels
        )
    ))

    # Update the layout for better readability
    fig.update_layout(
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',  # Transparent background
        plot_bgcolor='rgba(0,0,0,0)',    # Transparent plot background
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
        template='plotly_dark',
        yaxis=dict(
            showline=True,  # Remove the axis line
            showgrid=False,  # Remove the grid lines
            linecolor="grey",
            title="Salary"
        ),
        xaxis=dict(
            showline=True,  # Remove the axis line
            showgrid=False,  # Remove the grid lines
            linecolor="grey",
            title="Age"
        ),
        font=dict(size=10),
        shapes=[
            # Mean salary line (horizontal dashed line)
            dict(
                type="line",
                x0=30, y0=mean_salary,
                x1=hr_grouped['Age'].max(), y1=mean_salary,
                line=dict(color="grey", width=1, dash="dash")
            ),
            # Mean age line (vertical dashed line)
            dict(
                type="line",
                x0=mean_age, y0=56000,
                x1=mean_age, y1=hr_grouped['Salary'].max(),
                line=dict(color="grey", width=1, dash="dash")
            )
        ]
    )

    return fig


# create_scatter_plot(hr)
