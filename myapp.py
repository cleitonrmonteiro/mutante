import dash
import dash_bootstrap_components as dbc
import pandas as pd

from dash import Dash, html
from flask import jsonify
from pages import header, team

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


app.layout = html.Div(
    [
        header.navbar,
        team.canvas,
        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
