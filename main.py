# -*- coding: utf-8 -*-

# A tool to record expenditures, with crude planning features
# by makos
# TODO
# - backbone structure of the program
# - database (json)
# - add conf file to set range of display (month, week)
# - add sum of spendings in given range
# - ... 
# - GUI


from jsonhandler import JSONHandler
from sys import argv, exit
import time

if len(argv) > 1:
    j_handler = JSONHandler(argv[1])
else:
    j_handler = JSONHandler('db.json')

# testing stuff
# j_handler.dump([1442955507.7310047, 'old shit', 5.55])
# j_handler.dump([1445633908.7310047, 'new shit', 4.44])
def main():
    while True:
        option = input("\n(A)dd an entry, (V)iew entries, (S)earch entries, Savings (c)alculator, (Q)uit\n")

        if type(option) == str:
            option.lower()
            if option == 'q':
                exit() # from sys module
            elif option == 'a':
                add_entry()
            elif option == 'v':
                view_entries()
            elif option == 's':
                search()
            elif option == 'c':
                calculator()
            else:
                pass #XXX

def add_entry():
    # Entry fields:
    # Date - added automatically
    # Type
    # Amount spent
    entry = [time.time()]
    action = str(input("Type of spending: "))
    amount = float(input("Amount spent: "))
    entry.append(action)
    entry.append(amount)
    j_handler.dump(entry)

def view_entries():
    entries = j_handler.load()
    if entries == None:
        return "The database is empty."
    for entry in entries:
        if (time.time() - 2678400.0) < entry[0]: # if entry is not older than 31 days, display it
            print("===========")
            print(time.ctime(entry[0]))
            print("Type of expenditure:", entry[1])
            print("Amount spent:", entry[2])
    # print(entries)
    # 31 days in seconds = 2678400
    # 7 days in seconds = 604800
    # 1 day in seconds = 86400


def search():
    pass #XXX

def calculator():
    pass #XXX
main()
# handler = JSONHandler('db.json')
# someshit = ['dingus', 'crap', 555]
# print(handler.load())
# handler.dump(someshit)
# data = handler.load()
# print(handler.load())
# handler.clear()
# print(handler.load())