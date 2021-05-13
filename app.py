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


## options
hour_options = [heatmap_data_0,heatmap_data_1,heatmap_data_2,heatmap_data_3,heatmap_data_4,heatmap_data_5,heatmap_data_6,heatmap_data_7,heatmap_data_8,heatmap_data_9,heatmap_data_10,heatmap_data_11,heatmap_data_12,heatmap_data_13,heatmap_data_14,heatmap_data_15,heatmap_data_16,heatmap_data_17,heatmap_data_18,heatmap_data_19,heatmap_data_20,heatmap_data_21,heatmap_data_22,heatmap_data_23]
brh_options = ['BROOKLYN', 'MANHATTAN', 'BRONX', 'STATEN ISLAND', 'QUEENS', 'All Boroughs']
severity_options = ['Total collisions', 'Injured', 'Killed']
borough_options = ['BROOKLYN', 'BRONX', 'STATEN ISLAND', 'QUEENS', 'MANHATTAN']
year_options = ['2013','2014','2015','2016','2017','2018','2019','2020','2021']
week_options = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53']
hour_marks = np.arange(0,24)


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


#------------------Dash app-----------------#
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    # header of page
    html.H1('Vehicle Collisions in New York City', style={'text-align': 'center'}),
    
    # some text (introduction)
    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac. Mauris nec velit diam. Vivamus nec vestibulum augue. Aliquam et feugiat dui. Integer id dui venenatis, tristique ipsum vel, dapibus turpis.
        ''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),

    # title for contributing factors bar chart
    html.H2('Collisions and their contributing factors', style={'text-align': 'center'}),

    # some text
    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac.
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
    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac. Mauris nec velit diam. Vivamus nec vestibulum augue. Aliquam et feugiat dui. Integer id dui venenatis, tristique ipsum vel, dapibus turpis.
        Donec quis imperdiet tellus, nec semper turpis. Praesent a hendrerit mauris, et malesuada justo. Ut bibendum lacinia luctus. Ut accumsan ex eu enim sagittis, nec sollicitudin mauris porttitor. Sed maximus neque id magna cursus, et varius purus sagittis. Fusce dolor ligula, pretium posuere urna eu, ullamcorper semper elit. Morbi elementum sagittis tortor, ut blandit ante rhoncus at. Ut porttitor eu dui nec iaculis. Maecenas ut sem a sapien maximus semper. Suspendisse massa urna, cursus vitae euismod non, dapibus id eros. Duis quis nisl ac sem condimentum tincidunt et vitae odio. Nam ut gravida eros. Donec molestie, justo et auctor fermentum, ipsum erat mattis velit, id tempor ipsum libero non ligula.
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
    
    # some text
    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac.
        ''', style={'width': '80%',
                    'margin-left': 'auto', 
                    'margin-right': 'auto', 
                    'padding-top': '20px', 
                    'padding-bottom': '20px'}),

    # title for heatmap
    html.H2('Heat Map that shows collisions by time of day', style={'text-align': 'center'}),
    
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
            value='52',  
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
    

    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac. Mauris nec velit diam. Vivamus nec vestibulum augue. Aliquam et feugiat dui. Integer id dui venenatis, tristique ipsum vel, dapibus turpis.
        Donec quis imperdiet tellus, nec semper turpis. Praesent a hendrerit mauris, et malesuada justo. Ut bibendum lacinia luctus. Ut accumsan ex eu enim sagittis, nec sollicitudin mauris porttitor. Sed maximus neque id magna cursus, et varius purus sagittis. Fusce dolor ligula, pretium posuere urna eu, ullamcorper semper elit. Morbi elementum sagittis tortor, ut blandit ante rhoncus at. Ut porttitor eu dui nec iaculis. Maecenas ut sem a sapien maximus semper. Suspendisse massa urna, cursus vitae euismod non, dapibus id eros. Duis quis nisl ac sem condimentum tincidunt et vitae odio. Nam ut gravida eros. Donec molestie, justo et auctor fermentum, ipsum erat mattis velit, id tempor ipsum libero non ligula.
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
    


#----------------run server-------------------#
if __name__ == '__main__':
    app.run_server()
