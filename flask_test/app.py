from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def root():
    return "Hello World"

if __name__ == "__main__":
    app.run(port=4000, debug=True)
