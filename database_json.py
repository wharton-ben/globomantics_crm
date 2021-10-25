#!/usr/bin/env python

class Database:
    '''
    Represents the interface to the data (model). Uses only statically-
    defined data to keep things simple.
    '''

    def __init__(self, path):
        #constructor
        #open the specified database file for reading and perform loading
        with open(path, "r") as handle:
            import json
            self.data = json.load(handle)

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

