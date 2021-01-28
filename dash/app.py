# DASH TUTORIAL


# 1. IMPORT LIBARIES
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

import plotly.io as pio



pio.templates.default="ggplot2"

colors = {
    'text': '#7FDBFF'
}

# 2. LOAD THE DATA

df = ??

fig = ??

map_ = ??




#3. INITIALISE THE APP
app= dash.Dash()



# 4. DEFINE THE APP (STYLING)
app.layout = html.Div(children=[
        html.H1(children='Our first Dash app',
         style={
             'textAlign': 'center',
             'color': colors['text']

         }
    ),


    html.Div(children='''
    Dash Spiced Tutorial
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    dcc.Graph(
        id='example-graph2',
        figure =map_
    )
])


 # 5. RUN THE APP
if __name__ == '__main__':
    app.run_server(debug=True, port=5001)
