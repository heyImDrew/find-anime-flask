import flask
import requests
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/search', methods=["GET", "POST"])
def search():
    if request.method == "POST":
        search_name = request.form['name']
        api_response = requests.get(f"https://api.jikan.moe/v3/search/anime?q={search_name}").json()
        results = api_response.get('results', [])
        return flask.render_template('search.html', search_name=search_name, results=results)
    return flask.render_template('search.html', search_name="", results=[])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=7007)
