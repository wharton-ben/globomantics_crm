#!/usr/bin/env python

class Database:
    '''
    Represents the interface to the data (model). Uses only statically-
    defined data to keep things simple.
    '''

    def __init__(self):
        #constructor
        self.data = {
            "ACCT100": {"paid": 60, "due": 100}, # balance = 40
            "ACCT200": {"paid": 70, "due": 60}, # balance = -10
            "ACCT300": {"paid": 0, "due": 0}, # balance = 0
        }

    def balance(self, acct_id):
        '''
        determines the customer balance by finding the difference between
        what has been paid and what is still owed on the account. The 'model'
        can provide methods to help interface with the data; it is not limited 
        to only storing data. A positive number means the customer owes us money
        and a negative number means they overpaid and have a credit with us. 
        '''

        acct = self.data.get(acct_id)
        if acct:
            return int(acct["due"]) - int(acct["paid"])
        return None

