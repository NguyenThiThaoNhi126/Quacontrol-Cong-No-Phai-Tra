from flask import Flask
import dash

server = Flask(__name__)

app_NO_PT = dash.Dash(
        __name__,
        # server=server,
        url_base_pathname='/',
        suppress_callback_exceptions=True
    )


