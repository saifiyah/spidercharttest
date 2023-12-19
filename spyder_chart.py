# -*- coding: utf-8 -*-
"""Spyder Chart

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dZOw5eUsTetXM2hiy2UacrEguZjC4k2e
"""

pip install plotly

pip install dash

import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html

# Materials and their properties
materials = ['Aluminum 6061', 'PEEK', 'Material_1', 'Material_2', 'Material_3']

properties = {
    'Strength': [100, 80, 90, 70, 85],
    'Weight': [90, 70, 80, 95, 75],
    'Cost': [70, 60, 80, 85, 65],
    'Temperature Resistance': [80, 90, 85, 75, 95],
    'Corrosion Resistance': [85, 75, 90, 80, 88]
}

# Line and fill colors for each material
line_colors = ['blue', 'green', 'red', 'purple', 'orange']
fill_colors = ['rgba(0, 0, 255, 0.2)', 'rgba(0, 255, 0, 0.2)', 'rgba(255, 0, 0, 0.2)',
               'rgba(128, 0, 128, 0.2)', 'rgba(255, 165, 0, 0.2)']

# Initialize Dash app
app = dash.Dash(__name__)

# Layout of the app
app.layout = html.Div([
    html.H1("Interactive Spider Chart", style={'font-family': 'Arial'}),

    html.P("Select properties from the dropdown below to compare between materials. Click the legend to select which materials are compared.", style={'font-family': 'Arial', 'font-size': '18px'}),

    dcc.Dropdown(
        id='property-dropdown',
        options=[
            {'label': prop, 'value': prop} for prop in properties.keys()
        ],
        value=['Strength'],  # Initial selection
        multi=True,
        style={'font-family': 'Arial'}
    ),

    dcc.Graph(
        id='spider-chart'
    )
])


# Callback to update the spider chart based on dropdown selection
@app.callback(
    dash.dependencies.Output('spider-chart', 'figure'),
    [dash.dependencies.Input('property-dropdown', 'value')]
)
def update_spider_chart(selected_properties):
    fig = go.Figure()

    for i, material in enumerate(materials):
        fig.add_trace(go.Scatterpolar(
            r=[properties[prop][i] for prop in selected_properties],
            theta=selected_properties,
            fill='toself',
            line=dict(color=line_colors[i]),
            fillcolor=fill_colors[i],
            name=material
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]  # Adjust the range based on the sum of your properties
            )
        ),
        showlegend=True
    )

    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)