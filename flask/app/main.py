from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Tom look at me i made a webpage locally with flask on docker haha!"

if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
