import json
from flask import Flask
from flask import request
from data_manager import DataManager

app = Flask(__name__)
dm = DataManager()

@app.route('/api/accounts')
def get_account(methods = ['GET', 'POST', 'DELETE']):
    if request.method == 'GET':
        account_id = request.args["account_id"]
        account = dm.get_account_by_id(account_id)
        return json.dumps(account)
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        pass

@app.route('/api/accounts/health')
def get_health(methods = ['GET']):
    return json.dumps({"health": "UP"})


if __name__ == "__main__":
    app.run(debug=True)