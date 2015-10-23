# -*- coding: utf-8 -*-

import json

class JSONHandler():
    """Small wrapper for JSON encoding/decoding.
    Handles only Python lists, but adding other types should be ez.
    
    Constructor takes 1 argument, `db`, which should be a string containing JSON database file name.
    If file doesn't exist, it will be created with empty JSON array.
    
    Methods:
        load - takes no arguments, decodes JSON and returns it (a list)
        dump - takes `data` argument"""

    json_data = []
    def __init__(self, db):
        if type(db) != str:
            print("JSONHandler: Invalid argument; needs to be file name in string format")
        else:
            self.db = db
        # data = self.load(db)
        # if data == None:
        #     self.dump([], db)
        # JSONHandler.json_data = data
        # self.dummy()

    def load(self):
        try:
            json_file = open(self.db, 'r')
            JSONHandler.json_data = json.load(json_file)
            json_file.close()
            return JSONHandler.json_data
        except FileNotFoundError:
            print("JSONHandler: No JSON file with name", self.db, "found.")
            return None

    def dump(self, data):
        JSONHandler.json_data.append(data)
        json_file = open(self.db, 'w')
        json.dump(JSONHandler.json_data, json_file)
        json_file.close()
        print("JSONHandler: Data dumped into", str(self.db))

    def clear(self):
        option = input("JSONHandler: Database wipe - do you really want to do this? y/n")
        if option == 'y':
            JSONHandler.json_data = []
            json_file = open(self.db, 'w')
            json.dump(JSONHandler.json_data, json_file)
            json_file.close()
            print("JSONHandler: Database erased")
        else:
            pass
if __name__ == '__main__':
    prog = JSONHandler
    prog()