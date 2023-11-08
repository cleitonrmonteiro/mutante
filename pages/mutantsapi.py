import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

dash.register_page(__name__)

columnDefs = [
    {"field": "attribute"},
    {"field": "description"},
]

data = [
    {"attribute": "tool_name", "description": "Tool name"},
    {"attribute": "tool_url", "description": "URL to access the tool"},
    {"attribute": "article_title", "description": "Title of published work referring to the tool"},
    {"attribute": "article_location", "description": "Place of publication of the work"},
    {"attribute": "article_year", "description": "Year of publication of the work"},
    {"attribute": "article_doi", "description": "DOI for access to the published article"},
]

layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H2("API Reference"))),
        dbc.Row(
            dbc.Col(
                html.P([
                    'Connect directly to the dataset provided by MutAnTE through a simple and easy API.',
                    #'Connect directly to the dataset provided by MutAnTs Explorer through a simple and easy Application Programming Interface (API).',
                    html.Br(),
                    ' Use the ', html.B('MutAnTE API'),
                    ' to load a list of dictionaries, where each dictionary represents a tool, providing different attributes for data access.',

                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        html.Div(
            [
                dbc.Row(dbc.Col(html.H5("Here's a sample Python client code to easily connect"))),
                dbc.Row(
                    dbc.Col(
                        [
                        html.Code("import requests"),
                        html.Br(),
                        html.Code("url = 'http://mutante.onrender.com/api'"),
                        html.Br(),
                        html.Code("response = requests.get(url)"),
                        html.Br(),
                        html.Code("print(response.json())"),
                        ]
                    )
                )
            ],
            style={"padding-top": "15px"}
        ),
        html.Div(
            [
                dbc.Row(dbc.Col(html.H5("Use available attributes to get specific data"))),
                dbc.Row(
                    dbc.Col(
                        dag.AgGrid(
                            columnDefs=columnDefs,
                            rowData=data,
                            columnSize="sizeToFit",
                            defaultColDef={"resizable": False, "sortable": False, "filter": False},
                            dashGridOptions={"domLayout": "autoHeight"},
                            #style={"padding-top": "25px"}
                         ),
                    )
                ),
            ],
            style={"padding-top": "25px"}
        )
    ],
    style={"padding-top": "35px"},
    #fluid=True
)
