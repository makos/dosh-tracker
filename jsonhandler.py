#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

class JSONHandler():
    """Small wrapper for JSON encoding/decoding.
    Handles only Python lists, but adding other types should be ez.
    
    Constructor takes 1 argument, 'db', which should be a string containing JSON database file name.
    If file doesn't exist, it will be created with empty JSON array.
    
    Methods:
        load - takes no arguments, decodes JSON and returns it (a list)
        dump - takes 'data' argument (a list), encodes it and saves to file
        clear - wipes the 'db' file"""

    json_data = [] # this is ugly
    def __init__(self, db):
        if type(db) != str:
            print("JSONHandler: Invalid argument; needs to be file name in string format")
        else:
            self.db = db

    def load(self):
        try:
            with open(self.db, 'r') as json_file:
            # json_file = open(self.db, 'r')
                self.json_data = json.load(json_file)
                json_file.close()
            return self.json_data
        except FileNotFoundError:
            print("JSONHandler: No JSON file with name", self.db, "found.") # this should be remade so the file is
            return None                                                     # generated automatically - easy, but won't
                                                                            # it break parts of code in main that use it?
    def dump(self, data):
        self.json_data.append(data)
        with open(self.db, 'w') as json_file:
        # json_file = open(self.db, 'w')
            json.dump(self.json_data, json_file, indent = 4)
            json_file.close()
        print("JSONHandler: Data dumped into", str(self.db))

    def clear(self, prompt = True):
        if prompt:
            option = input("JSONHandler: Database wipe - do you really want to do this? y/n ")
            if option == 'y':
                self.json_data = []
                with open(self.db, 'w') as json_file:
                # json_file = open(self.db, 'w')
                    json.dump(self.json_data, json_file)
                    json_file.close()
                print("JSONHandler: Database erased")
        else:
            self.json_data = []
            # json_file = open(self.db, 'w')
            with open(self.db, 'w') as json_file:
                json.dump(self.json_data, json_file)
                json_file.close()
            print("JSONHandler: Database erased")