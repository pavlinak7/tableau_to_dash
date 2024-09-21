from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from dataFunctions.dataProcessing import *
from config import *

def apply_common_layout(fig: go.Figure) -> go.Figure:
    """
    Apply common layout settings to a Plotly figure for consistent styling.

    Parameters:
    fig (go.Figure): Plotly figure to apply the layout to.

    Returns:
    go.Figure: Updated figure with common layout settings.
    """
    fig.update_layout(
        paper_bgcolor=PLOT_CONFIG['paper_bgcolor'],
        plot_bgcolor=PLOT_CONFIG['plot_bgcolor'],
        template=PLOT_CONFIG['template'],
        font=dict(size=PLOT_CONFIG['font_size']),
    )
    return fig


def create_blank_figure():
    fig = go.Figure(go.Scatter(x=[], y=[]))
    fig.update_layout(
        paper_bgcolor='black',
        plot_bgcolor='black',
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        margin=dict(l=0, r=0, t=0, b=0)
    )
    return fig
############################################################################
#pomocná funkce ke graf1 a graf2
def create_trend_figure(hr: pd.DataFrame, date_column: str, line_color: str, fill_color: str) -> go.Figure:
    """
    Create a Plotly figure showing the trend (hires or terminations) per year.

    Parameters:
    hr (pd.DataFrame): DataFrame with a date column of datetime type.
    date_column (str): The name of the date column (either 'Hiredate' or 'Termdate').
    line_color (str): The line color for the trend.
    fill_color (str): The fill color for the area under the line.

    Returns:
    go.Figure: A Plotly figure object.
    """
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=sorted(hr[date_column].dt.year.unique()),  # Sorted years
        y=hr.groupby(hr[date_column].dt.year).size().reset_index(name='Count').loc[:, "Count"],  # Corresponding counts
        mode='lines',
        line=dict(color=line_color),
        fill='tozeroy',  # Fill the area under the line
        fillcolor=fill_color
    ))

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
        #width=100,
        #height=65,
    )

    fig.update_xaxes(
        visible=False,
        showticklabels=False
    )

    fig.update_yaxes(
        visible=False,
        showticklabels=False
    )

    return apply_common_layout(fig)

#graf1
def create_hire_trend_figure(hr: pd.DataFrame) -> go.Figure:
    return create_trend_figure(hr, 'Hiredate', '#03c4a1', 'rgba(3, 196, 161, 0.2)')

#graf2
def create_termination_trend_figure(hr: pd.DataFrame) -> go.Figure:
    hr = hr.loc[hr.Termdate.notnull(), :]
    return create_trend_figure(hr, 'Termdate', '#c62b88', 'rgba(198, 43, 136, 0.2)')

#############################################################################################################
#graf3
def plot_department_termination(hr: pd.DataFrame) -> go.Figure:
    """
    Create a horizontal stacked bar chart showing the number of employees who left or stayed by department.

    Parameters:
    hr (pd.DataFrame): DataFrame containing HR data with 'Department' and 'skoncil' columns.

    Returns:
    go.Figure: A Plotly figure object.
    """

    grouped_df = hr.groupby(['Department', 'skoncil'], observed=True).size().reset_index(name='Count')

    pivot_df = grouped_df.pivot(index='Department', columns='skoncil', values='Count').fillna(0)

    # Ensure the correct order of columns and handle missing columns
    if 'ne' not in pivot_df.columns:
        pivot_df['ne'] = 0
    if 'ano' not in pivot_df.columns:
        pivot_df['ano'] = 0

    pivot_df = pivot_df[['ne', 'ano']]
    pivot_df = pivot_df.sort_values(by=['ne', 'ano'], ascending=[True, True])

    colors = ['#03c4a1', '#c62b88']

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
            textfont=dict(size=10),
            cliponaxis=False  # Allows text to be outside the bar
        ))

    # Add custom department labels on the left
    annotations = [
        dict(
            x=0,
            y=i,
            xref="paper",
            yref="y",
            text=department,
            showarrow=False,
            xanchor='left',
            xshift=-100
        ) for i, department in enumerate(pivot_df.index)
    ]

    fig.update_layout(
        barmode='stack',
        margin=dict(l=120, r=20, t=0, b=0),
        autosize=True,
        #width=390,
        showlegend=False,
        annotations=annotations,
    )

    fig.update_yaxes(
        automargin=True,  # Ensures that labels don't overlap with the plot
        showticklabels=False
    )

    fig.update_xaxes(
        visible=False,
        showticklabels=False
    )

    return apply_common_layout(fig)

