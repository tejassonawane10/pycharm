"""
# request module explore
# free api post request share
import requests
# get request - url contain fetch
r = requests.get(url=)
print(r.text)
print(r.status_code)

url = "www.something.com"
data ={
    "p1":4,
    "p2":8,
}
r2 = requests.post(url=url, data=data)

# JSON module - java script object notation
#task1 - json.load #read json document for
#task2 - what is sort_keys parameter in dumps# sorting data
import json
data = '{"var1":"harry", "var2":56} '
parsed = json.loads(data)
print(type(parsed))
print(parsed['var1'])# data can be accessed by key value pair

data2 = {
    "channel_name":"codewithharry",
    "cars":['bmw', 'audi a8', 'ferrari'],
    "fridge":('roti', 540),
    "isbad": False
}
jscomp = json.dumps(data2)# java readable form
print(jscomp)

import pickle# sambhal kr rakhna prservation

# pickling a python object
#cars = ["Audi", "BMW", "Maruti Suzuki", "Hrryti Tuzuki"]
#file = "mycar.pkl"
#fileobj = open(file, "wb")
#pickle.dump(cars, fileobj)
#fileobj.close()

file = "mycar.pkl"
fileobj = open(file, 'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))


#regular expression
#findall, search, split, sub, finditer

# convert .py to .exe - by using pyinstaller module
#pyisntaller --onefile main.py

# Raise in python
# two bult in exception practical use

a = input("what is your name")
b = input("how much do you earn")
if int(b) == 0:
    raise ZeroDivisionError("stop")
if a.isnumeric():
    raise Exception('number is not allowed')
print(f'Hello {a}')
#100 line taking 1 hour


c = input("enter your name")
try:
    print(a)
except Exception as e:
    if c == "tejas":
        raise ValueError('Tejas is blocked he is not allowed')
    print("Exception handled")

# Diferrence between 'is' and '=='

 == - valuue euality - two object are the same value
 is - refrence equality - two reference refer to the same object

# python is command line utility
import argparse
import sys
def calc(args):
    if args.o=='add':
        return args.x + args.y

    elif args.o == 'mul':
        return args.x * args.y
    elif args.o == 'sub':
        return args.x / args.y
    elif args.o == 'div':
        return args.x / args.y
    else:
        print('something went wrong')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--x', type=float, default=1.0, help='Enter first number. this is a utility for calculation. Please contact harry bhai')

    parser.add_argument('--y', type=float, default=3.0, help='Enter second number. this is a utility for calculation. Please contact harry bhai')

    parser.add_argument('--o', type=str, default="add", help='this is a utility for calculation. Please contact harry bhai')
    args = parser.parse_args()
    sys.stdout.write(str(calc(args)))
"""

