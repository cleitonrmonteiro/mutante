import dash_ag_grid as dag
import dash
from dash import Input, Output, State, html, dcc, ctx
import dash_bootstrap_components as dbc
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer # termos frequentes
from sklearn.feature_extraction.text import TfidfVectorizer # TFIDF

from dash_holoniq_wordcloud import DashWordcloud

from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import dash_mantine_components as dmc
#import dash_iconify

dash.register_page(__name__)

df = pd.read_csv("db/mutants_db.csv")
#dados = df[['tool_name', 'article_location', 'article_doi']]

df_name_url = []
for i in df.itertuples():
    # df_name_url.append("[%s](%s)" % (i.tool_name, i.tool_url))
    df_name_url.append('<a href='+i.tool_url+' target="_blank">'+i.tool_name+'</a>')

#c = 0
df_doi = []
df_menu = []
for i in df.itertuples():
    #df_doi.append("[![alt text: test](assets/doi.png)](%s)" % (i.article_doi))
    #df_doi.append("[DOI](%s)" % (i.article_doi))
    #df_doi.append('<a href=' + i.article_doi + ' target="_blank">![alt text: test](assets/doi.png)</a>')
    df_doi.append('<a href=' + i.article_doi + ' target="_blank">Open by DOI</a>')

    #df_menu.append(
    #    [
    #            {"label": "Abstract", "value": c},
    #            {"label": "Go to article", "value": c+1},
    #    ],
    #)
    #c = c + 1
#rain =  "![alt text: rain](https://www.ag-grid.com/example-assets/weather/rain.png)"
#rain = "![alt text: rain](assets/doi.png)"

data_dict = {
    #dados para CSV
    "tool_name_hidden": df["tool_name"],
    "article_title_hidden": df["article_title"],
    "article_abstract_hidden": df["article_abstract"],

    "tool_name": df_name_url,
    "tool_url_hide": df['tool_url'],
    "article_title": df['article_title'],
    "article_location": df['article_location'],
    "article_year": df['article_year'],
    #"article_doi": f"{rain}" +" "+ df['article_doi'],
    "article_doi": df_doi,
    "article_doi_hide": df['article_doi'],
    "article_abstract": df['article_abstract'],
    #"menu": df_menu
}
df = pd.DataFrame(data_dict)
#df["index"] = df.index

columnDefs = [
    #dados para CSV
    {"headerName": "Tool Name", "field": "tool_name_hidden", "hide": True},
    {"headerName": "Article Title", "field": "article_title_hidden", "hide": True},
    {"headerName": "Abstract", "field": "article_abstract_hidden", "hide": True},

    {
        "headerName": "Tool Name",
        "field": "tool_name",
        "filter": True,
        "sortable": True,
        "checkboxSelection": False,
        "headerCheckboxSelection": False,
        "cellRenderer": "markdown",
        "headerTooltip": 'tool_name',
        #"tooltipField": 'tool_name',
        "tooltipComponentParams": {"color": '#D3D3D3'}, #SkyBlue,
        "rowDrag": False,
        "pinned": True,

        # stockLink function is defined in the dashAgGridComponentFunctions.js in assets folder
        #"cellRenderer": "StockLink",
    },
    #{
    #    "headerName": "Article Title",
    #    "field": "article_title",
    #    "filter": True,
    #    "sortable": False,
    #    "'autoH'eight": True,

        # "wrapText" = "True" faz automaticamente a quebra de linha
        #"wrapText": True,

        # Aqui foram usadas "white-space" e "text-align" pois a quebra estava "cortando" as palavras
        # "white-space" está funcionando aqui com os valores "normal" e "pre-line"
    #    "cellStyle": {"line-height": "145%", "white-space": "normal", "text-align": "justify",
    #                  "padding-top": "15px", "padding-bottom": "15px"}
    #},

    #{
        #"headerName": ("Publication Data"),
        #"children": [
            {
                "headerName": "Article Title",
                "field": "article_title",
                "filter": True,
                "sortable": False,
                "autoHeight": True,

                # "wrapText" = "True" faz automaticamente a quebra de linha
                #"wrapText": True,

                # Aqui foram usadas "white-space" e "text-align" pois a quebra estava "cortando" as palavras
                # "white-space" está funcionando aqui com os valores "normal" e "pre-line"
                "cellStyle": {"line-height": "145%", "white-space": "normal", "text-align": "justify",
                              "padding-top": "15px", "padding-bottom": "15px"}
            },
            {
                "headerName": "Journal",
                "field": "article_location",
                "filter": True,
                "sortable": True,
                "width": 125,
                "cellStyle": {"line-height": "145%", "white-space": "normal", #"text-align": "justify",
                              "padding-top": "15px"},
            },
            {
                "headerName": "Year",
                "field": "article_year",
                "filter": True,
                "sortable": True,
                "width": 95
            },
            {
                "headerName": "",
                "field": "article_doi",
                "filter": False,
                "sortable": False,
                "width": 75,
                "cellRenderer": "markdown"
            },
            #{"headerName": "Menu", "field": "menu", "cellRenderer": "rowMenu"},
        #],
   # },

    #{
    #    "headerName": "Publication Journal",
    #    "field": "article_location",
    #    "filter": True,
    #    "sortable": True,
    #    "width": 145,
    #    "cellStyle": {"line-height": "145%", "white-space": "normal", #"text-align": "justify",
    #                  "padding-top": "15px"},
    #},
    #{
    #    "headerName": "Publication Year",
    #    "field": "article_year",
    #    "filter": True,
    #   "sortable": True,
    #    "width": 125
    #},
    #{
    #    "headerName": "DOI",
    #    "field": "article_doi",
    #    "filter": True,
    #    "sortable": False,
    #    "cellRenderer": "markdown"
    #},
    #{"headerName": "", "field": "image", "cellRenderer": "markdown"},
]

getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.node.rowIndex % 2 === 0",
            "style": {"backgroundColor": "#F5F5F5"}, #WhiteSmoke
        },
    ]
}

# Termos mais frequntes (NOVO - excluir o outro se funcionar)
corpus = df["article_abstract"]
vectorizer = CountVectorizer(analyzer='word', stop_words='english', token_pattern='[a-z]*[a-z]')
X = vectorizer.fit_transform(corpus)
data_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
data_df = data_df.sum(axis=0)

freq = []
for x in vectorizer.get_feature_names_out():
    if data_df[x] > 35:
        freq.append([x, data_df[x]])

security_data = freq
# ------------------------------------------------------------------------------

# TFIDF
def calcTFIDF(search_term):
    corpus = df["article_abstract"]

    tr_idf_model  = TfidfVectorizer()
    tf_idf_vector = tr_idf_model.fit_transform(corpus)

    #print(type(tf_idf_vector), tf_idf_vector.shape)
    # <class'scipy.sparse.csr.csr_matrix'>(3,14)

    tf_idf_array = tf_idf_vector.toarray()
    #print(tf_idf_array)

    words_set = tr_idf_model.get_feature_names_out()
    #print(words_set)

    df_tf_idf = pd.DataFrame(tf_idf_array, columns = words_set)
    #df_tf_idf['protein']


    df['tfidf'] = df_tf_idf[search_term]
    new_df = df.query('tfidf>0')
    return new_df.sort_values(by='tfidf', ascending=False)

# ------------------------------------------------------------------------------

# NUVEM
def normalise(lst, vmax=50, vmin=16):
    lmax = max(lst, key=lambda x: x[1])[1]
    lmin = min(lst, key=lambda x: x[1])[1]
    vrange = vmax-vmin
    lrange = lmax-lmin or 1
    for entry in lst:
        entry[1] = int(((entry[1] - lmin) / lrange) * vrange + vmin)
    return lst

cloud = DashWordcloud(
    id='cloud',
    list=normalise(security_data),
    width=750, height=550,
    gridSize=16,
    # weightFactor=1.5,
    # origin=[90, 0],
    # fontFamily='Sans, serif',
    # color='#f0f0c0',
    # backgroundColor='#001f00',
    shuffle=True,
    rotateRatio=0.5,
    shrinkToFit=False,
    shape='circle',
    hover=True
)

def openCloud():
    #return html.Div([
    #    html.Header([
    #        cloud,

    #    ], className="App-header"),
    #], className="App")
    return dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                dbc.Alert(
                    [
                        #html.I(className="bi bi-info-circle me-2"),
                        "The tools will be listed considering the relevance of the word selected in the cloud.",
                    ],
                    color="primary",
                    className="d-flex align-items-center", dismissable=True
                ),
            ),
            className="py-3"
        ),
        dbc.Row(
            dbc.Col(
                cloud,
                width="auto",
            ),
            justify="center",
            #className="gx-5",
        ),
    ],
        #style={"padding": "35px"},
        fluid=True
    )

table = dag.AgGrid(
    id="grid",
    columnDefs=columnDefs,
    rowData=df.to_dict('records'),
    #className="ag-theme-alpine",
    #className="ag-theme-material",
    className="ag-theme-material selection",
    columnSize="sizeToFit",
    getRowStyle=getRowStyle,
    style={"height": 500},
    defaultColDef={"editable": False, "tooltipComponent": "CustomTooltip"},
    dashGridOptions={"tooltipShowDelay": 100, "rowDragManaged": True, "rowSelection": "multiple", "rowMultiSelectWithClick": False,
        "pagination": True,
        #"suppressPaginationPanel": False, "suppressScrollOnNewData": False,
        "loadingOverlayComponent": "CustomLoadingOverlay",
        "loadingOverlayComponentParams": {"loadingMessage": "One moment please...", "color": "red"},
    },
    dangerously_allow_code=True,
    #getRowId="params.data.index",
    #getRowId="params.data.make",
    csvExportParams={"fileName": "mutants.csv",
        "columnKeys": ["tool_name_hidden", "article_title_hidden", "article_abstract_hidden"],
        "skipColumnHeaders": True
    },
)

