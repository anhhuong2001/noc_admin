from flask import Flask, jsonify, request
app = Flask (__name__)

@app.route("/")
def hello():
    return "my name is Anh Huong"
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)