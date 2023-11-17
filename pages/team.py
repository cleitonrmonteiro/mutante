import dash
from dash import Input, Output, State, html
import dash_bootstrap_components as dbc

canvas = dbc.Offcanvas(
        dbc.Container(
            dbc.Row([
                dbc.Col(
                    html.P([
                        html.H4("Cleiton Monteiro"),
                        html.B("PhD student"),
                        html.H6("Universidade Federal de Viçosa"),
                    ]),
                    width="auto"
                ),
                dbc.Col(
                    html.P([
                        html.H4("Jerônimo Penha"),
                        html.B("PhD student"),
                        html.H6("Universidade Federal de Viçosa"),
                    ]),
                    width="auto"
                ),
                dbc.Col(
                    html.P([
                        html.H4("Sabrina Silveira"),
                        html.B("Assistant Professor"),
                        html.H6("Universidade Federal de Viçosa"),
                    ]),
                    width="auto"
                ),

            ], justify="evenly"),
        ),

        id="offcanvas-placement",
        title="Team",
        is_open=False,
        placement="bottom"
    )


@dash.callback(
    Output("offcanvas-placement", "is_open"),
    Input("open-offcanvas-placement", "n_clicks"),
    [State("offcanvas-placement", "is_open")],
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open
