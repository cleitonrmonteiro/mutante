#import base64
#import json
#from numpy import NaN, empty
#import plotly.graph_objs as go
import pandas as pd
import dash
from dash.dependencies import Input, Output, State
from dash import dcc, html, ctx
import plotly.express as px
import dash_bootstrap_components as dbc

dash.register_page(__name__)

# modal Sunburst
mdSb = dbc.Modal(
    [
        dbc.ModalHeader(dbc.ModalTitle("Abstract")),
        dbc.ModalBody(
            id="mdSb-content",
            style={"text-align": "justify"}
        ),
        dbc.ModalFooter(
            [
                html.Div(id="mdSb-doi"),
                html.Div(id="mdSb-url"),
                dbc.Button("Close", id="mdSb-close", className="ml-auto")
            ]
        ),

    ],
    id="mdSb",
    size="lg"
)

def main_layout() -> html.Div:
    #return container
    return html.Div(style={'border-style': 'none', 'margin': 'auto'},
        children=[
            dbc.Container(
                [
                    dbc.Row(
                        dbc.Col(
                            dbc.Alert(
                                [
                                    "Apply filters to select works by publication period and by the Brazilian journal evaluation system (Qualis/CAPES).",
                                ],
                                color="primary",
                                className="d-flex align-items-center", dismissable=True
                            ),
                        ),
                        className="py-3"
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    html.H6("Publication period", style={'font-weight': 'bold'}),
                                    dcc.RangeSlider(dash.ano_min, dash.ano_max,
                                                    marks={i: f'{i}' for i in range(dash.ano_min, dash.ano_max, 1 if (
                                                        dash.ano_max - dash.ano_min) < dash.LIMIT_SCALE else (
                                                        dash.ano_max - dash.ano_min) // dash.LIMIT_SCALE)},
                                                    value=[dash.ano_min, dash.ano_max], id='year_slider'),
                                ]
                            ),
                            dbc.Col(
                                [
                                    html.H6("Brazilian Qualis", style={'font-weight': 'bold'}),
                                    dcc.Dropdown(dash.qualis, dash.qualis, multi=True, id='qualis_filter'),
                                ]
                            ),
                        ],
                        className="py-2",
                    ),
                    dbc.Row(
                        dbc.Col(
                            [
                                #html.H6("Gráfico:", style={'font-weight': 'bold'}),
                                dcc.Graph(figure=dash.fig, id='graph-interact'),
                                mdSb,
                            ],
                            width={"size": '100%', "offset": 3},
                        ),
                        justify="center",
                    ),
                ],
                # fluid=True
            )
        ])

def update_graph(df):
    dash.fig = px.sunburst(
        df,
        path=['brazilian_qualis_cc', 'article_location', 'article_year', 'tool_name'],
        maxdepth=4, width=900, height=900)
    dash.fig.update_layout(clickmode='event+select')


def update_qualis_filter(df):
    #print('update qualis filter')
    qualis = []
    for i in df['brazilian_qualis_cc']:
        if i not in qualis:
            #print("teste")
            qualis.append(i)
    dash.qualis = sorted(qualis)

def read_csv(filename):
    #print("csv reader")
    try:
        df = pd.read_csv(filename)
    except Exception as e:
        #print(e)
        return html.Div([
            'There was an error processing the database file.'
        ])
    dash.df = df
    update_graph(df)
    update_qualis_filter(df)

dash.LIMIT_SCALE = 10
dash.qualis = []
dash.fig = None
dash.ano_min = 2000
dash.ano_max = 2022

@dash.callback(
    Output("mdSb", "is_open"),
    Output("mdSb-content", "children"),
    Output("mdSb-doi", "children"),
    Output("mdSb-url", "children"),
    Input('graph-interact', 'clickData'),
    Input("mdSb-close", "n_clicks"),
    #prevent_initial_call=True
)
def filter_graphic(clickData, _):
    if ctx.triggered_id == "mdSb-close" or clickData is None:
        return False, dash.no_update, dash.no_update, dash.no_update
    tool = clickData['points'][0]['label']
    a = dash.df.loc[dash.df['tool_name'] == tool]

    if len(a) > 0:
        return True, a['article_abstract'].item(), \
        dcc.Link(
            "Open by DOI", href=a["article_doi"].item(),
            target="blank"
        ), \
        dcc.Link(
            "Tool web page", href=a["tool_url"].item(),
            target="blank"
        ),
    return False, dash.no_update, dash.no_update, dash.no_update

@dash.callback(
    Output('graph-interact', 'figure'),
    Input('qualis_filter', 'value'),
    Input('year_slider', 'value'))
def filter_graphic(qualis_value, year_slider_value):
    #print('filter_graphic')
    df = dash.df
    df = df.loc[(df['article_year'] >= (year_slider_value[0])) &
                (df['article_year'] <= (year_slider_value[1]))]
    df = df.loc[df['brazilian_qualis_cc'].isin(qualis_value)]
    if df is not None:
        fig = px.sunburst(
            df,
            path=['brazilian_qualis_cc', 'article_location', 'article_year', 'tool_name'],
            maxdepth=4, width=900, height=900)
        dash.fig = fig
    return dash.fig

read_csv("db/mutants_db.csv")
layout = main_layout()
