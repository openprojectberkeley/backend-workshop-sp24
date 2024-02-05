from flask import Flask, request, jsonify
import db

app = Flask(__name__)

@app.route("/get-balance", methods=["POST"])
def get_balance():
    pass

@app.route("/deposit", methods=["POST"])
def deposit():
    pass

@app.route("/transfer", methods=["POST"])
def transfer():
    pass

@app.route("/create", methods=["POST"])
def create_user():
    pass

if __name__ == "__main__":
    app.run(debug=True)
