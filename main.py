#!/usr/bin/python3
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

STEP = 2678400.0 # default cutoff for entry display - one month
# 31 days in seconds = 2678400
# 7 days in seconds = 604800
# 1 day in seconds = 86400
CALC_RATIOS = (0.7, 0.2, 0.1) # ratios used for savings calculator
# first is living costs, second is savings, third is luxury items (not necessary for living)
DEFAULTS = [["step", STEP], ["calc_ratios", CALC_RATIOS]]

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
    print("Entry added.")

def view_entries():
    entries = j_handler.load()
    total = 0

    if entries == None:
        return "The database is empty."
    for entry in entries:
        if (time.time() - STEP) < entry[0]: # if entry is not older than STEP variable (31 days by default), display it
            print("===========")
            print(time.ctime(entry[0]))
            print("Type of expenditure:", entry[1])
            print("Amount spent:", entry[2])
            total += entry[2]
    print("===========\nTotal spent:", total)

def search():
    pass #XXX

def calculator():
    global CALC_RATIOS
    paycheck = float(input("Last paycheck (number): "))
    living = paycheck * CALC_RATIOS[0]
    savings = paycheck * CALC_RATIOS[1]
    luxury = paycheck * CALC_RATIOS[2]
    print("Money for living (food, rent etc.):", living)
    print("Money for savings account:", savings)
    print("Disposable money for luxury items:", luxury)

def read_config(cfg_file=".config"):
    global STEP, CALC_RATIOS, DEFAULTS
    cfg_handler = JSONHandler(cfg_file)
    cfg_contents = cfg_handler.load()
    
    if cfg_contents == None:
        cfg_handler.dump(DEFAULTS)
    else:
        for level in cfg_contents:
            for option in level:
                if option[0] == "step":
                    STEP = option[1]
                elif option[0] == "calc_ratios":
                    CALC_RATIOS = option[1]
def show_help():
    print("Usage: python3 main.py [JSON file name] [-c -h] [config file name]")
    print("\nProviding JSON and config files is optional, defaults are created automatically.")
    print("If you provide your own JSON file, it needs to have a .json extension.")
    print("\nOptions:\n-c\tuse a provided config file, see README for config syntax\n-h\tshow this help")
    exit()

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
            elif option == 'debug':
                global STEP, CALC_RATIOS
                print("STEP = ", STEP)
                print("CALC_RATIOS = ", CALC_RATIOS)
            elif option == 'clear':
                j_handler.clear()
            else:
                pass #XXX

if len(argv) > 1:
    if ".json" in argv[1]:
        j_handler = JSONHandler(argv[1])
        if len(argv) > 2:
            if (argv[2] == "-c") and (len(argv) > 3):
                read_config(argv[3])
            else:
                read_config()
        else:
            read_config()
    elif argv[1] == "-h":
        show_help()
    elif (argv[1] == "-c") and (len(argv) > 2):
        j_handler = JSONHandler("db.json")
        read_config(argv[2])
    else:
        show_help()
else:
    j_handler = JSONHandler("db.json")
    read_config()

# testing stuff
# j_handler.dump([1442955507.7310047, 'old shit', 5.55])
# j_handler.dump([1445633908.7310047, 'new shit', 4.44])
# handler = JSONHandler('db.json')
# someshit = ['dingus', 'crap', 555]
# print(handler.load())
# handler.dump(someshit)
# data = handler.load()
# print(handler.load())
# handler.clear()
# print(handler.load())

main()