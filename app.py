#-------------------Imports--------------#
import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
import warnings
warnings.filterwarnings('ignore')
import base64

import json


#-------------------Variables from json--------------#
contributing_factors_ALL_top = pd.read_json('data/contributing_factors_ALL_top.json')
contributing_factors_BRONX_top = pd.read_json('data/contributing_factors_BRONX_top.json')
contributing_factors_BROOKLYN_top = pd.read_json('data/contributing_factors_BROOKLYN_top.json')
contributing_factors_MANHATTAN_top = pd.read_json('data/contributing_factors_MANHATTAN_top.json')
contributing_factors_QUEENS_top = pd.read_json('data/contributing_factors_QUEENS_top.json')
contributing_factors_STATENISLAND_top = pd.read_json('data/contributing_factors_STATENISLAND_top.json')

contributing_factors_BRONX_top7 = pd.read_json('data/contributing_factors_BRONX_top7.json')
contributing_factors_BROOKLYN_top7 = pd.read_json('data/contributing_factors_BROOKLYN_top7.json')
contributing_factors_MANHATTAN_top7 = pd.read_json('data/contributing_factors_MANHATTAN_top7.json')
contributing_factors_QUEENS_top7 = pd.read_json('data/contributing_factors_QUEENS_top7.json')
contributing_factors_STATENISLAND_top7 = pd.read_json('data/contributing_factors_STATENISLAND_top7.json')


visual = pd.read_json('data/visual.json')

street_data_full = pd.read_json('data/street_data_full.json')

frequent_collisions_2018 = pd.read_json('data/frequent_collisions_2018.json')

chloropleth = pd.read_json('data/chloropleth.json')

heatmap_data_0 = pd.read_json('data/hours/heatmap_data_0.json')
heatmap_data_1 = pd.read_json('data/hours/heatmap_data_1.json')
heatmap_data_2 = pd.read_json('data/hours/heatmap_data_2.json')
heatmap_data_3 = pd.read_json('data/hours/heatmap_data_3.json')
heatmap_data_4 = pd.read_json('data/hours/heatmap_data_4.json')
heatmap_data_5 = pd.read_json('data/hours/heatmap_data_5.json')
heatmap_data_6 = pd.read_json('data/hours/heatmap_data_6.json')
heatmap_data_7 = pd.read_json('data/hours/heatmap_data_7.json')
heatmap_data_8 = pd.read_json('data/hours/heatmap_data_8.json')
heatmap_data_9 = pd.read_json('data/hours/heatmap_data_9.json')
heatmap_data_10 = pd.read_json('data/hours/heatmap_data_10.json')
heatmap_data_11 = pd.read_json('data/hours/heatmap_data_11.json')
heatmap_data_12 = pd.read_json('data/hours/heatmap_data_12.json')
heatmap_data_13 = pd.read_json('data/hours/heatmap_data_13.json')
heatmap_data_14 = pd.read_json('data/hours/heatmap_data_14.json')
heatmap_data_15 = pd.read_json('data/hours/heatmap_data_15.json')
heatmap_data_16 = pd.read_json('data/hours/heatmap_data_16.json')
heatmap_data_17 = pd.read_json('data/hours/heatmap_data_17.json')
heatmap_data_18 = pd.read_json('data/hours/heatmap_data_18.json')
heatmap_data_19 = pd.read_json('data/hours/heatmap_data_19.json')
heatmap_data_20 = pd.read_json('data/hours/heatmap_data_20.json')
heatmap_data_21 = pd.read_json('data/hours/heatmap_data_21.json')
heatmap_data_22 = pd.read_json('data/hours/heatmap_data_22.json')
heatmap_data_23 = pd.read_json('data/hours/heatmap_data_23.json')

image_filename = 'plot1.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
image_filename1 = 'plot2.png' # replace with your own image
encoded_image1 = base64.b64encode(open(image_filename1, 'rb').read())
image_filename2 = 'plot3.png' # replace with your own image
encoded_image2 = base64.b64encode(open(image_filename2, 'rb').read())

## options
hour_options = [heatmap_data_0,heatmap_data_1,heatmap_data_2,heatmap_data_3,heatmap_data_4,heatmap_data_5,heatmap_data_6,heatmap_data_7,heatmap_data_8,heatmap_data_9,heatmap_data_10,heatmap_data_11,heatmap_data_12,heatmap_data_13,heatmap_data_14,heatmap_data_15,heatmap_data_16,heatmap_data_17,heatmap_data_18,heatmap_data_19,heatmap_data_20,heatmap_data_21,heatmap_data_22,heatmap_data_23]
brh_options = ['BROOKLYN', 'MANHATTAN', 'BRONX', 'STATEN ISLAND', 'QUEENS', 'All Boroughs']
severity_options = ['Total collisions', 'Injured', 'Killed']
borough_options = ['BROOKLYN', 'BRONX', 'STATEN ISLAND', 'QUEENS', 'MANHATTAN']
year_options = ['2013','2014','2015','2016','2017','2018','2019','2020','2021']
week_options = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53']
hour_marks = np.arange(0,24)
street_options = street_data_full['ON STREET NAME'].unique()


