from flask import Flask, request, jsonify
import db_solution

app = Flask(__name__)

@app.route("/get-balance", methods=["GET"])
def get_balance():
    name = request.args.get("name")
    balance = db_solution.get_balance(name)
    if balance is not None:
        return jsonify({ "balance": balance }), 200
    else:
        return "User not found", 404

@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()
    user_name = data.get("name")
    amount = data.get("amount")
    if user_name and amount is not None:
        deposit(user_name, amount)
        return "Deposit successful", 200
    else:
        return "Invalid request", 400


@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.get_json()
    sender_name = data.get("sender")
    receiver_name = data.get("receiver")
    amount = data.get("amount")
    if sender_name and receiver_name and amount is not None:
        db_solution.transfer_amount(sender_name, receiver_name, amount)
        return "Transfer successful", 200
    else:
        return "Invalid request", 400

@app.route("/create", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    if name:
        db_solution.create_user(name)
        return "User successfully created", 200
    else:
        return "Invalid name", 400

if __name__ == "__main__":
    app.run(debug=True)