modal = dbc.Modal(
    [
        #dbc.ModalHeader("More information about selected tool: "),
        dbc.ModalHeader(dbc.ModalTitle("Abstract")),
        dbc.ModalBody(
            id="modal-content",
            style={"text-align": "justify"}
        ),
        dbc.ModalFooter(
            [
                html.Div(id="url"),
                html.Div(id="doi"),
                #html.Div(id="url"),
                dbc.Button("Close", id="close", className="ml-auto")
            ]
        ),

    ],
    id="modal",
    size="lg"
)

modalCloud = dbc.Modal(
    [
        dbc.ModalHeader([
            #html.I(className="bi bi-cloud me-2"),
            dbc.ModalTitle("MutAnTE Word Cloud")]),
        dbc.ModalBody(
            id="modalCloud-content",
            #style={"text-align": "justify"}
        ),
        #dbc.ModalFooter(
        #    [
        #        dbc.Button("Close", id="close-cloud", className="ml-auto")
        #    ]
        #),

    ],
    id="modalCloud",
    #size="xl"
    fullscreen=True,
)

# ------------------------------------------------------------------------------
#corpus = ...
# ------------------------------------------------------------------------------

# Word Cloud -------------------------------------------------------------------
#corpusCloud = open('db/dados_completos.txt')
corpusCloud = open('db/dados_completos.txt', encoding="utf8").read()
#z = file.read()
image_mask = np.array(Image.open('images/img_mut.png'))
wordcloud = WordCloud(background_color = 'white', # cor de fundo
                      width = 1000, # largura
                      height = 500, # altura
                      mask = image_mask, # imagem utilizada
                      contour_width = 2, # espessura do contorno
                      contour_color = 'lightblue', # cor do contorno
                      #contour_color = 'lightgray', # cor do contorno
                      colormap = 'winter') # cor das palavras
wordcloud.generate(corpusCloud)
plt.figure(figsize = (10, 5)) # tamanho do gráfico
plt.imshow(wordcloud, interpolation = 'bilinear') # plotagem da nuvem de palavras
plt.axis('off') # remove as bordas
#z = plt.show() # mostra a word cloud

# ------------------------------------------------------------------------------

# Termos mais frequntes --------------------------------------------------------
corpus = df["article_abstract"]
vectorizer = CountVectorizer(analyzer='word', stop_words='english')
X = vectorizer.fit_transform(corpus)
data_df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
data_df = data_df.sum(axis=0)

freq = {}
for x in vectorizer.get_feature_names_out():
  freq[x] = data_df[x]
freqSort = sorted(freq, key=freq.get, reverse=True)
#freqSort[0:10]

#L = [{"label": "", "value": ""}]
L = []
for x in freqSort[0:10]:
    L.append({"label": x, "value": x})
# ------------------------------------------------------------------------------


layout = dbc.Container(
    [
        #dbc.Row(dbc.Col(html.Div("Tool List", className="h3 p-2 text-white bg-secondary"))),
        #html.Div("Tools List", className="h3 p-2 text-white bg-secondary"),
        dbc.Row(
            dbc.Col(
                dbc.Alert(
                    [
                        #html.I(className="bi bi-info-circle me-2"),
                        "Click on the article title to view the abstract",
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
                    dbc.InputGroup(
                        [
                            dbc.InputGroupText("Show"),
                            dbc.Select(
                                id="select-page-size",
                                value="10",
                                options=[
                                    {"label": "10", "value": "10"},
                                    {"label": "25", "value": "25"},
                                    {"label": "50", "value": "50"},
                                    {"label": "100", "value": "100"},
                                ],
                            ),
                            dbc.InputGroupText("resources per page"),
                        ]
                    ),
                    #dbc.Select(
                    #    id="select-page-size",
                    #    value="10",
                    #    options=[
                    #        {"label": "10 resources per page", "value": "10"},
                    #        {"label": "25 resources per page", "value": "25"},
                    #        {"label": "50 resources per page", "value": "50"},
                    #        {"label": "100 resources per page", "value": "100"},
                    #    ],
                    #),
                    width="auto"
                ),
                dbc.Col(
                    dbc.Button(" Export", id="btn-export", class_name="bi bi-filetype-csv", n_clicks=0),
                    width="auto"
                ),
                #dbc.Col(
                #    dbc.Button(" Word Cloud", id="btn-cloud", class_name="bi bi-cloud"),
                #    width="auto"
                #),
                dbc.Col(
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.Button(" Word Cloud", id="btn-cloud", class_name="bi bi-cloud"),
                                width="auto"
                            ),
                            dbc.Col(
                                #dbc.InputGroup(
                                #    [
                                #
                                #       dbc.InputGroupText("Frequent terms"),
                                #        #    dbc.Input(id="input-search-term", placeholder="Enter the search term", type="text"),
                                #        #    width={"size": 5}
                                #            dbc.Select(
                                #                id="select-search-term",
                                #                #value="",
                                #                options=L
                                #            ),
                                #        dbc.InputGroupText("or"),
                                        dbc.Input(id="input-search-term", placeholder="Select a search term", type="text", disabled="False"),
                                #    ],
                                #),
                                width={"size": 3}
                            ),
                            dbc.Col(
                                #dbc.Button(" Clean", id="btn-search", class_name="bi bi-eraser"),
                                dbc.Button(" Clean", id="btn-search"),
                                width="auto"
                            ),
                        ],
                        justify="end",
                        className="g-0",
                    )
                ),
            ],
            className="py-2",
        ),
        dbc.Row(
            dbc.Col(
                [
                    modalCloud,
                    table,
                    modal,
                ]
            )
        ),
    ],
    #fluid=True
)

