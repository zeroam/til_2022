from flask import Flask, jsonify

from db import fetch_blogs, fetch_blog

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/blogs")
def all_blogs():
    return jsonify(fetch_blogs())


@app.route("/blogs/<id>")
def get_blog(id):
    return jsonify(fetch_blog(id))


if __name__ == "__main__":
    app.run()