############################################################################################################
#graf4
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

def get_coords(city, state):
    return city_coords.get(f'{city}, {state}', (None, None))
hr['latitude'], hr['longitude'] = zip(*hr.apply(lambda row: get_coords(row['City'], row['State']), axis=1))

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
    city_counts = dataframe.groupby([city_col, state_col, lat_col, lon_col]).size().reset_index(name='count')

    fig = go.Figure()

    fig.add_trace(go.Scattergeo(
        lat=city_counts[lat_col],
        lon=city_counts[lon_col],
        mode='markers',
        marker=dict(
            size=city_counts['count'],
            sizemode='area',
            sizeref=2.*max(city_counts['count']) / \
            (20.**2),  # Adjust the size scaling
            symbol='circle',
            color='rgba(3, 196, 161, 0.2)',
            line=dict(width=1, color='rgba(3, 196, 161, 1)')
        ),
        showlegend=False,
        text=city_counts[city_col] + ', ' + city_counts[state_col] + \
        ': ' + city_counts['count'].astype(str),
        hoverinfo='text'
    ))

    # Highlight the state of New York with cyan color
    fig.add_trace(go.Choropleth(
        locations=['NY'],
        locationmode='USA-states',
        z=[1],  # Dummy variable for coloring
        colorscale=[[0, 'rgba(0, 255, 255, 0.2)'], [1, 'rgba(3, 196, 161, 0.2)']],
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
        paper_bgcolor='black',
        plot_bgcolor='black',
    )

    return fig
####################################################################################################
#graf5
def plot_lokace_distribution(hr):
    """
    Creates a bar plot showing the distribution of values in the specified column.

    Parameters:
        hr (pd.DataFrame): The DataFrame containing the data.

    Returns:
        fig (go.Figure): The Plotly Figure object.
    """
    count_data = hr["lokace"].value_counts().reset_index()
    count_data.columns = ["lokace", 'count']

    total_count = count_data['count'].sum()
    count_data['percentage'] = (count_data['count'] / total_count) * 100

    colors = ['#03c4a1' if loc == 'HQ' else 'grey' for loc in count_data['lokace']]

    fig = go.Figure(go.Bar(
        x=count_data["lokace"],
        y=count_data['count'],
        marker_color=colors,
        width=0.6
    ))

    annotations = [
        dict(
            x=row["lokace"],
            y=-0.05 * total_count,
            text=f"{int(round(row['percentage'], 0))}%",
            showarrow=False,
            yanchor="top",
            xanchor="center",
            textangle=-90
        ) for _, row in count_data.iterrows()
    ]

    fig.update_layout(
        annotations=annotations,
        margin=dict(l=0, r=0, t=0, b=0),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(side="top"),
        showlegend=False,
    )

    return apply_common_layout(fig)

##########################################################################################################
#graf6
def generate_donut_charts(hr_df):
    hr_df["skoncil"] = hr_df.Termdate.apply(lambda x: "ne" if pd.isna(x) else "ano")

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
        fig = go.Figure(
            data=[
                go.Pie(
                    labels=['Active', 'Inactive'],
                     values=[active_pct, inactive_pct],
                     hole=.7,
                     textinfo='percent',
                     textposition='outside'
                     )
            ]
        )

        fig.update_traces(
            marker=dict(colors=['#03c4a1', '#c62b88'])
        )
        fig.update_layout(
            showlegend=False,
              annotations=[
                  dict(text=f'{int(total_pct)}%', x=0.5,
                       y=0.5, font_size=10, showarrow=False),
                  dict(text=gender_label, x=-0.14, y=0.5,
                       font_size=10, showarrow=False, textangle=-90)
              ],
              #paper_bgcolor='rgba(0,0,0,0)',
              #template='plotly_dark',
              margin=dict(l=0, r=0, t=20, b=15),
              #font=dict(size=10)
              )
        return apply_common_layout(fig)

    men_active_pct, men_inactive_pct, men_total_pct = calculate_percentages('Male')
    women_active_pct, women_inactive_pct, women_total_pct = calculate_percentages('Female')

    fig_men = create_donut_chart(men_active_pct, men_inactive_pct, men_total_pct, 'Male')
    fig_women = create_donut_chart(women_active_pct, women_inactive_pct, women_total_pct, 'Female')

    return fig_men, fig_women
#######################################################################################################
# Common utility function for coloring bars
def get_bar_colors(data, highlight_color='#03c4a1', default_color='lightgrey'):
    """
    Returns a list of colors for bars, highlighting the maximum value.

    Parameters:
    - data: A list or series of numeric values.
    - highlight_color: Color to use for the highest bar.
    - default_color: Color to use for the other bars.

    Returns:
    - List of colors with the highlight color applied to the maximum value.
    """
    max_value = data.max()
    return [highlight_color if value == max_value else default_color for value in data]

#graf7_1
def create_scatter_plot_with_text(pivot_table):
    melted_df = pivot_table.melt(id_vars=['Age_bins'], var_name='Education Level', value_name='Count')

    # Normalize the size of the circles for better visualization
    melted_df['Size'] = melted_df['Count'] / melted_df['Count'].max() * 100

    melted_df['Education Level'] = melted_df['Education Level'].replace({
        'High School': 'High S',
        'Bachelor': 'Bc',
        'Master': 'Msc'
    })

    max_row = melted_df.loc[melted_df['Count'].idxmax()] # row with the maximum Count

    # Calculate the percentage for the maximum value
    max_percentage = round((max_row['Count'] / melted_df['Count'].sum()) * 100, 0)

    fig = go.Figure()

    for age_bin in melted_df['Age_bins'].unique():
        df = melted_df[melted_df['Age_bins'] == age_bin]

        # Determine the text for each point
        text = [f"{int(max_percentage)}%" if (row['Education Level'] == max_row['Education Level']) and
                                             (age_bin == max_row['Age_bins']) else "" for _, row in df.iterrows()]


        fig.add_trace(go.Scatter(
            x=df['Education Level'],
            y=[age_bin] * len(df),
            mode='markers+text',
            marker=dict(
                size=df['Size'],
                sizemode='area',
                sizeref=2.*max(melted_df['Size'])/(60.**2)*5, # <----- zmenšení pětky -> větší kruhy
                sizemin=4,
                color=['#03c4a1' if (row['Education Level'] == max_row['Education Level']) and
                       (age_bin == max_row['Age_bins']) else "#a6a5a2" for _, row in df.iterrows()]
            ),
            text=text,  # Set the text for each point
            textposition="middle center",  # Position the text inside the circle
            name=age_bin
        ))

    fig.update_layout(
        yaxis=dict(
            categoryorder='array',
            categoryarray=['54+', '45-54', '35-44', '25-34', '<25'],
            showgrid=False,
                   ),
        xaxis=dict(
            categoryorder='array',
            categoryarray=['High S', 'Bc', 'Msc', 'PhD'],
            side='top',
            showgrid=False
        ),
        showlegend=False,
        margin=dict(l=0, r=0, t=20, b=0),
        autosize=True,
    )

    return apply_common_layout(fig)
# ----------------------------------------------------------------------------
#graf7_2
def create_education_level_chart(hr):
    """
    Creates a bar chart of the Education Level distribution with a special color for the highest bar.

    Parameters:
    hr_data (DataFrame): The DataFrame containing the 'Education Level' column.

    Returns:
    fig (Figure): A Plotly figure object representing the bar chart.
    """
    counts = hr['Education Level'].value_counts()
    ordered_counts = counts.reindex(['High School', 'Bachelor', 'Master', 'PhD'], fill_value=0)

    # Determine the index of the bar with the highest count
    colors = get_bar_colors(ordered_counts)

    # Create the bar chart with conditional colors
    fig = go.Figure(
        data=[
            go.Bar(
                x=ordered_counts.index,
                y=ordered_counts.values,
               marker_color=colors,
                width=0.3
            )
        ]
    )

    fig.update_layout(
        margin=dict(l=30, r=0, t=0, b=0),
        autosize=True,
        yaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=False,
            zeroline=False,
            linewidth=0,
        ),
        xaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=False,
            zeroline=False,
            linewidth=0,
        )
    )

    return apply_common_layout(fig)
