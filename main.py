#!/usr/bin/env python3

from flask import Flask, render_template
from brou_api import scraper_brou
from brou_api import scraper_bs


app = Flask(__name__, static_folder="static")
app.static_url_path = "/static"


@app.route("/")
def index():
    title = 'Mi Web Retro'
    return render_template("index.html", title=title)


@app.get("/brou/v1")
def api_brou():
    try:
        datos = scraper_brou.query()
        return datos
    except Exception as e:
        return 'No funciona el scraper, error: {}'.format(e)

@app.get("/brou/v2")
def api_brou_2():
    try:
        datos = scraper_bs.query()
        return datos
    except Exception as e:
        return 'No funciona el scraper, error: {}'.format(e)

if __name__ == "__main__":
    app.run(debug=False)