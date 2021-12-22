#Generator
"""
iterable - python object __iter__ or __getitem__ method lagu hoti hai
iterator - __next__ define in it only present in string not in int yeh layak hota hai generate krne ke
iteration -

Genarator is same as iterator we can only one traverse

generator factoriala and fibonaaci series program

def gen(n):
    for i in range(n):#to secure ram we use generator, its used to generate capable when need we use it and zaroorat padegi tab iterate kr lenge
        yield i# on the fly generate krega
g = gen(3)# geerator is iterator and can be iterate once
print(g)
#g.__next__()
#print(g.__next__())
#print(g.__next__())
#print(g.__next__())

#for i in g:
 #   print(i)# no error stop iteration for loop automatically handled it

h = 'tejas'
a = iter(h)
print(a.__next__())
print(a.__next__())
for ch in h:# iterable string is __iter__present in it
    print(ch)

# python Comprehensions
ls = []
for i in range(100):
    if i%3==0:
        ls.append(i)
print(ls)

ls = [i for i in range(100) if i%3==0]
print(ls)

#dictionary Comprehensions
dict = {i:f"item {i}" for i in range(1000) if i%100 == 0}#scalability increarse
print(dict)

dict = {i:f"Item {i}" for i in range(5)}
dict1 = {value:key for key ,value in dict.items()}
print(dict1,"\n", dict)

dresses = {dress for dress in ['dress1','dress2','dress1','dress2','dress1','dress2','dress1','dress2',]}
print(type(dresses))

#generator Comprehensions
Evens = (i for i in range(100) if i%2==0 )
#print(type(Evens))
print(Evens.__next__())
print(Evens.__next__())
#for item in Evens:
 #   print(item)

user input list item how much wihich type of comprehension

no_of_list = int(input('Enter number of items you want to add:'))
input_string = input('Enter a list element separated by space')
list = input_string.split()
t = int(input('Which type of comprehension do you wamnt 1. List 2. Dictionary 3. set'))
if t ==1 :
    ls = [i for i in list]
    print(ls)
    print(type(ls))
elif t ==2:
    dict1 = {f'item{i}':i for i in list}
    print(dict1)
    print(type(dict1))
elif t==3:
    s = {i for i in list}
    print(s)
    print(type(s))

# for loop with else - for loop normally end ho tabhi else chanlega nor break statement no continue
khana = ["roti","sabji","chawal"]
for item in khana:
    if item == 'rotiroll':
        break
else:
    print('your item was ot found')

#Function caching
import time
from functools import lru_cache
@lru_cache(maxsize=3)# 3 calls save
def some_work(n):#fuction i/p o/p value save so another time we use it it access properly its is called function caching
    #some task taking n second
    time.sleep(n)
    return n

if __name__ == '__main__':

    print("now run some_work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(9)
    print('done..calling again')
    some_work(3)
    print('called done')

#else,finally with try and except

f1 = open('filewrite.txt')

try:
    #pass
    f = open('does.txt')

except Exception as t:# we can right more than one except statement
    print(t)

else:# only else and except only run at a time
    print('this will only run if exception is not run')

finally:# used for file clean up
    print('Run this anyway')
    f1.close()
print('Imortant stuff')

# Coroutines in python
def searcher():
    import time
    # 4 sec consuming task
    book = "this is book on tejas and rishika love story"
    time.sleep(4)

    while True:# this routine run every tme
        text = (yield)# sercher is use as coroutine
        if text in book:
            print("your text in the book")
        else:

            print("text is not in the book")

search = searcher()# instance
print("serch os started")
next(search)
print("next method run")
search.send('tejas')
input("press any key")
search.send("tejas and")
search.close()# coroutine off after that serch.send not work because all sources are get free


input("press any key")
search.send("tfghgdyg")
input("press any key")
search.send("tejas ahvhhd")
input("press any key")
search.send("liufbgd")

import time
def names():
    names = 'tejas rishika tejal sanket i love u'
    time.sleep(2)

    while True:
        text = (yield)
        if text in names:
            print('name is present')
        else:
            print('name is not prsent')
name = names()
next(name)
name.send(input("type your name"))
name.close()
"""
# OS Module
import os
#print(dir(os))
#print(os.getcwd())
#print(os.listdir())
#os.mkdir("rishu/tejal")
#os.makedirs("")
#os.rename('main1.py')
#print(os.environ.get(''))
