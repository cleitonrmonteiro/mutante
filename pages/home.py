import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/')

card1 = dbc.Card(
    [
        dbc.CardImg(src="assets/wordcloud.png", top=True),
        dbc.CardBody(
            [
                html.H4("TF-IDF", className="card-title"),
                html.P(
                    #"Explore through keywords in an easy and interactive data table.",
                    "Explore through frequent terms in an easy and interactive data table.",
                    className="card-text",
                    style={'textAlign': 'justify'},
                ),
                #dbc.Button(" Run", class_name="bi bi-table", color="primary", href='grid'),
                dbc.Button("Go", color="primary", href='grid'),
            ]
        ),
    ],
    style={"width": "18rem"},
)

card2 = dbc.Card(
    [
        dbc.CardImg(src="assets/sunburstgraph.png", top=True),
        dbc.CardBody(
            [
                html.H4("Sunburst Graph", className="card-title"),
                html.P(
                    "Explore through an interactive graph and publication data.",
                    className="card-text",
                    style={'textAlign': 'justify'},
                ),
                #dbc.Button(" Run", class_name="bi bi-pie-chart", color="primary", href='sunburst'),
                dbc.Button("Go", color="primary", href='sunburst'),
            ]
        ),
    ],
    style={"width": "18rem"},
)

card3 = dbc.Card(
    [
        #dbc.CardImg(src="", top=True),
        dbc.CardBody(
            [
                html.H4("API", className="card-title"),
                html.P(
                    "Connect directly to the MutAnTE dataset.",
                    className="card-text",
                    style={'textAlign': 'justify'},
                ),
                #dbc.Button(" Run", class_name="bi bi-pie-chart", color="primary", href='sunburst'),
                dbc.Button("Go", color="primary", href='mutantsapi'),
            ]
        ),
    ],
    style={"width": "18rem"},
)

layout = \
    html.Div([
        dbc.Container(
            dbc.Row(
                dbc.Col(
                    html.P(
                        [
                            'Mutation Analysis Tools Explorer',
                            html.B(' (MutAnTE) '),
                            'is an easy and interactive web server for querying mutation analysis tools. '
                            'It combines data visualization techniques and an extensive list of tools, providing the end user '
                            'with a simple search platform with publication information for over 200 papers. The web server was developed in Python, '
                            'including some of the most modern libraries on the market for integrating back-end and front-end environments.'
                        ]
                    ),
                ), style={'textAlign': 'justify'}
            ),
            #fluid=True,
        )
    ],
    className="py-3",
    #808080
    #949494
    #a9a9a9
    #bdbebd
    #d3d3d3
    #e9e9e9
    #ffffff / #fff
    style={"background-color": "#e9e9e9"}

    ),\
    dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    card1,
                    width="auto"
                ),
                dbc.Col(
                    card2,
                    width="auto"
                ),
                #dbc.Col(
                #    card3,
                #    width="auto"
                #),

            ],
            justify="center",
            className="gx-5",
            #justify="evenly",
            #className="py-2",
        ),
    ],
    style={"padding-top": "35px"},
    #fluid=True
)

layout1 = html.Div(
    [
        html.P([
            'MutAnTs ',
            html.B('(Mutation Analysis Tools)'),
            #html.Div(
            ' Viewer is an easy and interactive web server for '
            'querying mutation analysis tools. It combines data visualization techniques and an extensive '
            'list of tools to provide the end user with a simple research platform, involving important aspects such as '
            'the publication journal and its relevance.'
        ]),
        html.P(
            html.Div(
            'The web server was developed in Python, using the Pandas library (version 1.4.2) for data manipulation and '
            'Plotly for creating graphical components. Integration of back-end and front-end environments takes place through '
            'Dash (version 2.4.1).')
        ),
        #buttons
    ],
    style={'textAlign': 'justify'},
    #className='col py-3 px-md-5 border bg-light'
    className='col py-3 px-md-5 border'
)