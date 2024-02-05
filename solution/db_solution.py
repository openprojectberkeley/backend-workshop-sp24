from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = "mongodb+srv://joeljaison13:test@cluster0.8e783c2.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(uri, server_api=ServerApi('1'))
db = client.users
collection = db.users
# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


def create_account(name):
    """
    Creates an account under the name passed in.
    Balance is set to 0.
    """
    user = {
        "name": name,
        "balance": 0
    }
    user_id = collection.insert_one(user).inserted_id
    print(f"Created user with ID {user_id}")


def transfer_amount(sender_name, receiver_name, amount):
    """
    Transfers the specified amount from account under name1 to name2
    """
    # get the info of the sender and receiver
    sender = collection.find_one({"name": sender_name})
    receiver = collection.find_one({"name": receiver_name})

    if sender and receiver:
        # Check if sender has sufficient balance
        if sender["balance"] >= amount:
            # Deduct amount from sender's balance
            sender_new_balance = sender["balance"] - amount
            collection.update_one({"_id": sender["_id"]}, {"$set": {"balance": sender_new_balance}})
            
            # Add amount to receiver's balance
            receiver_new_balance = receiver["balance"] + amount
            collection.update_one({"_id": receiver["_id"]}, {"$set": {"balance": receiver_new_balance}})
            
            print(f"Transfer successful. {amount} transferred from {sender_name} to {receiver_name}.")
        else:
            print(f"{sender_name} does not have sufficient balance for the transfer.")
    else:
        print("One or both users not found.")

def get_balance(name):
    """
    Returns the balance associated the with the name passed in.
    """
    user = collection.find_one({"name": name})

    if user:
        return user["balance"]
    else:
        return None


def deposit_funds(name, amount):
    """
    Deposits the specified amount to an account
    """
    user = collection.find_one({"name": name})

    if user:
        # Update the balance for the user
        new_balance = user["balance"] + amount
        collection.update_one({"_id": user["_id"]}, {"$set": {"balance": new_balance}})
        print(f"Deposited {amount} to {name}. New balance: {new_balance}")
    else:
        print(f"User {name} not found.")