#Filtering 
for i in range(0, len(hour_options)):
    hour_options[i]['CRASH DATE'] = pd.to_datetime(hour_options[i]['CRASH DATE'])
    hour_options[i]['CRASH TIME'] = pd.to_datetime(hour_options[i]['CRASH TIME'])
    hour_options[i]['Year'] = hour_options[i]['CRASH DATE'].dt.year
    hour_options[i]['Week'] = hour_options[i]['CRASH DATE'].dt.week
    hour_options[i]['WeekDay'] = hour_options[i]['CRASH DATE'].dt.weekday
    hour_options[i]['Hr'] = hour_options[i]['CRASH TIME'].dt.hour

    hour_options[i]['Year'] = hour_options[i]['Year'].astype('str')
    hour_options[i]['Hr'] = hour_options[i]['Hr'].astype('str')
    hour_options[i]['Week'] = hour_options[i]['Week'].astype('str')
    hour_options[i]['WeekDay'] = hour_options[i]['WeekDay'].astype('str')

# Data for all hours
heat_data_all_hours = pd.concat(hour_options)

street_data_full['Year'] = street_data_full['Year'].astype('str')
street_data_full['Hr'] = street_data_full['Hr'].astype('str')
street_data_full['Week'] = street_data_full['Week'].astype('str')
street_data_full['WeekDay'] = street_data_full['WeekDay'].astype('str')



#figures
img = 'plot1.png'
fig1 = px.bar(visual, x="CONTRIBUTING FACTOR VEHICLE 1",y = "Accident_count", width=800, height=400,title="Top Contributing Factor for Accidents")
fig1.update_layout(
    yaxis_title="Number of Accidents",
    xaxis_title="CONTRIBUTING FACTOR VEHICLE 1",
    autosize=True,
    width=600,
    height=600,
    )

x_center=frequent_collisions_2018.LATITUDE.mean()
y_center=frequent_collisions_2018.LONGITUDE.mean()
fig2 = px.scatter_mapbox(frequent_collisions_2018, lat='LATITUDE', lon='LONGITUDE',
                            center=dict(lat=x_center, lon=y_center), zoom=9, opacity=1.0,
                            mapbox_style="open-street-map", height=500)

fig2.update_traces(
        text=frequent_collisions_2018[['0']],
        hovertemplate='Accidents in 2018: %{text[0]}')
fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

temp1 = chloropleth.iloc[0].copy()
temp2 = chloropleth.iloc[1].copy()
temp3 = chloropleth.iloc[2].copy()
temp4 = chloropleth.iloc[3].copy()
temp5 = chloropleth.iloc[4].copy()
chloropleth.iloc[0] = temp5
chloropleth.iloc[1] = temp4
chloropleth.iloc[2] = temp2
chloropleth.iloc[3] = temp3
chloropleth.iloc[4] = temp1


nycmap = json.load(open("data/boroughs.geojson"))
# create new columns in df for area and density  

# call Plotly Express choropleth function to visualize data
fig3 = px.choropleth_mapbox(chloropleth,
                           geojson=nycmap,
                           locations=chloropleth.index,
                           color='Accident/Square Km',
                           color_continuous_scale="Reds",
                           mapbox_style="open-street-map",
                           zoom=9, center={"lat": 40.7, "lon": -73.9},
                           opacity=0.7,
                           hover_name="BOROUGH"
                           )

fig3.update_traces(
        text=chloropleth[['BOROUGH','Accident/Square Km']],
        hovertemplate='Borough: %{text[0]} <br> Accident/Square Km: %{text[1]}')
fig3.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


#------------------Dash app-----------------#
app = dash.Dash(__name__)
server = app.server

colors = {
    'background': '#b4e6ed',
    'text': '#111111'
}


