import dash
import plotly.graph_objs as go
import numpy as np
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime as dt
app=dash.Dash()
 
app.layout = html.Div([
    html.Label('Choose a city'),
    dcc.Dropdown(
        id= 'first-dropdown',
        options=[
            {'label': 'San Francisco', 'value': 'SF'},
            {'label': 'Ney York', 'value': 'NY'},
            {'label': 'Raligh Durham', 'value': 'RDH', 'disabled': True}
        ]
    ),
    html.Label('This is a slider'),
    dcc.Slider(
        min= 1,
        max= 10,
        value= 5,
        step= .5,
        marks= {i: i for i in range(10)}
    ),
    html.Label('This is a range slider'),
    dcc.RangeSlider(
        min= 1,
        max= 10,
        step= .5,
        value= [3, 7],
        marks= {i: i for i in range(10)}
    ),
    html.Br(),
    html.Br(),
    
    html.Div([
        html.Label('This is input box'),
        dcc.Input(
            placeholder= 'Input your name',
            type= 'text',
            value= ''
        )
    ]),
    html.Br(),
    html.Button('Submit', id= 'submit_form'),
    html.Br(),
    html.Br(),
    dcc.Textarea(
        placeholder= 'Input your feedback',
        value= 'placeholder for text',
        style= {'width': '100%'}
    ),
    html.Br(),
    html.Br(),
    dcc.Checklist(
        options= [
            {'label': 'San Francisco', 'value': 'SF'},
            {'label': 'Ney York', 'value': 'NY'},
            {'label': 'Raligh Durham', 'value': 'RDH'}
        ],
        value=['SF']
    ),
     html.Br(),
    html.Br(),
    dcc.RadioItems(
        options= [
            {'label': 'San Francisco', 'value': 'SF'},
            {'label': 'Ney York', 'value': 'NY'},
            {'label': 'Raligh Durham', 'value': 'RDH'}
        ],
        value=['SF']
    ),
    html.Br(),
    html.Br(),
    dcc.DatePickerSingle(
        id= 'db_pick_single',
        date= dt(2015, 5, 10)
    ),
    html.Br(),
    html.Br(),
    dcc.DatePickerRange(
        id= 'db_pick_range',
        start_date= dt(2015, 5, 10),
        end_date_placeholder_text= 'Select the end date'
    ),
    html.Br(),
    html.Br(),
    dcc.Markdown('''

# This is an <h1> tag

## This is an <h2> tag

###### This is an <h6> tag
''')  

    
])

if __name__ == '__main__':
    app.run_server(port=4001)