layout1 = html.Div(
    [
        #dcc.Markdown(
        #    "Grids can be styled using one of six provided themes from ag-grid."
        #),
        html.Div(
            [
                html.H3("Alpine (default)"),
                dag.AgGrid(
                    id="alpine",
                    columnDefs=columnDefs,
                    #rowData=dados.to_dict('records'),
                    className="ag-theme-alpine",
                    #className="ag-theme-material",
                    columnSize="sizeToFit",
                    getRowStyle=getRowStyle,
                    #dashGridOptions={"rowSelection":"multiple"},
                ),
                #html.Hr(),
            ]
        ),
    ],
)

@dash.callback(
    Output("modal", "is_open"),
    Output("modal-content", "children"),
    Output("url", "children"),
    Output("doi", "children"),
    #Output("url", "children"),
    Input("grid", "cellClicked"),
    Input("grid", "selectedRows"),
    Input("close", "n_clicks"),
)
def open_modal(cell, selection, _):
    if ctx.triggered_id == "close" or (cell is not None and cell["colId"] != "article_title"):
        return False, dash.no_update, dash.no_update, dash.no_update
    if selection:
        return True,\
            ([s["article_abstract"] for s in selection]), \
            ([
                dcc.Link(
                    #"Go to article", href=s["article_doi_hide"],
                    "Open by DOI", href=s["article_doi_hide"],
                    target="blank"
                )
                for s in selection
            ]), \
            ([
                dcc.Link(
                    "Tool web page", href=s["tool_url_hide"],
                    target="blank"
                )
                for s in selection
            ])
    return dash.no_update, dash.no_update, dash.no_update, dash.no_update

@dash.callback(
    Output("modalCloud", "is_open", allow_duplicate=True),
    Output("modalCloud-content", "children"),
    Input("btn-cloud", "n_clicks"),
    #Input("close-cloud", "n_clicks"),
    prevent_initial_call=True
)
def open_modalCloud( _):
    if ctx.triggered_id == "btn-cloud":
        return True, openCloud()
    #elif ctx.triggered_id == "close-cloud":
    #    return False, dash.no_update
    return dash.no_update, dash.no_update
#--

@dash.callback(
    Output("grid", "rowData"),
    Input("input-search-term", "value"),
    #Input("btn-search", "n_clicks"),
    #State("grid", "rowData")
)
def update_table(value):
    if value is not None:
        return calcTFIDF(value).to_dict("records")
    return df.to_dict("records")

@dash.callback(
    Output("input-search-term", "value", allow_duplicate=True),
    Input("btn-search", "n_clicks"),
    prevent_initial_call=True
)
def clean_search( _):
    if ctx.triggered_id == "input-search-term":
        return None

#---

@dash.callback(
    Output("grid", "dashGridOptions"),
    Input("select-page-size", "value"),
    State("grid", "dashGridOptions"),
)
def update_page_size(page_size, grid_options):
    page_size = 1 if page_size is None else page_size
    grid_options["paginationPageSize"] = page_size
    return grid_options

@dash.callback(
    Output("grid", "exportDataAsCsv"),
    Input("btn-export", "n_clicks"),
)
def export_data_as_csv(n_clicks):
    if n_clicks:
        return True
    return None

@dash.callback(
    Output(component_id='input-search-term', component_property='value'),
    Output("modalCloud", "is_open"),
    Input(component_id='cloud', component_property='click')
)
def update_output_div(item):
    if item is None:
        return None, True
    else:
        return item[0], False
