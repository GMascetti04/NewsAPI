import json
from flask_cors import CORS
from flask import Flask, jsonify, request, render_template, Response
import sys

sys.path.append("../src")
import news

# retrieve News API key from key.text
with open('key.txt', 'r') as file:
    key = file.read().rstrip()


# create instance of NewsSource class with api key
source = news.NewsSource(key)

app = Flask(__name__)
CORS(app)

articles = {}
sources = source.getNewsSources(lang="en", country="us")

@app.route("/search/top_headline_count", methods = ['POST'])
def fetch_top_headlines():
    if request.method == 'POST':
        count = int(request.form['count'])
        global articles
        articles = source.getNumberOfArticles(count)
        return render_template('results.html')

@app.route("/search/title", methods = ['POST'])
def search_by_title():
    if request.method == 'POST':
        title = request.form['title']
        global articles
        articles = source.searchByTitle(str(title))
        return render_template('results.html')

@app.route("/search/keywords", methods = ['POST'])
def search_by_keywords():
    if request.method == 'POST':
        keywords = request.form['keywords']
        global articles
        articles = source.searchByKeyWords(keywords)
        return render_template('results.html')


@app.route("/search/source", methods = ['POST'])
def search_by_source():
    if request.method == 'POST':
        source_choice = request.form['source']
        global articles
        articles = source.getArticlesFromSource(source_choice)
        return render_template('results.html')

@app.route("/search", methods = ['GET'])
def search():
    if request.method == 'GET':
        print('get')
        return render_template('client.html')


@app.route("/results", methods=['GET'])
def access_results():
    if request.method == 'GET':
        return Response(json.dumps(articles),  mimetype='application/json')
    

@app.route("/sources", methods=['GET'])
def access_sources():
    if request.method == 'GET':
        return Response(json.dumps(sources),  mimetype='application/json')