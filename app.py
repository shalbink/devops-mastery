
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
    <head><title>DevOps Mastery</title></head>
    <body>
        <h1>Welcome to DevOps Mastery CI/CD!</h1>
    </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="UP")


@app.route("/about")
def about():
    return jsonify(
        application="DevOps Mastery",
        message="A simple Flask application"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

