# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px
from src.Algorithms import rabbit_problem
from src.Algorithms.rabbit_problem import Warren
import src.Algorithms.thomson_problem as thomson
from src.Dash.FirstApp import sampling

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

# df = pd.DataFrame({
#     "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#     "Amount": [4, 1, 2, 2, 4, 5],
#     "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
# })

warren = Warren(100)
df = sampling.create_sample_to_dataframe(method=rabbit_problem.rabbit_search, args=[warren], trials=1000)
points = thomson.random_points_on_sphere(120, 1)

for i in range(0):
    print("STEPPED")
    thomson.thomson_force_step(points)

th_df = pd.DataFrame(data=points)
energy = thomson.thomson_energy(points)

# for i in range(20):
#     thomson.thomson_force_step(points)
#
# th_df2 = pd.DataFrame(data=points)
# energy2 = thomson.thomson_energy(points)

for i in range(200):
    thomson.thomson_force_step(points)

th_df3 = pd.DataFrame(data=points)
energy3 = thomson.thomson_energy(points)

fig = px.histogram(data_frame=df, x="Result")

sphere = px.scatter_3d(data_frame=th_df, x=0, y=1, z=2)
# sphere2 = px.scatter_3d(data_frame=th_df2, x=0, y=1, z=2)
sphere3 = px.scatter_3d(data_frame=th_df3, x=0, y=1, z=2)

app.layout = html.Div(children=[
    html.H1(children='Number of guesses required to solve the rabbit problem'),

    html.Div(children='''
        Histogram showing distribution of number of guesses
    '''),

    dcc.Graph(
        id='rabbit-problem',
        figure=fig
    ),

    html.H1(children='Thomson Energies and Configurations'),
    html.Div(children=("Energy = %f" % energy)),
    dcc.Graph(
        id='thomson-plot',
        figure=sphere
    ),

    # html.Div(children=("Energy = %f" % energy2)),
    # dcc.Graph(
    #     id='thomson-plot2',
    #     figure=sphere2
    # ),

    html.Div(children=("Energy = %f" % energy3)),
    dcc.Graph(
        id='thomson-plot3',
        figure=sphere3
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)