import plotly.express as px, pandas as pd, numpy as np,dash, pickle
from dash import dcc
from dash import html
import json  
#import configparser



# Deployment inforamtion
PORT = 8000

app = dash.Dash(__name__)


# Associating server
server = app.server
# Define title and layout
app.title = 'Global Warming'
#config = configparser.ConfigParser()
#config.read('data/config.ini')

#token =config['mapbox']['token']





country_df = pd.read_csv('data/country_avg.csv')
a_file = open("data/world_ok.pkl", "rb")
geo_dic = pickle.load(a_file)


fig = px.choropleth_mapbox(country_df, geojson= geo_dic, locations= 'Country', color= 'pct_change',
                       color_continuous_scale='balance',animation_frame = 'decade',
                        range_color=(-5, 5),
                        hover_name='Country',
                        hover_data={'pct_change': True, 'Country': True,'avg_per_country':True,'previous_decade':True,'start':True,'change_start':True},
                        mapbox_style='carto-positron',
                        zoom=1,
                        center={'lat': 19, 'lon': 11},
                        opacity=0.6,
                       labels={'pct_change':'Percent Change','avg_per_country':'Average Temp','previous_decade':'Previous Decade','decade':'Decade','start':'Temperature in 1840', 'change_start':'Percent Change from 1840'}
                          )
 
fig.update_layout(
margin={"r":0,"t":0,"l":0,"b":0})
#mapbox_accesstoken=token)


app.layout = html.Div([
    
    # HEADER
    html.Div(
        className="header",
        children=[
        html.H1('Temperature Change From Decade to Decade'),
        ],
    ),
    
    # CONTENT
    html.Section([
        html.Div(
            id='main_fig',
            children = [
                    dcc.Graph(id="choropleth",figure =fig )
                ],
            
            ),
    ]),
])





 


if __name__ == "__main__":
    app.run_server(debug=True, use_reloader=True) 