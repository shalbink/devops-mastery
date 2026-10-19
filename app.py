
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>DevOps Mastery</title>
        </head>
        <body>
            <h1>Welcome to DevOps Mastery - Develop Branch!</h1>
            <p>Created by Shalbin K Eldo</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="UP")


@app.route("/about")
def about():
    return {
        "application": "DevOps Mastery",
        "author": "Shalbin K Eldo"
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