# --------------------------------------------------------------------------
#graf7_3
def create_age_distribution_chart(hr):
    counts = hr['Age_bins'].value_counts()
    ordered_counts = counts.reindex(['<25', '25-34', '35-44', '45-54', '54+'], fill_value=0)

    # Determine the index of the bar with the highest count
    colors = get_bar_colors(ordered_counts)

    # Create the bar chart with conditional colors
    fig = go.Figure(
        data=[
            go.Bar(
                x=ordered_counts.values,
                y=ordered_counts.index,
               marker_color=colors,
                orientation='h',
                width=0.4
            )
        ]
    )

    fig.update_layout(
        margin=dict(l=0, r=0, t=25, b=0),
        autosize=True,
        yaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=False,
            zeroline=False,
            linewidth=0,
        ),
        xaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=False,
            zeroline=False,
        ),
        font=dict(size=10),
    )

    return apply_common_layout(fig)
#####################################################################################################
#graf8
def create_scatter_plot_with_text2(pivot_table):
    melted_df = pivot_table.melt( id_vars=['Performance Rating'], var_name='Education Level', value_name='Count')

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

    melted_df['Color'] = 'lightgrey'

    melted_df.loc[max_values, 'Color'] = '#03c4a1'

    # Create the text column, with percentage only for the biggest square
    melted_df['Text'] = ""
    melted_df.loc[max_value_idx,'Text'] = f"{int(melted_df.loc[max_value_idx, 'Percentage'])}%"

    fig = go.Figure()

    for rating in melted_df['Performance Rating'].unique():
        df = melted_df[melted_df['Performance Rating'] == rating]

        fig.add_trace(go.Scatter(
            x=df['Education Level'],
            y=[rating] * len(df),
            mode='markers+text',
            marker=dict(
                size=df['Size'],
                sizemode='area',
                sizeref=2.*max(melted_df['Size'])/(60.**2),
                sizemin=4,
                color=df['Color'],
                symbol='square'
            ),
            # Add percentage text only inside the biggest square
            text=df['Text'],
            textposition="middle center",
            name=rating
        ))

    fig.update_layout(
        yaxis=dict(
            tickvals=['Needs Improvement','Satisfactory', 'Good', 'Excellent'],
            ticktext=['Needs<br>Improvement', 'Satisfactory','Good', 'Excellent'],
            showgrid=False
        ),
        xaxis=dict(categoryorder='array', categoryarray=[
                   # Set the x-axis side to top
                   'High S', 'Bc', 'Msc', 'PhD'], side='top', showgrid=False),
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
    )

    return apply_common_layout(fig)
