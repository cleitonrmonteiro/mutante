import dash
from dash import html, dcc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag

dash.register_page(__name__)

layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H5("Getting started with MutAnTE"))),
        dbc.Row(
            dbc.Col(
                html.P([
                    'MutAnTE is an easy and interactive web server for searching mutation analysis tools. '
                    'It combines data visualization techniques and an extensive list of tools, providing the end user '
                    'with a simple search platform with publication information for over 200 papers.'
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.P([
                    'Three features are available in this version: search for frequent terms, search for '
                    'sunburst graph and an API for connecting directly to data.'
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.H3("Exploring data through frequent terms (TF-IDF)"))),
        dbc.Row(
            dbc.Col(
                html.P([
                    'The search page for frequent terms can be accessed from the home page or via the top menu ',
                    html.B('Explore > TF-IDF'), '.'
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.Center(html.Img(src="assets/help_fig_grid.png", width='75%')))),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Resources per page ', html.B('(1)'), ' - '
                        'allows you to define the number of lines that will be displayed per page in the grid.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Export button ', html.B('(2)'), ' - '
                        'allows you to export the listed dataset in CSV format.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Word Cloud button ', html.B('(3)'), ' - '
                        'allows you to select a search term from a word cloud with the most frequent terms present in '
                        'all abstracts. The selected term is displayed in ', html.B('(4) '), 'and can be discarded '
                        'when necessary with the Clean button ', html.B('(5)'), '.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        "You can open the tool's web page by clicking on the link with its name (Tool Name column) ",
                        html.B('(6)'), '.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Open by DOI ', html.B('(7)'), ' - '
                        'allows you to access the full paper by clicking on the Open by DOI link.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Pagination ', html.B('(8)'), ' - '
                        'allows you to navigate the grid pages according to the number of lines defined for display.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),

        dbc.Row(dbc.Col(html.Center(html.Img(src="assets/help_fig_grid_filter.png", width='75%')))),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Filters ', html.B('(9)'), ' - '
                        'allows you to filter data by different criteria. This feature can be applied to all available '
                        'data columns - Tool Name, Article Title, Journal and Year.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.Center(html.Img(src="assets/help_fig_grid_selection.png", width='75%')))),
        dbc.Row(dbc.Col(html.Center(html.Img(src="assets/help_fig_grid_abstract.png", width='75%')))),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'For each work listed in the data table, it is possible to see its abstract by clicking on the '
                        'article title ', html.B('(10)'), '. It is also possible to access the full paper through '
                        'the DOI ', html.B('(11) '), "and the tool's web page ", html.B('(12)'), '.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.Center(html.Img(src="assets/help_fig_cloud.png", width='75%')))),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'MutAnTE Word Cloud: generates a word cloud with the most frequent terms from all abstracts, '
                        'allowing you to select the desired word as a search term ', html.B('(13)'), '. In this case, '
                        'the works will be listed considering the relevance of the selected word (TF-IDF).'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.H3("Exploring data through a sunburst graph"))),
        dbc.Row(
            dbc.Col(
                html.P([
                    'The sunburst graph can be accessed from the home page or via the top menu ',
                    html.B('Explore > Sunburst Graph'), '.'
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.Center(html.Img(src="assets/help_fig_sunburst.png", width='75%')))),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Allows you to explore the tools through a sunburst-type graph, where the selection can be '
                        'made by publication period of the works ', html.B('(14) '), 'and by the Brazilian journal '
                        'evaluation system ', html.B('(15)'), '. The graph can be resized as '
                        'desired ', html.B('(16)'), '.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'You can also filter the data by selecting specific layers in the graph ', html.B('(17)'),
                        '. The abstract can be seen by clicking on the desired tool ', html.B('(18)'), '.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.H3("MutAnTE API"))),
        dbc.Row(
            dbc.Col(
                html.P([
                    'Our API can be accessed via the top menu ',
                    html.B('Explore > MutAnTE API'), '.'
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
        dbc.Row(dbc.Col(html.Center(html.Img(src="assets/help_fig_api.png", width='75%')))),
        dbc.Row(
            dbc.Col(
                html.P([
                    html.Li([
                        'Connect directly to the data provided by MutAnTE using different programming languages, like '
                        'our Python example ', html.B('(19)'), '. To use specific data columns, use the attributes '
                        'listed in table ', html.B('(20)'), '.'
                    ])
                ]),
                style={'textAlign': 'justify'}
            ),
        ),
    ],
    style={"padding-top": "35px"},
)
