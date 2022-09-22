# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
from src.Algorithms import rabbit_problem
from src.Algorithms.rabbit_problem import Warren
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
df = sampling.create_sample_to_dataframe(method=rabbit_problem.rabbit_search, args=[warren], trials=10000)

# fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig = px.histogram(data_frame=df, x="Result")
app.layout = html.Div(children=[
    html.H1(children='Number of guesses required to solve the rabbit problem'),

    html.Div(children='''
        Histogram showing distribution of number of guesses
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)