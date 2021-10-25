#!/usr/bin/env python
from flask import Flask, render_template, request
from database import Database

#create Flask object and instantiate database object
app = Flask(__name__)
db = Database()

@app.route("/", methods=["GET", "POST"])
def index():
    '''
    This is a view function which responds to requests for the top-level URL.
    It serves as the "controller" in MVC as it accesses both the model and 
    the view. 
    '''

    #button click within the view kicks off a POST request 
    if request.method == "POST":
        #This collects the user input from the view. The controller's job
        #is to process this information, which includes using methods from 
        #the "model" to get the information we need (in this case, the account
        #balance).
        acct_id = request.form["acctid"]
        acct_balance = db.balance(acct_id.upper())
        app.logger.debug(f"balance for {acct_id}: {acct_balance}")
    
    else:
        acct_balance = "N/A"

    return render_template("index.html", acct_balance=acct_balance)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)