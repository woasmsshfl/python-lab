from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/post")
def hello_world():
    dic = {"id": 1, "username" : "ssar"}
    return dic

if __name__ == "__name__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )