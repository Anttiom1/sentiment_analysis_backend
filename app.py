from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello</h1>"

@app.route("/sentiment", methods=["POST"])
def get_sentiment():
    input_data = request.json

    #TODO analyysi :D
    # pickle

    print(input_data)
    return {"input_data": input_data}

if __name__ == "main":
    app.run(debug=True)

