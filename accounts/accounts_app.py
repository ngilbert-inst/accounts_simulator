import sys
from flask import Flask, request, redirect, render_template
from functions.sqlquery import sql_query

app = Flask(__name__)

@app.route('/accounts')
def sql_database():
    results = sql_query(''' SELECT * FROM data_table''')
    msg = 'SELECT * FROM data_table'
