from flask import Flask
from flask import request
from data_manager import DataManager

app = Flask(__name__)
dm = DataManager()

@app.route('/api/accounts')
def get_account(methods = ['GET', 'POST', 'DELETE']):
    if request.method == 'GET':
        pass
    elif request.method == 'POST':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        pass

if __name__ == "__main__":
    app.run(debug=True)