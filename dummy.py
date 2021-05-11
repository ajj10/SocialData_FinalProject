import pandas as pd
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from jupyter_dash import JupyterDash
import plotly.express as px
import folium
import folium.plugins as plugins

import warnings
warnings.filterwarnings('ignore')

collisions_df_original1 = pd.read_csv("Motor_Vehicle_Collisions_-_Crashes.csv", sep=',', error_bad_lines=False, index_col=False, dtype='unicode')

contributing_factors1 = collisions_df_original1[['CONTRIBUTING FACTOR VEHICLE 1', 'BOROUGH', 'NUMBER OF PERSONS INJURED', 'NUMBER OF PERSONS KILLED']]

# combining and Simplifing contributing factors (from 61 -> 26)
contributing_factors1['CONTRIBUTING FACTOR VEHICLE 1'].replace({'Texting': 'Cell Phone Usage', 'Cell Phone (hand-Held)': 'Cell Phone Usage', 'Cell Phone (hand-held)': 'Cell Phone Usage', 'Cell Phone (hands-free)': 'Cell Phone Usage', '80': 'Unspecified', '1': 'Unspecified', 'Outside Car Distraction': 'Driver Inattention/Distraction', 'Passenger Distraction': 'Driver Inattention/Distraction', 'Drugs (Illegal)': 'Drugs/Prescription Medication', 'Drugs (illegal)': 'Drugs/Prescription Medication', 'Prescription Medication': 'Drugs/Prescription Medication', 'Fatigued/Drowsy': 'Fatigued/Drowsy/Lost Consciousness/Fell Asleep', 'Fell Asleep': 'Fatigued/Drowsy/Lost Consciousness/Fell Asleep', 'Lost Consciousness': 'Fatigued/Drowsy/Lost Consciousness/Fell Asleep', 'Illnes': 'Illness/Physical Disability', 'Illness': 'Illness/Physical Disability', 'Physical Disability': 'Illness/Physical Disability', 'Glare': 'View Obstructed/Limited', 'Obstruction/Debris': 'View Obstructed/Limited', 'Windshield Inadequate': 'View Obstructed/Limited', 'Tinted Windows': 'View Obstructed/Limited', 'Lane Marking Improper/Inadequate': 'Lane Marking/Pavement Defective/Inadequate', 'Pavement Defective': 'Lane Marking/Pavement Defective/Inadequate', 'Shoulders Defective/Improper': 'Lane Marking/Pavement Defective/Inadequate', 'Reaction to Other Uninvolved Vehicle': 'Other Vehicular', 'Reaction to Uninvolved Vehicle': 'Other Vehicular', 'Passing or Lane Usage Improper': 'Passing or Lane Usage/Changing Improper/Unsafe', 'Passing Too Closely': 'Passing or Lane Usage/Changing Improper/Unsafe', 'Unsafe Lane Changing': 'Passing or Lane Usage/Changing Improper/Unsafe', 'Failure to Keep Right': 'Passing or Lane Usage/Changing Improper/Unsafe', 'Listening/Using Headphones': 'Using Headphones/other Electronic Device', 'Using On Board Navigation Device': 'Using Headphones/other Electronic Device', 'Other Electronic Device': 'Using Headphones/other Electronic Device', 'Headlights Defective': 'Vehicle Inadequate/Defective', 'Vehicle Vandalism': 'Vehicle Inadequate/Defective', 'Other Lighting Defects': 'Vehicle Inadequate/Defective', 'Tow Hitch Defective': 'Vehicle Inadequate/Defective', 'Steering Failure': 'Vehicle Inadequate/Defective', 'Brakes Defective': 'Vehicle Inadequate/Defective', 'Tire Failure/Inadequate': 'Vehicle Inadequate/Defective', 'Accelerator Defective': 'Vehicle Inadequate/Defective', 'Driver Inexperience': 'Driver Inexperience/Oversized Vehicle', 'Oversized Vehicle': 'Driver Inexperience/Oversized Vehicle', 'Traffic Control Disregarded': 'Traffic Control/Speed Limits Disregarded', 'Unsafe Speed': 'Traffic Control/Speed Limits Disregarded'}, inplace=True)

contributing_factors1['COUNTS'] = 1.0

# Drop all NaN Boroughs since they dont give the insight wwe need
contributing_factors1 = contributing_factors1[contributing_factors1['BOROUGH'].notna()]
contributing_factors_combined1 = contributing_factors1.astype({"NUMBER OF PERSONS INJURED": float, "NUMBER OF PERSONS KILLED": float})

contributing_factors_combined1 = contributing_factors_combined1.groupby(['CONTRIBUTING FACTOR VEHICLE 1','BOROUGH']).agg({'NUMBER OF PERSONS INJURED': 'sum', 'NUMBER OF PERSONS KILLED': 'sum', 'COUNTS': 'sum'})

