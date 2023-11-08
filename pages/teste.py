"""""
import dash
from dash import html
import requests

dash.register_page(__name__)

link = "http://127.0.0.1:8050/teste"
request = requests.get(link)

layout = html.Div()
"""""