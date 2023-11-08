import dash
from dash import Dash, html

import pandas as pd
from flask import jsonify


import dash_bootstrap_components as dbc

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = Dash(__name__,  external_stylesheets=external_stylesheets, use_pages=True)

#app = Dash(__name__,  external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.BOOTSTRAP], use_pages=True)
#app = Dash(__name__,  external_stylesheets=[dbc.themes.SPACELAB, dbc.icons.BOOTSTRAP], use_pages=True)
#app = Dash(__name__,  external_stylesheets=[dbc.themes.YETI, dbc.icons.BOOTSTRAP], use_pages=True)
#app = Dash(__name__,  external_stylesheets=[dbc.themes.ZEPHYR, dbc.icons.BOOTSTRAP], use_pages=True)

#app = Dash(__name__,  external_stylesheets=[dbc.themes.CERULEAN, dbc.icons.BOOTSTRAP], use_pages=True)
app = Dash(__name__,  external_stylesheets=[dbc.themes.COSMO, dbc.icons.BOOTSTRAP], use_pages=True,
           suppress_callback_exceptions=True)

server = app.server

# MutAnTE API ==========================================================================================================
# Returns the dataset as a list of dictionaries, where each dictionary contains data from a specific tool.
@server.route("/api")
def api():
    df = pd.read_csv("db/mutants_db.csv")
    df = df[['tool_name', 'tool_url', 'article_title', 'article_location', 'article_year', 'article_doi']]
    response = df.to_dict('records')
    return jsonify(response)
# ======================================================================================================================

    #resp = {"tool": "Vermont"}
    #return jsonify(resp)

#app = Dash(__name__,  use_pages=True)
#app = Dash(__name__, suppress_callback_exceptions=True)

#inserindo a navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(" Home", class_name="bi bi-house", href="/")),
        dbc.NavItem(
            dbc.DropdownMenu(
                label="Explore",
                children=[
                    dbc.DropdownMenuItem("TF-IDF", href='grid'),
                    dbc.DropdownMenuItem("Sunburst Graph", href='sunburst'),
                    dbc.DropdownMenuItem(divider=True),
                    dbc.DropdownMenuItem("MutAnTE API", href='mutantsapi'),
                ],
                nav=True,
                #in_navbar=True
            ),
        ),
        dbc.NavItem(dbc.NavLink("Help", href="")),
        dbc.NavItem(dbc.NavLink("About", href="")),
    ],
    #brand="MutAnTE",
    brand=html.Img(src="assets/mutante-logo-lato.png", height="25px"),
    brand_href="/",
    #color="primary",
    dark=True, class_name="bg-dark"
)

app.layout = html.Div([
	#html.H1('Multi-page app with Dash Pages'),
    navbar,
    #html.Div(
    #    [
    #        html.Div(
    #            dcc.Link(
    #                #f"{page['name']} - {page['path']}", href=page["relative_path"]
    #                f"{page['name']}", href=page["relative_path"]
    #            )
    #        )
    #        for page in dash.page_registry.values()
    #    ]
    #),
	dash.page_container
])

if __name__ == '__main__':
	app.run_server(debug=True)
    #app.run()