contributing_factors_BRONX = contributing_factors_combined1.iloc[contributing_factors_combined1.index.get_level_values('BOROUGH') == 'BRONX']
contributing_factors_BRONX = contributing_factors_BRONX.droplevel(1)
contributing_factors_QUEENS = contributing_factors_combined1.iloc[contributing_factors_combined1.index.get_level_values('BOROUGH') == 'QUEENS']
contributing_factors_QUEENS = contributing_factors_QUEENS.droplevel(1)
contributing_factors_BROOKLYN = contributing_factors_combined1.iloc[contributing_factors_combined1.index.get_level_values('BOROUGH') == 'BROOKLYN']
contributing_factors_BROOKLYN = contributing_factors_BROOKLYN.droplevel(1)
contributing_factors_MANHATTAN = contributing_factors_combined1.iloc[contributing_factors_combined1.index.get_level_values('BOROUGH') == 'MANHATTAN']
contributing_factors_MANHATTAN = contributing_factors_MANHATTAN.droplevel(1)
contributing_factors_STATENISLAND = contributing_factors_combined1.iloc[contributing_factors_combined1.index.get_level_values('BOROUGH') == 'STATEN ISLAND']
contributing_factors_STATENISLAND = contributing_factors_STATENISLAND.droplevel(1)

# Deleting unspecified since they give no insight 
contributing_factors_BRONX = contributing_factors_BRONX.drop("Unspecified", axis=0)
contributing_factors_QUEENS = contributing_factors_QUEENS.drop("Unspecified", axis=0)
contributing_factors_BROOKLYN = contributing_factors_BROOKLYN.drop("Unspecified", axis=0)
contributing_factors_MANHATTAN = contributing_factors_MANHATTAN.drop("Unspecified", axis=0)
contributing_factors_STATENISLAND = contributing_factors_STATENISLAND.drop("Unspecified", axis=0)

contributing_factors_ALL = contributing_factors_BRONX
contributing_factors_ALL = contributing_factors_ALL.add(contributing_factors_QUEENS, fill_value=0)
contributing_factors_ALL = contributing_factors_ALL.add(contributing_factors_BROOKLYN, fill_value=0)
contributing_factors_ALL = contributing_factors_ALL.add(contributing_factors_MANHATTAN, fill_value=0)
contributing_factors_ALL = contributing_factors_ALL.add(contributing_factors_STATENISLAND, fill_value=0)

contributing_factors_ALL_top = contributing_factors_ALL.drop(contributing_factors_ALL[contributing_factors_ALL.COUNTS < 2000].index)
contributing_factors_BRONX_top = contributing_factors_BRONX.drop(contributing_factors_BRONX[contributing_factors_BRONX.COUNTS < 800].index)
contributing_factors_BROOKLYN_top = contributing_factors_BROOKLYN.drop(contributing_factors_BROOKLYN[contributing_factors_BROOKLYN.COUNTS < 1000].index)
contributing_factors_MANHATTAN_top = contributing_factors_MANHATTAN.drop(contributing_factors_MANHATTAN[contributing_factors_MANHATTAN.COUNTS < 1000].index)
contributing_factors_QUEENS_top = contributing_factors_QUEENS.drop(contributing_factors_QUEENS[contributing_factors_QUEENS.COUNTS < 600].index)
contributing_factors_STATENISLAND_top = contributing_factors_STATENISLAND.drop(contributing_factors_STATENISLAND[contributing_factors_STATENISLAND.COUNTS < 100].index)
contributing_factors_STATENISLAND_top = contributing_factors_STATENISLAND_top.drop(contributing_factors_STATENISLAND_top[contributing_factors_STATENISLAND_top.COUNTS == 197].index)

collisions_df_original = collisions_df_original1

#Removing Na from relevant columns
collisions_df_original = collisions_df_original[collisions_df_original['BOROUGH'].notna()]
collisions_df_original = collisions_df_original[collisions_df_original['LATITUDE'].notna()]
collisions_df_original = collisions_df_original[collisions_df_original['LONGITUDE'].notna()]

#Data Type conversions
collisions_df_original['LATITUDE']=collisions_df_original['LATITUDE'].astype('float').round(3)
collisions_df_original['LONGITUDE']=collisions_df_original['LONGITUDE'].astype('float').round(3)
 
collisions_df_original['NUMBER OF PERSONS INJURED']=collisions_df_original['NUMBER OF PERSONS INJURED'].fillna(0)
collisions_df_original['NUMBER OF PERSONS INJURED']=collisions_df_original['NUMBER OF PERSONS INJURED'].astype('int')

collisions_df_original['NUMBER OF PERSONS KILLED']=collisions_df_original['NUMBER OF PERSONS KILLED'].fillna(0)
collisions_df_original['NUMBER OF PERSONS KILLED']=collisions_df_original['NUMBER OF PERSONS KILLED'].astype('int')

collisions_df_original['NUMBER OF PEDESTRIANS INJURED']=collisions_df_original['NUMBER OF PEDESTRIANS INJURED'].fillna(0)
collisions_df_original['NUMBER OF PEDESTRIANS INJURED']=collisions_df_original['NUMBER OF PEDESTRIANS INJURED'].astype('int')

