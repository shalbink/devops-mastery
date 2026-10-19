
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head><title>DevOps Mastery</title></head>
        <body>
            <h1>Welcome to My DevOps Application!</h1>
            <p>Created by Shalbin K Eldo</p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="UP")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

