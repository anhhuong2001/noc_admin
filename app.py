from flask import Flask, jsonify, request
app = Flask (__name__)

@app.route("/")
def hello():
    return "my name is Anh Huong"

account_list = [
    {"id": 1, "username" : "huong", "password": 1234},
    {"id": 2 , "username" : "thuy", "password" : 5678}
]

@app.route("/get_account_list")
def get_account_list():
    return jsonify(account_list)
    
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080)