app.layout = html.Div(style={ 'font-family':'Sans-Serif',
                             'color': colors['text'],  
                             'width':'80%', 'height':'100%', 
                             'margin-left':'auto',
                             'margin-right':'auto',
                            }, 
    children=[

    
    # header of page
    html.H1('Vehicle Collisions in New York City', style={'text-align': 'center',
                                                            'background': colors['background']}),

    # some text (introduction)
    dcc.Markdown(children='''
            This webpage gives you a visual experience of the collisions in the city of New York. There is a mix of a plethora of different analytic and interactive visualizations giving you  interesting insights as well as a lot of possibilities to explore the dataset for yourself.
        ''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),

    # plot 1
    html.Img(src='data:image/png;base64,{}'.format(encoded_image.decode()), style={'margin-right':'auto', 
                                                                                   'margin-left':'auto',
                                                                                   'width':'60%',
                                                                                   'display':'flex'}),

    # some text (introduction)
    dcc.Markdown(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac. Mauris nec velit diam. Vivamus nec vestibulum augue. Aliquam et feugiat dui. Integer id dui venenatis, tristique ipsum vel, dapibus turpis.
        ''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),

    ## bokeh plot here
    html.Iframe(src="https://www.student.dtu.dk/~s202094/bokeh/plot.html",
                style={"width": "1000px",
                        "height": "600px",
                        'margin-left': 'auto',
                        'margin-right': 'auto',
                        'display':'block'}),


    ## plot 2
    html.Img(src='data:image/png;base64,{}'.format(encoded_image1.decode()), style={'margin-right':'auto', 
                                                                                    'margin-left':'auto',
                                                                                    'width':'60%',
                                                                                    'display':'flex'}),

    # some text (introduction)
    dcc.Markdown(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac. Mauris nec velit diam. Vivamus nec vestibulum augue. Aliquam et feugiat dui. Integer id dui venenatis, tristique ipsum vel, dapibus turpis.
        ''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),


    ## plot 3
    html.Img(src='data:image/png;base64,{}'.format(encoded_image2.decode()), style={'margin-right':'auto', 
                                                                                    'margin-left':'auto',
                                                                                    'width':'60%',
                                                                                    'display':'flex'}),

    # title for contributing factors bar chart
    html.H2('Collisions and their contributing factors', style={'text-align': 'center',
                                                                'padding-top': '50px'}),

    # some text
    dcc.Markdown(children='''
        New York is divided into 5 Boroughs. Each one of them is very different in terms of their area, population density and “purpose”. So, each Borough is also very different when it comes to motor vehicle collisions. Through an interactive visualization, you can select a particular Borough and look at the number of collisions as well as the injuries and deaths across all the different reasons for a collision.
        For all Boroughs, speeding violations result in the highest number fatalities even though the number of collisions due to it are relatively low. Even Driver Inattention which has by far the highest number of collisions (6 times more than over speeding), has lower number of deaths. So, a very strict curb on speeding is definitely impending.
        ''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),

    # Dropdown menu for Boroughs
    html.Div(dcc.Dropdown(
            id='Borough',
            options=[{
                'label': i,
                'value': i
            } for i in brh_options],
            value='All Boroughs'),
            style={'width': '25%',
                   'margin-left': '10%'}),

    # interactive contributing factors bar chart
    html.Div(dcc.Graph(
        id='collision-graph1'
    ),  style={'width': '80%',
                'margin-left': 'auto', 
                'margin-right': 'auto',
                'position': 'relative'}),
    
    # some text
    dcc.Markdown(children='''
        Looking closer at collisions, injuries and deaths for the top 7 reasons for collisions we can see how it is distributed across each borough.
        ''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),

    # Dropdown menu for Collisions, injured, killed
    html.Div(dcc.Dropdown(
            id='Severity',
            options=[{
                'label': i,
                'value': i
            } for i in severity_options],
            value='Total collisions'),
            style={'width': '25%',
                   'margin-left': '10%'}),

    # interactive collision bar chart
    html.Div(dcc.Graph(
        id='collision-graph2'
    ),  style={'width': '80%',
                'margin-left': 'auto', 
                'margin-right': 'auto',
                'position': 'relative'}),
    

    # title for contributing factors bar chart
    html.H2('Geographical Analysis', style={'text-align': 'center',
                                            'padding-top': '50px'}),

    
    # some text
    dcc.Markdown(children='''
        The idea is to give you different geographical visualizations to be able to see and understand Motor Vehicle Collisions in the city of New York. Starting from the bird eye's view and narrowing it down to the very latitude and longitude of any collision, also giving the user the options to filter the visuals by Year, Week, Day and even the hour.        
        <br>
        Following 2 visuals were built to give you an idea of the power of seeing geographical data on the map.''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),

    html.H3('Collisions per square Km (2019)', style={'text-align': 'center'}),

     # some text
    dcc.Markdown(children='''
        The previous bar graph which compares the collisions across Boroughs does not paint the complete picture as the area of these Boroughs is very different. So, we look collision per square Km in this chloropleth below.        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),

    # chloropleth
    html.Div(dcc.Graph(
        id='graph5',
        figure=fig3,
    ),  style={'width': '80%',
              'margin-left': 'auto', 
              'margin-right': 'auto', 
              'padding-bottom':'20px'}),

    # some text
    dcc.Markdown(children='''
        As expected, Manhattan (often refered to as the centre of the modern world) is the most dangerous areas when it comes to driving in the city of New York followed by Brooklyn and then Bronx. Brooklyn though, has the highest number of accidents.        '''
        , style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),

    # some text
    dcc.Markdown(children='''
        The following graph reveals top 100 locations with the highest number of collisions in the city of New York..
        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),


    # title for dangerous intersections
    html.H2('Most dangerous intersections in 2018', style={'text-align': 'center'}),
    
    # most dangerous intersections
    html.Div(dcc.Graph(
        id='graph4',
        figure=fig2,
    ),  style={'width': '80%',
              'margin-left': 'auto', 
              'margin-right': 'auto', 
              'padding-bottom':'20px'}),

    # some text
    dcc.Markdown(children='''
        Now, its time for you to leverage this power. Following series of interactive geographical visualizations will enable you to do all kinds of adhoc analysis by yourself.
        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),
    
    # title for heatmap
    html.H3('Heat Map', style={'text-align': 'center'}),

     # some text
    dcc.Markdown(children='''
        Having had a bird view of the data, its time to get hands dirty. Looking at a heat map of the collisions with the option to filter a borough, an year and even the week. Furthermore, you can also slide through the hours of the day to at the changing accident density across the day.
        So, you can just filter a Borough, the year, week and even the day to look at the hotspots for collisions and take necessary measures.
        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),
    
    #labels for drop down menus
    html.Div(children=[
        html.Div([
            html.Label(['Select Borough'], style={'font-weight': 'bold', "text-align": "right"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Year'], style={'font-weight': 'bold', "text-align": "center"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Week'], style={'font-weight': 'bold', "text-align": "center"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Weekday'], style={'font-weight': 'bold',"text-align": "left"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
    ],style={'margin-left': '10%','margin-right': '10%'}),

    #Dropdown menus for heatmap
    html.Div(children=[
        #Dropdown menu for Borough
        html.Div(
            dcc.Dropdown(
            id='borough_heatmap',
            options=[{
                'label': i,
                'value': i
            } for i in borough_options],
            value='MANHATTAN',  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for year
        html.Div(dcc.Dropdown(
            id='year_heatmap',
            options=[{
                'label': i,
                'value': i
            } for i in year_options],
            value='2019',  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for Week
        html.Div(dcc.Dropdown(
            id='week_heatmap',
            options=[{
                'label': i,
                'value': i
            } for i in week_options],
            value=['1', '2','3', '4'],  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for weekday
        html.Div(dcc.Dropdown(
            id='day_heatmap',
            options=[
                {'label': 'Monday', 'value': '0'},
                {'label': 'Tuesday', 'value': '1'},
                {'label': 'Wednesday', 'value': '2'},
                {'label': 'Thursday', 'value': '3'},
                {'label': 'Friday', 'value': '4'},
                {'label': 'Saturday', 'value': '5'},
                {'label': 'Sunday', 'value': '6'}
            ],
            value=['0', '1', '2', '3', '4', '5','6'],  
            multi=True),
            style={'width': '25%',  'display': 'inline-block'}
        ),
    ], style={'margin-left': '10%', 
              'margin-right': '10%', 
              'padding-bottom':'20px'}),

    # Heatmap
    html.Div(dcc.Graph(
        id='heatmap-graph-time',
    ), style={'width': '80%',
              'margin-left': 'auto', 
              'margin-right': 'auto', 
              'padding-bottom':'20px'}),

    ## Radio button to choose betweeen all day or hour slider
    html.Div([
        dcc.RadioItems(
            id='allDay_radioButton',
            options=[
                {'label': 'All day', 'value': '0'},
                {'label': 'Choose hour', 'value': '1'},
            ],
            value='1',
            style={'padding-bottom':'10px'}
        ), 
        ## Slider for heatmap
        html.Div(id='slider-container',children=[
            dcc.Slider(
                id='crossfilter-hour-slider',
                min=0,
                max=23,
                value=0,
                marks=hour_marks,
                step=None,
                updatemode='drag'
        )], style={'display': 'block'}), 
    ], style={'width': '75%',
              'margin-left': '10%', 
              'margin-right': '15%'}),

    #labels for hour slider
    html.Div(id='slider-label-container',children=[
        html.Div([
            html.Label(['Select Hour of day'], style={'font-weight': 'bold', "text-align": "right"}),
        ], style={'width': '90%', 'display': 'inline-flex', 'justify-content':'center'}),
    ],style={'margin-left': '20%','margin-right': '10%'}),


    # title for Latitude Longitude Marker
    html.H3('Latitude Longitude Marker', style={'text-align': 'center','padding-top': '30px',}),
    
    # Some text
    dcc.Markdown(children='''
        Now, that you have an even better idea of what is going in the different Boroughs across different time periods, its time for the last straw of the geogrphic Visualizations.        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),
    

    #labels for drop down menus
    html.Div(children=[
        html.Div([
            html.Label(['Select Borough'], style={'font-weight': 'bold', "text-align": "right"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Year'], style={'font-weight': 'bold', "text-align": "center"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Week'], style={'font-weight': 'bold', "text-align": "center"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Weekday'], style={'font-weight': 'bold',"text-align": "left"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
    ],style={'margin-left': '10%','margin-right': '10%'}),


    #Dropdown menus for point map
    html.Div(children=[
        #Dropdown menu for Borough
        html.Div(
            dcc.Dropdown(
            id='borough_pointmap',
            options=[{
                'label': i,
                'value': i
            } for i in borough_options],
            value='MANHATTAN',  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for year
        html.Div(dcc.Dropdown(
            id='year_pointmap',
            options=[{
                'label': i,
                'value': i
            } for i in year_options],
            value='2019',  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for Week
        html.Div(dcc.Dropdown(
            id='week_pointmap',
            options=[{
                'label': i,
                'value': i
            } for i in week_options],
            value=['1', '2','3', '4'],  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for weekday
        html.Div(dcc.Dropdown(
            id='day_pointmap',
            options=[
                {'label': 'Monday', 'value': '0'},
                {'label': 'Tuesday', 'value': '1'},
                {'label': 'Wednesday', 'value': '2'},
                {'label': 'Thursday', 'value': '3'},
                {'label': 'Friday', 'value': '4'},
                {'label': 'Saturday', 'value': '5'},
                {'label': 'Sunday', 'value': '6'}
            ],
            value=['0', '1', '2', '3', '4', '5','6'],  
            multi=True),
            style={'width': '25%',  'display': 'inline-block'}
        ),
        html.Label(['Type a street name:'], style={'font-weight': 'bold',"text-align": "left", 'padding-right':'10px'}),
        dcc.Input(id="type_input", type="text", placeholder="Type something...", value='', style={'padding-top':'10px'}) #, debounce=True
    ], style={'margin-left': '10%', 
              'margin-right': '10%', 
              'padding-bottom':'20px'}),

    # Pointmap
    html.Div(dcc.Graph(
        id='pointmap-graph',
    ), style={'width': '80%',
              'margin-left': 'auto', 
              'margin-right': 'auto', 
              'padding-bottom':'20px'}),

    # Some text
    dcc.Markdown(children='''
        Along with the above filters, the user will now be able see the exact location of the accident on the map. The marker, when clicked would also provide additional valuable information about the collision.
        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),

    # title for Failure to Yield Intersections
    html.H3('Latitude Longitude Marker', style={'text-align': 'center'}),

    # some text
    dcc.Markdown(children='''
        Driver Inattention/Distraction is ofcourse the number one reason for accidents (Phone calls, food and what not). What is interesting is to look at the second highest reason for accidents i.e. 'Failure to Yield Right-of-Way'As the 'Failure to Yield Right-of-Way' mostly happen at the intersections, it would be interesting to see the top 50 streets with the highest number of such accidents geographically on the map.
        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),


    #labels for drop down menus
    html.Div(children=[
        html.Div([
            html.Label(['Select Borough'], style={'font-weight': 'bold', "text-align": "right"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Year'], style={'font-weight': 'bold', "text-align": "center"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Week'], style={'font-weight': 'bold', "text-align": "center"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
        html.Div([
            html.Label(['Select Weekday'], style={'font-weight': 'bold',"text-align": "left"}),
        ], style={'width': '25%', 'display': 'inline-flex', 'justify-content':'center'}),
    ],style={'margin-left': '10%','margin-right': '10%'}),


    #Dropdown menus for point map with street names
    html.Div(children=[
        #Dropdown menu for street Name
        html.Div(dcc.Dropdown(
            id='street_input',
            options=[{
                'label': i,
                'value': i
            } for i in street_options],
            value='BROADWAY'
            ),
            style={'width': '25%',  'display': 'inline-block'}
        ),
        #Dropdown menu for year
        html.Div(dcc.Dropdown(
            id='year_pointmap1',
            options=[{
                'label': i,
                'value': i
            } for i in year_options],
            value='2019',  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for Week
        html.Div(dcc.Dropdown(
            id='week_pointmap1',
            options=[{
                'label': i,
                'value': i
            } for i in week_options],
            value=['1', '2','3', '4', '5', '6','7', '8','9', '10','11', '12',],  
            multi=True),
            style={'width': '25%', 'display': 'inline-block'}
        ),
        #Dropdown menu for weekday
        html.Div(dcc.Dropdown(
            id='day_pointmap1',
            options=[
                {'label': 'Monday', 'value': '0'},
                {'label': 'Tuesday', 'value': '1'},
                {'label': 'Wednesday', 'value': '2'},
                {'label': 'Thursday', 'value': '3'},
                {'label': 'Friday', 'value': '4'},
                {'label': 'Saturday', 'value': '5'},
                {'label': 'Sunday', 'value': '6'}
            ],
            value=['0', '1', '2', '3', '4', '5','6'],  
            multi=True),
            style={'width': '25%',  'display': 'inline-block'}
        ),        
    ], style={'margin-left': '10%', 
              'margin-right': '10%', 
              'padding-bottom':'20px'}),

    # Pointmap
    html.Div(dcc.Graph(
        id='pointmap-graph1',
    ), style={'width': '80%',
              'margin-left': 'auto', 
              'margin-right': 'auto', 
              'padding-bottom':'20px'}),

    # some text
    dcc.Markdown(children='''
        Investigating this map, you can find out the crossing with the highest number of accidents and measures are needed to fix them
        ''', style={'width': '80%',
                    'margin-left': 'auto',
                    'margin-right': 'auto',
                    'padding-top': '20px',
                    'padding-bottom': '20px'}),
])


## update bar chart when changing Boroughs
@app.callback(
    dash.dependencies.Output('collision-graph1', 'figure'),
    [dash.dependencies.Input('Borough', 'value')])
def update_graph(Borough):
    if Borough == 'All Boroughs':
        trace1 = go.Bar(x=contributing_factors_ALL_top.index, y=contributing_factors_ALL_top['COUNTS'], name='Total Collisions')
        trace2 = go.Bar(x=contributing_factors_ALL_top.index, y=contributing_factors_ALL_top['NUMBER OF PERSONS INJURED'], name='Persons Injured')
        trace3 = go.Bar(x=contributing_factors_ALL_top.index, y=contributing_factors_ALL_top['NUMBER OF PERSONS KILLED'], name='Persons Killed')

    elif Borough == 'BRONX':
        trace1 = go.Bar(x=contributing_factors_BRONX_top.index, y=contributing_factors_BRONX_top['COUNTS'], name='Total Collisions')
        trace2 = go.Bar(x=contributing_factors_BRONX_top.index, y=contributing_factors_BRONX_top['NUMBER OF PERSONS INJURED'], name='Persons Injured')
        trace3 = go.Bar(x=contributing_factors_BRONX_top.index, y=contributing_factors_BRONX_top['NUMBER OF PERSONS KILLED'], name='Persons Killed')

    elif Borough == 'QUEENS':
        trace1 = go.Bar(x=contributing_factors_QUEENS_top.index, y=contributing_factors_QUEENS_top['COUNTS'], name='Total Collisions')
        trace2 = go.Bar(x=contributing_factors_QUEENS_top.index, y=contributing_factors_QUEENS_top['NUMBER OF PERSONS INJURED'], name='Persons Injured')
        trace3 = go.Bar(x=contributing_factors_QUEENS_top.index, y=contributing_factors_QUEENS_top['NUMBER OF PERSONS KILLED'], name='Persons Killed')

    elif Borough == 'BROOKLYN':
        trace1 = go.Bar(x=contributing_factors_BROOKLYN_top.index, y=contributing_factors_BROOKLYN_top['COUNTS'], name='Total Collisions')
        trace2 = go.Bar(x=contributing_factors_BROOKLYN_top.index, y=contributing_factors_BROOKLYN_top['NUMBER OF PERSONS INJURED'], name='Persons Injured')
        trace3 = go.Bar(x=contributing_factors_BROOKLYN_top.index, y=contributing_factors_BROOKLYN_top['NUMBER OF PERSONS KILLED'], name='Persons Killed')

    elif Borough == 'MANHATTAN':
        trace1 = go.Bar(x=contributing_factors_MANHATTAN_top.index, y=contributing_factors_MANHATTAN_top['COUNTS'], name='Total Collisions')
        trace2 = go.Bar(x=contributing_factors_MANHATTAN_top.index, y=contributing_factors_MANHATTAN_top['NUMBER OF PERSONS INJURED'],name='Persons Injured')
        trace3 = go.Bar(x=contributing_factors_MANHATTAN_top.index, y=contributing_factors_MANHATTAN_top['NUMBER OF PERSONS KILLED'], name='Persons Killed')

    elif Borough == 'STATEN ISLAND':
        trace1 = go.Bar(x=contributing_factors_STATENISLAND_top.index, y=contributing_factors_STATENISLAND_top['COUNTS'], name='Total Collisions')
        trace2 = go.Bar(x=contributing_factors_STATENISLAND_top.index, y=contributing_factors_STATENISLAND_top['NUMBER OF PERSONS INJURED'],name='Persons Injured')
        trace3 = go.Bar(x=contributing_factors_STATENISLAND_top.index, y=contributing_factors_STATENISLAND_top['NUMBER OF PERSONS KILLED'], name='Persons Killed')

    return {
        'data': [trace1, trace2, trace3],
        'layout':
        go.Layout(barmode='stack', height=520, xaxis=dict(automargin=True))
    }

@app.callback(
    dash.dependencies.Output('collision-graph2', 'figure'),
    [dash.dependencies.Input('Severity', 'value')])
def update_graph(Severity):
    if Severity == 'Total collisions':
        fig = go.Figure(data=[
            go.Bar(name='BRONX', x=contributing_factors_BRONX_top7['COUNTS'].index, y=contributing_factors_BRONX_top7['COUNTS']),
            go.Bar(name='BROOKLYN', x=contributing_factors_BROOKLYN_top7['COUNTS'].index, y=contributing_factors_BROOKLYN_top7['COUNTS']),
            go.Bar(name='MANHATTAN', x=contributing_factors_MANHATTAN_top7['COUNTS'].index, y=contributing_factors_MANHATTAN_top7['COUNTS']),
            go.Bar(name='QUEENS', x=contributing_factors_QUEENS_top7['COUNTS'].index, y=contributing_factors_QUEENS_top7['COUNTS']),
            go.Bar(name='STATENISLAND', x=contributing_factors_STATENISLAND_top7['COUNTS'].index, y=contributing_factors_STATENISLAND_top7                  ['COUNTS']),
        ])

    elif Severity == 'Injured':
        fig = go.Figure(data=[
            go.Bar(name='BRONX', x=contributing_factors_BRONX_top7['COUNTS'].index, y=contributing_factors_BRONX_top7['NUMBER OF PERSONS INJURED']),
            go.Bar(name='BROOKLYN', x=contributing_factors_BROOKLYN_top7['COUNTS'].index, y=contributing_factors_BROOKLYN_top7['NUMBER OF PERSONS INJURED']),
            go.Bar(name='MANHATTAN', x=contributing_factors_MANHATTAN_top7['COUNTS'].index, y=contributing_factors_MANHATTAN_top7['NUMBER OF PERSONS INJURED']),
            go.Bar(name='QUEENS', x=contributing_factors_QUEENS_top7['COUNTS'].index, y=contributing_factors_QUEENS_top7['NUMBER OF PERSONS INJURED']),
            go.Bar(name='STATENISLAND', x=contributing_factors_STATENISLAND_top7['COUNTS'].index, y=contributing_factors_STATENISLAND_top7  ['NUMBER OF PERSONS INJURED']),
        ])

    elif Severity == 'Killed':
        fig = go.Figure(data=[
            go.Bar(name='BRONX', x=contributing_factors_BRONX_top7['COUNTS'].index, y=contributing_factors_BRONX_top7['NUMBER OF PERSONS KILLED']),
            go.Bar(name='BROOKLYN', x=contributing_factors_BROOKLYN_top7['COUNTS'].index, y=contributing_factors_BROOKLYN_top7['NUMBER OF PERSONS KILLED']),
            go.Bar(name='MANHATTAN', x=contributing_factors_MANHATTAN_top7['COUNTS'].index, y=contributing_factors_MANHATTAN_top7['NUMBER OF PERSONS KILLED']),
            go.Bar(name='QUEENS', x=contributing_factors_QUEENS_top7['COUNTS'].index, y=contributing_factors_QUEENS_top7['NUMBER OF PERSONS KILLED']),
            go.Bar(name='STATENISLAND', x=contributing_factors_STATENISLAND_top7['COUNTS'].index, y=contributing_factors_STATENISLAND_top7    ['NUMBER OF PERSONS KILLED']),
        ])

    fig.update_layout(barmode='group', height=520, xaxis=dict(automargin=True))
    fig.update_traces(hovertemplate="%{y}")

    return fig
    

## update heatmap when using slider
@app.callback(
    [dash.dependencies.Output('heatmap-graph-time', 'figure'),
     dash.dependencies.Output('slider-container', 'style'),
     dash.dependencies.Output('slider-label-container', 'style')],
    [dash.dependencies.Input('crossfilter-hour-slider', 'value'),
     dash.dependencies.Input('allDay_radioButton', 'value'), 
     dash.dependencies.Input('borough_heatmap', 'value'), 
     dash.dependencies.Input('year_heatmap', 'value'), 
     dash.dependencies.Input('week_heatmap', 'value'),
     dash.dependencies.Input('day_heatmap', 'value')])
def update_heatmap(weight, allday, borough, year, week, day):

    # if only one value chosen its just a string so we cast to array
    if type(borough) == str:
        borough = [borough]
    if type(year) == str:
        year= [year]
    if type(week) == str:
        week= [week]
    if type(day) == str:
        day= [day]

    # if allday is chosen use whole data set else only corresponding hour
    if allday == '0':
        currDisplayData = heat_data_all_hours
    else:
        currDisplayData = hour_options[weight]
    
    lat_lon_data=currDisplayData[(currDisplayData['BOROUGH'].isin(borough)) & (currDisplayData['Year'].isin(year)) & (currDisplayData['Week'].isin(week)) & (currDisplayData['WeekDay'].isin(day))]


    # plot all lot, lon data from the current filters    
    if lat_lon_data.shape[0] < 1:
        fig = px.density_mapbox(lat=[0], lon=[0], radius=10,
                        center=dict(lat=40.7812, lon=-73.9665), zoom=10, opacity=0.0,
                        mapbox_style="stamen-toner", height=500)
    else:
        fig = px.density_mapbox(lat_lon_data, lat='LATITUDE', lon='LONGITUDE', radius=5,
                            center=dict(lat=40.7812, lon=-73.9665), zoom=10, opacity=0.5,
                            mapbox_style="stamen-toner", height=500)
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_traces(hovertemplate=None, hoverinfo='skip')
    fig.update_layout(uirevision=True)

    # if allday is chosen show slider and label else hide it
    if allday == '0':
        return fig, {'display': 'none'}, {'display': 'none'}
    else:
        return fig, {'display': 'block'}, {'display': 'block'}

# callback for pointmap
@app.callback(
    dash.dependencies.Output('pointmap-graph', 'figure'),
    [dash.dependencies.Input('borough_pointmap', 'value'), 
     dash.dependencies.Input('year_pointmap', 'value'), 
     dash.dependencies.Input('week_pointmap', 'value'),
     dash.dependencies.Input('day_pointmap', 'value'),
     dash.dependencies.Input('type_input', 'value')])
def update_pointmap(borough, year, week, day, street):
    # if only one value chosen its just a string so we cast to array
    if type(borough) == str:
        borough = [borough]
    if type(year) == str:
        year= [year]
    if type(week) == str:
        week= [week]
    if type(day) == str:
        day= [day]


    # if allday is chosen use whole data set else only corresponding hour

    currDisplayData = heat_data_all_hours

    if street == '':
        lat_lon_data=currDisplayData[(currDisplayData['BOROUGH'].isin(borough)) & (currDisplayData['Year'].isin(year)) & (currDisplayData['Week'].isin(week)) & (currDisplayData['WeekDay'].isin(day))]
    else:
        lat_lon_data=currDisplayData[(currDisplayData['BOROUGH'].isin(borough)) & (currDisplayData['Year'].isin(year)) & (currDisplayData['Week'].isin(week)) & (currDisplayData['WeekDay'].isin(day)) & currDisplayData['ON/CROSS STREET NAME'].str.contains(street.upper())]

    # plot all lot, lon data from the current filters    
    if lat_lon_data.shape[0] < 1:
        fig = px.scatter_mapbox(lat=[0], lon=[0],
                        center=dict(lat=40.7812, lon=-73.9665), zoom=10, opacity=0.0,
                        mapbox_style="open-street-map", height=500)
    else:
        fig = px.scatter_mapbox(lat_lon_data, lat='LATITUDE', lon='LONGITUDE',
                            center=dict(lat=40.7812, lon=-73.9665), zoom=10, opacity=0.8,
                            mapbox_style="open-street-map", height=500)
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update_traces(hovertemplate=None, hoverinfo='skip')
    fig.update_layout(uirevision=True)


    return fig

# callback for pointmap with streets
@app.callback(
    dash.dependencies.Output('pointmap-graph1', 'figure'),
    [dash.dependencies.Input('year_pointmap1', 'value'), 
     dash.dependencies.Input('week_pointmap1', 'value'),
     dash.dependencies.Input('day_pointmap1', 'value'),
     dash.dependencies.Input('street_input', 'value')])
def update_pointmap1(year, week, day, street):
    # if only one value chosen its just a string so we cast to array
    if type(year) == str:
        year= [year]
    if type(week) == str:
        week= [week]
    if type(day) == str:
        day= [day]
    if type(street) == str:
        street= [street]

    # if allday is chosen use whole data set else only corresponding hour

    currDisplayData = street_data_full

    lat_lon_data=currDisplayData[(currDisplayData['Year'].isin(year)) & (currDisplayData['Week'].isin(week)) & (currDisplayData['WeekDay'].isin(day)) & currDisplayData['ON STREET NAME'].isin(street)]

    x_map=lat_lon_data.LATITUDE.mean()
    y_map=lat_lon_data.LONGITUDE.mean()

    # plot all lot, lon data from the current filters    
    if lat_lon_data.shape[0] < 1:
        fig = px.scatter_mapbox(lat=[0], lon=[0],
                        center=dict(lat=40.7812, lon=-73.9665), zoom=10, opacity=0.0,
                        mapbox_style="open-street-map", height=500)
    else:
        fig = px.scatter_mapbox(lat_lon_data, lat='LATITUDE', lon='LONGITUDE',
                            center=dict(lat=x_map, lon=y_map), zoom=10, opacity=0.8,
                            mapbox_style="open-street-map", height=500)
    
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    #fig.update_traces(hovertemplate=None, hoverinfo='skip')
    fig.update_traces(
        text=lat_lon_data[['Accident_Type', 'VEHICLE TYPE CODE 1']],
        customdata=lat_lon_data[['NUMBER_OF_PERSONS_INJURED', 'NUMBER_OF_PERSONS_KILLED']],
        hovertemplate='Accident Type: %{text[0]} <br> Type of Vehicle 1: %{text[1]} <br> Injured:  %{customdata[0]} <br> Injured:  %{customdata[1]}')
    fig.update_layout(uirevision=True)

    #d.apply(lambda row: folium.CircleMarker(location=[row['LATITUDE'], row['LONGITUDE']],popup = 'Accident Type: ' + row.loc['Accident_Type']  + ', Type of Vehicle 1: ' + row.loc['VEHICLE TYPE CODE 1'] + ', Injured = ' + row.loc['NUMBER_OF_PERSONS_INJURED'] + ', Killed = ' + row.loc['NUMBER_OF_PERSONS_KILLED'],radius = 3, fill = True, fill_opacity=1).add_to(map_ny), axis=1)


    return fig

#----------------run server-------------------#
if __name__ == '__main__':
    app.run_server()