collisions_df_original['NUMBER OF PEDESTRIANS KILLED']=collisions_df_original['NUMBER OF PEDESTRIANS KILLED'].fillna(0)
collisions_df_original['NUMBER OF PEDESTRIANS KILLED']=collisions_df_original['NUMBER OF PEDESTRIANS KILLED'].astype('int')

collisions_df_original['NUMBER OF CYCLIST INJURED']=collisions_df_original['NUMBER OF CYCLIST INJURED'].fillna(0)
collisions_df_original['NUMBER OF CYCLIST INJURED']=collisions_df_original['NUMBER OF CYCLIST INJURED'].astype('int')

collisions_df_original['NUMBER OF CYCLIST KILLED']=collisions_df_original['NUMBER OF CYCLIST KILLED'].fillna(0)
collisions_df_original['NUMBER OF CYCLIST KILLED']=collisions_df_original['NUMBER OF CYCLIST KILLED'].astype('int')

collisions_df_original['NUMBER OF MOTORIST INJURED']=collisions_df_original['NUMBER OF MOTORIST INJURED'].fillna(0)
collisions_df_original['NUMBER OF MOTORIST INJURED']=collisions_df_original['NUMBER OF MOTORIST INJURED'].astype('int')

collisions_df_original['NUMBER OF MOTORIST KILLED']=collisions_df_original['NUMBER OF MOTORIST KILLED'].fillna(0)
collisions_df_original['NUMBER OF MOTORIST KILLED']=collisions_df_original['NUMBER OF MOTORIST KILLED'].astype('int')



#Deleting incorrect columns
collisions_df_original = collisions_df_original[collisions_df_original['LONGITUDE']!=0.0]
collisions_df_original = collisions_df_original[collisions_df_original['LATITUDE']!=0.0]

collisions_df_original = collisions_df_original.rename(columns={"NUMBER OF PERSONS KILLED": "NUMBER_OF_PERSONS_KILLED", "NUMBER OF PERSONS INJURED": "NUMBER_OF_PERSONS_INJURED",
                                                                "NUMBER OF PEDESTRIANS INJURED":"NUMBER_OF_PEDESTRIANS_INJURED",
                                                                "NUMBER OF PEDESTRIANS KILLED":"NUMBER_OF_PEDESTRIANS_KILLED",
                                                                "NUMBER OF CYCLIST INJURED":"NUMBER_OF_CYCLIST_INJURED",
                                                                "NUMBER OF CYCLIST KILLED":"NUMBER_OF_CYCLIST_KILLED","NUMBER OF MOTORIST INJURED":"NUMBER_OF_MOTORIST_INJURED",
                                                                "NUMBER OF MOTORIST KILLED":"NUMBER_OF_MOTORIST_KILLED"})

collisions_df_original["Accident_count"] = 1

#Filtering Data for a particular Year
collisions_df_original['CRASH DATE'] = pd.to_datetime(collisions_df_original['CRASH DATE'])
collisions_df_original['CRASH TIME'] = pd.to_datetime(collisions_df_original['CRASH TIME'])
collisions_df_original['Year'] = collisions_df_original['CRASH DATE'].dt.year
collisions_df_original['Month'] = collisions_df_original['CRASH DATE'].dt.month
collisions_df_original['Hr'] = collisions_df_original['CRASH TIME'].dt.hour

#Filtering on Time Period for Limited Data
collisions_df = collisions_df_original[(collisions_df_original['Year']==2019)]
#collisions_df = collisions_df_original[(collisions_df_original['Year']==2020) &(collisions_df_original['Month']==4)]


# Selecting only relevant columns
#collisions_df = collisions_df[["LATITUDE","LONGITUDE","Accident_count","NUMBER_OF_PERSONS_INJURED","NUMBER_OF_PERSONS_KILLED","NUMBER_OF_PEDESTRIANS_INJURED","NUMBER_OF_PEDESTRIANS_KILLED","NUMBER_OF_CYCLIST_INJURED","NUMBER_OF_CYCLIST_KILLED","NUMBER_OF_MOTORIST_INJURED","NUMBER_OF_MOTORIST_KILLED"]]

# Create weight column, using date
collisions_df['Weight'] = collisions_df['Hr']
collisions_df['Weight'] = collisions_df['Weight'].astype(float)
data_3 = collisions_df.dropna(axis=0, subset=['LONGITUDE','LATITUDE','Weight'])
data_3 = data_3[['LONGITUDE', 'LATITUDE','Weight']]

# Dash graph
options = contributing_factors1['BOROUGH'].unique()
brh_options = np.append(options, ['All Boroughs'], axis=0)
Borough = 'All Boroughs'

app = JupyterDash(__name__)

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
    

app.run_server(mode='external', port=2000)
#app.run_server(mode='inline')
#if __name__ == '__main__':
#    app.run_server(debug=True)