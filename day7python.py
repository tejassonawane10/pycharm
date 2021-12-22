"""
# Public, Private and Protected Specifier
public variable - paper with info ghar ke bahar chipkana
protected variable - paper with info ghar ke anadr chipkana( start with unerscore_variable)
private variable - paper with info apne khud ke personal room me chipakana( start with double unerscore_variable)


class Employee:
    no_of_leaves = 8 # public variable
    _protect = 10# protected variable outer class cant use it
    __private = 98# private variable use only this class

    # object banate tim all work done by constructor init
    def __init__(self, aname, asalary, arole): # here self here is obj that create self = harry or rohan
        self.name = aname #name instance variable and aname is argumnet
        self.salary = asalary
        self.role = arole

    def printdetails(self):  # method self - object self if mothod use rohan then self converted to rohan
        return f" TheName is {self.name}.salary is {self.salary} and role is {self.role}"

    @classmethod # class isntance variable access by class and instant both
    # its also use as alternatrive costructor and our instance can also change the class variable value
    def change_leaves(cls, newleaves):#class only cls - class instance
        cls.no_of_leaves = newleaves

    @classmethod #alternative constructor
    def from_str(cls, string):
        #params = string.split('-')
        #print(params)
        #return cls(params[0], params[1], params[2])

     return cls(*string.split("-"))# one linear

    @staticmethod# function that ony return some thing who dosent take self or class argument b only our own work
    def print_good(string): # efficiency increase when we dont want ro use 'self'
        print('this is good' + string)

emp = Employee('tejas', 4999, 'programmer')
#print(emp.__private)# no print python create name mangling not acces like this if want acces then use _Employee
print(emp._Employee__private)#python save like this if not use outer side so python save this in with complex name
# private variable having name mangling saving nam in complex manner
# polymorphism - is a concept - meaning is abilty to take various form
#override - new method lagu hoga purana nahi hoga
print(5+6)
print('5'+'6')
# this both example are called polymorphism
# acieve using override and using dunder method
abstraction
Encapsulation
Inheritance
Polymorphism
"""""
#super and overiding in classes
#if we have two constructor and we want to access out old one but not possible it because we overight it that time super use
class A:
    classvar1 = 'i am a class variable in class A'
    def __init__(self):
        self.var1 = "i am class A's constructor"
        self.classvar1 = 'instance variable in class A'
        self.special = 'special'

class B(A):
    classvar1 = 'i am in class B'  # attribute override here
    def __init__(self):#overwrite
        #super().__init__()# super class ke constructor ko call kr do, VALUE SAME
        self.var1 = "i am class B's constructor"
        self.classvar1 = 'instance variable in class B'
        super().__init__()# VALUE CHANGE, super class variable
        print(super().classvar1)
a = A()
b = B()
print(b.special, b.var1, b.classvar1)

# diamond shape problem in multiple inhritance
class A:

    def met(self):
        print('this method from class A')

class B(A):

    def met(self):
        print('this method from class B')

class C(A):

    def met(self):
        print('this method from class C')

class D(C, B):

    def met(self):
        print('this method from class D')
a = A()
b = B()
c = C()
d = D()
d.met()

#Operator overloading and Dunder method(special method)
#__method__(called dunder method with underscore)
class Employee:
    no_of_leaves = 8
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f" TheName is {self.name}.salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    def __add__(self, other):# dunder add and helping operator overloading
        return self.salary + other.salary

    def __repr__(self):
        return f"Employee('{self.name}', {self.salary}, '{self.role}')"
#first prefrence given to str then repr if str absent then only repr direct aacess
    def __str__(self):

        return f" TheName is {self.name}.salary is {self.salary} and role is {self.role}"


emp1 = Employee('harry',455,'programmer')
#emp2 = Employee('rohan',45,'cleaner')
#print(emp1 + emp2) #mapping operator to function serach krna hai 3 special method operator overloadiing
print(str(emp1))

# abstract base class and @abstractbasemethod
# class which work as base class
#from abc import ABCMeta, abstractmethod
from abc import ABC, abstractmethod
class shape(ABC):# all lower method is mandatory to use printarea function
    @abstractmethod # for forcing  one of the method or function
    def printarea(self):# we cant make abstract base class object and instance
        return 0
class Reactangle:
    type = 'Rectangle'
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printarea(self):
        return self.length * self.breadth
rect1 = Reactangle()
print((rect1.printarea()))

# setters and property decorators
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@.codewithharry.com"

    def explain(self):
        return f"this emoplyee is {self.fname} {self.lname}"

    @property # as function if you dont want to access
    def email(self):

        if self.fname == None or self.lname == None:
            return "Email is not set, please set it using setter"
        return f"{self.fname}.{self.lname}@.codewithharry.com"

    @email.setter
    def email(self, string):
        print(('setting know'))
        names = string.split("@")[0]#split used to spilt and convert it into list
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):# we not delet attribute in oops we generally set it to None
        self.fname = None
        self.lname = None

hindustani_supporter = Employee('hindustani', 'supporter')
nikhil_raj_pandey = Employee('nikhil', 'raj')
print(hindustani_supporter.email)
hindustani_supporter.fname = "US"
print(hindustani_supporter.email)# name same constrtctor run first and intialized value to improve this we used setter
hindustani_supporter.email = 'this.that@codewithharry.com'# setter used here
print(hindustani_supporter.email)
print(hindustani_supporter.fname)
print(hindustani_supporter.lname)
del hindustani_supporter.email # this command find deleter so we make deleter
print(hindustani_supporter.email)


# Object Introspection - info of one of thata object jankar hasil karna
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        #self.email = f"{fname}.{lname}@.codewithharry.com"

    def explain(self):
        return f"this emoplyee is {self.fname} {self.lname}"

    @property # as function if you dont want to access
    def email(self):

        if self.fname == None or self.lname == None:
            return "Email is not set, please set it using setter"
        return f"{self.fname}.{self.lname}@.codewithharry.com"

    @email.setter
    def email(self, string):
        print(('setting know'))
        names = string.split("@")[0]#split used to spilt and convert it into list
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]

    @email.deleter
    def email(self):# we not delet attribute in oops we generally set it to None
        self.fname = None
        self.lname = None
skillf = Employee("Tejas","sonawane")# python everything is object
print(skillf.email)
print(type(skillf))#object intrspection
print(id(skillf))
print(id("that"))
skillf = "tejas sosnawnw"
print(dir(skillf))# kya kya khilwad kr sakte hai

import inspect # object inspec
print(inspect.getmembers(skillf))
"""
#mini project online management system
#create library class - method books display - donate book - return book - lend book
# constructor harrylibar = library(list of books, libraryname)

#dictionary maintain key books value name of person