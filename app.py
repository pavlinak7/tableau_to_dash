import dash
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

app = Dash(
        __name__,
        external_stylesheets=[dbc.themes.BOOTSTRAP],
        use_pages=True
    )

app.layout = html.Div(
                      [
                        dcc.Location(
                            id='url',
                            refresh=False
                        ),
                        dash.page_container
                      ]
                      )


if __name__ == '__main__':
    app.run_server(debug=True)
