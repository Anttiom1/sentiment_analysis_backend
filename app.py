from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello</h1>"

@app.route("/sentiment", methods=["POST"])
def get_sentiment():
    input_data = request.json

    #pickle

    print(input_data)
    return {"input_data": input_data}

if __name__ == "main":
    app.run(host="0.0.0.0", port="8080", debug=False)