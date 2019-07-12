from flask import Flask
from flask import request
from flask import abort
from flask import jsonify
from flask import make_response
from data_manager import DataManager

app = Flask(__name__)
dm = DataManager()
dm.connect()

@app.route('/api/accounts')
def get_account(methods = ['GET', 'POST', 'DELETE']):
    if request.method == 'GET':
        account_id = request.args.get("account_id", default = None, type = int)
        user_id = request.args.get("user_id", default = None, type = int)
        role_id = request.args.get("role_id", default = None, type = int)
        team_id = request.args.get("team_id", default = None, type = int)
        if account_id is not None:
            result = dm.get_account_by_id(account_id)
        elif user_id is not None:
            result = dm.get_account_by_user_id(user_id)
        elif role_id is not None:
            result = dm.get_accounts_by_role_id(role_id)
        elif team_id is not None:
            result = dm.get_accounts_by_team_id(team_id)

        response = make_response(jsonify({"users": result}))
        response.mimetype = 'application/json'
        return response
    else:
        abort(400)

@app.route('/api/accounts/health')
def get_health(methods = ['GET']):
    return json.dumps({"health": "UP"})


if __name__ == "__main__":
    app.run(debug=True)