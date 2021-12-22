# scope global variable global keyword

"""
l = 10 #globl variable anyone use it global scope
def func1(n):
    #l = 5# local variable first preference local scope
    m = 8
    global l # function know have a permission to change the gloval variable with help of global keyword
    l = l + 10
    print(l,m)

    print(n,"i have printed")

func1('this is me')
print(l)
#print(m)# local cant be access any where


def tejas():
    a = 20
    def sanket():
        pass
        global a # value not change after using global here because when we use this its go out of all func and all if availablke the change or other than local one get printed
        a = 88
    print("before calling sanket()",a)
    sanket()
    print("after calling sanket()",a)
tejas()
print(a)
print(a) # print 88 and create one global variable with value of 88

# recursion: recursive vs iterative approach

def factorial(n):
    #parameter n integer retrn n*n-1*n-3....1
    fac = 1
    for i in range(n):
        fac = fac * (i+1)

    return fac

number = int(input('enter the number'))
print("factorial using iterative method",factorial(number))

def fact_recurssive(n):
    if n==1:
        return 1
    else:
        return n * fact_recurssive(n-1)

n = int(input('entervthe number'))
print("factorial using recurssive method",fact_recurssive(n))

def fibonnaci(n):
    if n == 0:
        return 0
    elif n ==1 or n == 2:

        return 1
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)
n = int(input("enter a number:\n"))
print("the fibonnaci series is", fibonnaci(n))

#lambda function at anonymous function
one liner function
its used when you have to create function but not using def a short function it is.

def minus(x, y):
    return x-y
minus = lambda  x, y : x-y
print(minus(9,4))
print(minus(9,4))

# lambda using sort function
#def a_first(a):
 #   return a[1]
a = [ [1,4], [ 5,6], [8,23]]
a.sort(key= lambda x:x[1]) # here key = is used to assign function
print(a)

import random
random_number = random.randint(0, 5)
rand = random.random() * 100
#print(rand)
#print(random_number)
lst = [ 'star plus', 'dd1', 'aaj tak', 'code wit harry']
ch = random.choice(lst)
print(ch)
use two python module and use function

# f"" string
string formatting

import math
me = 'harry'
a1 = 3
#a = "this is %s"%me

#a = "this is {} {}"
#b = a.format(me, a1)# string formatting
#print(b)

a = f"this is {me} {a1} {4*65} {math.cos(0), }, 'i love u'" # f stands for fast
print(a)
#module time info find out
"""