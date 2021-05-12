import pandas as pd
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px

import warnings
warnings.filterwarnings('ignore')

contributing_factors_ALL_top = pd.read_json('contributing_factors_ALL_top.json')
contributing_factors_BRONX_top = pd.read_json('contributing_factors_BRONX_top.json')
contributing_factors_BROOKLYN_top = pd.read_json('contributing_factors_BROOKLYN_top.json')
contributing_factors_MANHATTAN_top = pd.read_json('contributing_factors_MANHATTAN_top.json')
contributing_factors_QUEENS_top = pd.read_json('contributing_factors_QUEENS_top.json')
contributing_factors_STATENISLAND_top = pd.read_json('contributing_factors_STATENISLAND_top.json')

data_3 = pd.read_json('data_3.json')

# Dash graph

brh_options = ['BROOKLYN', 'MANHATTAN', 'BRONX', 'STATEN ISLAND', 'QUEENS', 'All Boroughs']

app = dash.Dash(__name__)
server = app.server

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options


app.layout = html.Div([
    html.H1('Vehicle Collisions in New York City', style={'text-align': 'center'}),
    
    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac. Mauris nec velit diam. Vivamus nec vestibulum augue. Aliquam et feugiat dui. Integer id dui venenatis, tristique ipsum vel, dapibus turpis.
    ''', style={'width': '80%',
                'margin-left': 'auto', 
                'margin-right': 'auto', 
                'padding-top': '20px', 
                'padding-bottom': '20px'}),

    html.H2('Collisions and their contributing factors', style={'text-align': 'center'}),

    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac.
    ''', style={'width': '80%','margin-left': 'auto', 'margin-right': 'auto', 'padding-top': '20px', 'padding-bottom': '20px'}),

    html.Div(
        [
            dcc.Dropdown(
                id='Borough',
                options=[{
                    'label': i,
                    'value': i
                } for i in brh_options],
                value='All Boroughs'),
        ],
        style={'width': '25%',
               'margin-left': '10%'}),

    dcc.Graph(id='collision-graph1',
              style={'width': '80%',
                     'margin-left': 'auto', 
                     'margin-right': 'auto',
                     'position': 'relative'}),
    
    html.Div(children='''
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec in vehicula ex, ut hendrerit erat. Nulla facilisi. Etiam maximus, elit et interdum ultrices, dui orci facilisis mauris, sed auctor lorem metus eu risus. Vestibulum accumsan sagittis odio, id sodales turpis tincidunt ac. Maecenas erat erat, suscipit eu erat eu, blandit egestas dolor. Nulla euismod sapien vitae eleifend auctor. Nunc aliquet mollis tortor, in placerat eros vulputate ac. Mauris nec velit diam. Vivamus nec vestibulum augue. Aliquam et feugiat dui. Integer id dui venenatis, tristique ipsum vel, dapibus turpis.

Donec quis imperdiet tellus, nec semper turpis. Praesent a hendrerit mauris, et malesuada justo. Ut bibendum lacinia luctus. Ut accumsan ex eu enim sagittis, nec sollicitudin mauris porttitor. Sed maximus neque id magna cursus, et varius purus sagittis. Fusce dolor ligula, pretium posuere urna eu, ullamcorper semper elit. Morbi elementum sagittis tortor, ut blandit ante rhoncus at. Ut porttitor eu dui nec iaculis. Maecenas ut sem a sapien maximus semper. Suspendisse massa urna, cursus vitae euismod non, dapibus id eros. Duis quis nisl ac sem condimentum tincidunt et vitae odio. Nam ut gravida eros. Donec molestie, justo et auctor fermentum, ipsum erat mattis velit, id tempor ipsum libero non ligula.
    ''', style={'width': '80%',
                'margin-left': 'auto', 
                'margin-right': 'auto', 
                'padding-top': '20px', 
                'padding-bottom': '20px'}),

    html.H2('Heat Map that shows collisions by time of day', style={'text-align': 'center'}),
    
    html.Div(dcc.Graph(
        id='heatmap-graph-time',
        #figure=fig
    ), style={'width': '80%',
              'margin-left': 'auto', 
              'margin-right': 'auto', 
              'padding-bottom':'20px'}),


    html.Div(dcc.Slider(
        id='crossfilter-hour-slider',
        min=data_3['Weight'].min(),
        max=data_3['Weight'].max(),
        value=data_3['Weight'].min(),
        marks={str(weight): str(weight) for weight in data_3['Weight'].unique()},
        step=None
    ), style={'width': '70%',
              'margin-left': 'auto', 
              'margin-right': 'auto'})
])


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
    dash.dependencies.Output('heatmap-graph-time', 'figure'),
    [dash.dependencies.Input('crossfilter-hour-slider', 'value')])
def update_heatmap(weight):
    lats_lons_hour = data_3.loc[data_3['Weight'] == weight]

    fig = px.density_mapbox(lats_lons_hour, lat='LATITUDE', lon='LONGITUDE', radius=5,
                        center=dict(lat=40.7812, lon=-73.9665), zoom=10, opacity=0.5,
                        mapbox_style="stamen-toner", height=500)
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.update(layout_coloraxis_showscale=False)
    fig.update_traces(hovertemplate=None, hoverinfo='skip')
    fig.update_layout(uirevision=True)

    return fig
    

#app.run_server(mode='external', port=2000)
#app.run_server(mode='inline')
if __name__ == '__main__':
    app.run_server()