###################################################################################################
#graf9
def plot_salary_distribution(hr):
    hr['Education Level'] = hr['Education Level'].replace({
        'High School': 'High S',
        'Bachelor': 'Bc',
        'Master': 'Msc'
    })

    grouped_df = hr.groupby(["Education Level", "Gender"])["Salary"].mean().reset_index()
    sorted_df = grouped_df.sort_values(by=["Education Level", "Salary"])

    salary_range_df = hr.groupby(["Education Level", "Gender"])["Salary"].mean().reset_index()
    min_salaries = salary_range_df.groupby("Education Level")["Salary"].min().tolist()
    max_salaries = salary_range_df.groupby("Education Level")["Salary"].max().tolist()
    education_levels = salary_range_df["Education Level"].unique().tolist()

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
    male_education = sorted_df[sorted_df["Gender"]== "Male"]["Education Level"]

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
    female_education = sorted_df[sorted_df["Gender"] == "Female"]["Education Level"]

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

    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        yaxis=dict(
            showline=False,  # Remove the axis line
            categoryorder='array',
            categoryarray=['PhD', 'Msc', 'Bc', 'High S'],
            showgrid=False,
        ),
        xaxis=dict(
            showline=False,
            showgrid=False,
            showticklabels=False,
        ),
    )

    return apply_common_layout(fig)
##################################################################################################
#graf10
def create_scatter_plot(hr):
    """
    Creates a scatter plot showing the relationship between age and salary for different job titles.

    Parameters:
        hr (pd.DataFrame): DataFrame containing HR data with 'Job Title', 'Age', and 'Salary' columns.

    Returns:
        plotly.graph_objects.Figure: The scatter plot figure.
    """
    hr_grouped = hr.groupby('Job Title')[['Age', 'Salary']].mean().reset_index()

    mean_age = hr_grouped['Age'].mean()
    mean_salary = hr_grouped['Salary'].mean()

    fig = go.Figure(
            data=go.Scatter(
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
        )
    )

    fig.update_layout(
        showlegend=False,
        margin=dict(l=0, r=0, t=0, b=0),
        autosize=True,
        yaxis=dict(
            showline=True,
            showgrid=False,
            linecolor="grey",
            title="Salary"
        ),
        xaxis=dict(
            showline=True,
            showgrid=False,
            linecolor="grey",
            title="Age"
        ),
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

    return apply_common_layout(fig)

