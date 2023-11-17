from dash import Dash, Input, Output, State, html, dcc, ctx
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        #dbc.NavItem(dbc.NavLink(" Home", class_name="bi bi-house", href="/")),
        dbc.NavItem(dbc.NavLink(" Home", href="/")),
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
        dbc.NavItem(dbc.NavLink("Help", href="help")),
        dbc.NavItem(dbc.NavLink("Team", id="open-offcanvas-placement", n_clicks=0, style={"cursor": "pointer"})),
    ],
    #brand="MutAnTE",
    brand=html.Img(src="assets/mutante-logo-lato.png", height="25px"),
    brand_href="/",
    #color="primary",
    dark=True, class_name="bg-dark"
)