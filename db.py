from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


uri = ... # enter your mongodb uri here
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


def create_account(name):
    """
    Creates an account under the name passed in.
    Balance is set to 0.
    """
    pass


def transfer_amoount(name1, name2, amount):
    """
    Transfers the specified amount from account under name1 to name2
    """
    pass

def get_balance(name):
    """
    Returns the balance associated the with the name passed in.
    """
    pass


def deposit_funds(name, amount):
    """
    Deposits the specified amount to an account
    """
    pass
