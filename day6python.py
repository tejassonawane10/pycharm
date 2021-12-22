#python decorators - fuction functionality modified
"""
copy one func element to another
def function1():
    print('subscribe now')
func2 = function1
del function1
func2()
# fuction with help fuction we can also retrun it
def funcret(num):
    if num == 0:
        return print
    if num == 1:
        return sum
a = funcret(1)
print(a)

# we can give fuc as argument
def executor(func):
    func("this")
executor(print)

def dec1(func1):
    def nowexec():
        print('executing now')
        func1()
        print('executed')
    return nowexec
@dec1 # use when we want one program multipl place that like using blue print we use it
def who_is_tejas():
    print('tejas is good boy')
# who_is_tejas = dec1(who_is_tejas)   this line return as similsr as @dec1
who_is_tejas()

# oops concept - class and object
classes - template
object - the thing written with the help of template (instance of the class
why class make -DRY - class follow dry do not repeat your self


class student:      # contain always blueprint or template to make work easy
    pass
harry = student() # both are seprate object
larry = student()
harry.name = 'harry' # instance variable of harry
harry.std = 12
harry.section =1
larry.std = 9
larry.subjects = ['hindi','physics']
print(larry.subjects, harry.std)

# differnce between instance and class varaiable

class Employee:
    no_of_leaves = 8 # same for all objects of class, epmployee value only change by class, class variable
    pass
harry = Employee() # object
rohan = Employee()
#all the object own property
harry.name = 'harry'
harry.salary = 455
harry.role = 'instructor'

rohan.name = 'rohan'
rohan.salary = 4555
rohan.role = 'student'

print(rohan.no_of_leaves, harry.no_of_leaves)
print(rohan.__dict__)
print(Employee.__dict__)
rohan.no_of_leaves = 9 # here create new instance variable of object own property
print(rohan.__dict__)#definesd alredy it is attribute
Employee.no_of_leaves = 9 # instance cant change class variable only class can.
print(Employee.__dict__)
print(Employee.no_of_leaves)


#self and __init__ and constructor
#oops organize the work, code reusability
# employee ko arguments thenne ke tarike ko constructor kehante hai init

class Employee:
    no_of_leaves = 8
    # object banate tim all work done by constructor init
    def __init__(self, aname, asalary, arole): # here self here is obj that create self = harry or rohan
        self.name = aname #name instance variable and aname is argumnet
        self.salary = asalary
        self.role = arole

    def printdetails(self):  # method self - object self if mothod use rohan then self converted to rohan
        return f" TheName is {self.name}.salary is {self.salary} and role is {self.role}"

harry = Employee('harry', 255, 'instructor') # object, WHEN ARGUEMENT GIVEN TO CLASS THAT ARGUMENT HANDLED NY INIT ALWAYS ALL ARGUMENTS GOES TO CONSTRUCTOR
#rohan = Employee()

#harry.name = 'harry'
#harry.salary = 455
#harry.role = 'instructor'

#rohan.name = 'rohan' #instance variable
#rohan.salary = 4555
#rohan.role = 'student'

#print(rohan.printdetails()) #o/p - Name is rohan.salary is 4555 and role isstudent
# rohan goes into prindetails and self use to handled it
#print(harry.printdetails())
#print(rohan.no_of_leaves)# class variable can be access by instance
print(harry.salary)

# class method

class Employee:
    no_of_leaves = 8
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



harry = Employee('harry', 255, 'instructor') # object, WHEN ARGUEMENT GIVEN TO CLASS THAT ARGUMENT HANDLED NY INIT ALWAYS ALL ARGUMENTS GOES TO CONSTRUCTOR
rohan = Employee('rohan', 455, 'student')
harry.change_leaves(34)
print(harry.no_of_leaves) #first serch for instancre variable then go towards class variable
print(Employee.no_of_leaves)


# class method alternative constructor


class Employee:
    no_of_leaves = 8
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
harry = Employee('harry', 255, 'instructor') # object, WHEN ARGUEMENT GIVEN TO CLASS THAT ARGUMENT HANDLED NY INIT ALWAYS ALL ARGUMENTS GOES TO CONSTRUCTOR
rohan = Employee('rohan', 455, 'student')
karan = Employee.from_str('karan-480-student')
print(karan.salary, karan.no_of_leaves)
harry.change_leaves(34)
print(harry.no_of_leaves) #first serch for instancre variable then go towards class variable
print(Employee.no_of_leaves)
rohan.change_leaves(110)
print(harry.no_of_leaves)
print()

# static method


class Employee:
    no_of_leaves = 8
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


harry = Employee('harry', 255, 'instructor') # object, WHEN ARGUEMENT GIVEN TO CLASS THAT ARGUMENT HANDLED NY INIT ALWAYS ALL ARGUMENTS GOES TO CONSTRUCTOR
rohan = Employee('rohan', 455, 'student')
karan = Employee.from_str('karan-480-student')
print(karan.salary, karan.no_of_leaves)
harry.change_leaves(34)
print(harry.no_of_leaves) #first serch for instancre variable then go towards class variable
print(Employee.no_of_leaves)
rohan.change_leaves(110)
print(harry.no_of_leaves)
print(Employee.print_good(''))

# Abstraction and Encapsulationn
#abstraction means kissi kamm ko tukdo me tod dena pc ->mouse,laptop all are layer of abstraction for full computer
# to acieve abstraction in ooops we need to encapsulation
#encapsulation means hide the details or we can say hide the implimentation aam khao guthali matt gino

# inheritance - parents gunn aa jate hai child me, in oops class ko copy krke or cheeze usmein add krna


class Employee:
    no_of_leaves = 8
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

class programmer(Employee):# single inheritance
    no_of_holiday = 56
    def __init__(self, aname, asalary, arole, language):#warning second constructor not create use super keyword here
        self.name = aname  # name instance variable and aname is argumnet
        self.salary = asalary
        self.role = arole
        self.language = language

    def printprog(self):
        return f" The programmer is {self.name}.salary is {self.salary} and role is {self.role} and the languages are {self.language}"


harry = Employee('harry', 255, 'instructor') # object, WHEN ARGUEMENT GIVEN TO CLASS THAT ARGUMENT HANDLED NY INIT ALWAYS ALL ARGUMENTS GOES TO CONSTRUCTOR
rohan = Employee('rohan', 455, 'student')

shubham = programmer('shubham', 555, 'programmer', ['python'])
karan = programmer('karan', 770, 'programmer', ['python', 'c++'])

print(karan.printprog())
print(karan.printdetails())
print(harry.printdetails())
print(shubham.no_of_holiday)


class Employee:
    var = 8
    no_of_leaves = 8
    # object banate time all work done by constructor init
    def __init__(self, aname, asalary, arole): # here self here is obj that create self = harry or rohan
        self.name = aname #name instance variable and aname is argumnet
        self.salary = asalary
        self.role = arole

    def printdetails(self):  # method self - object self if method use rohan then self converted to rohan
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

class player:
    var = 9
    no_of_games = 4
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f" The name is {self.name}.game is {self.game} "

class coolprogrammer(Employee, player):  # order is important, if variable or any attribute in both class same then first class written so child class take that value
#class coolprogrammer(player, Employee):  # order is important

    #var = 10
    language =  'c++'
    def printlanguage(self):
        print(self.language)


harry = Employee('harry', 255, 'instructor') # object, WHEN ARGUEMENT GIVEN TO CLASS THAT ARGUMENT HANDLED NY INIT ALWAYS ALL ARGUMENTS GOES TO CONSTRUCTOR
rohan = Employee('rohan', 455, 'student')
shubham = player('shubham', ['cricket'])
karan = coolprogrammer('karan', 100000, 'coolprogrammer')
#karan = coolprogrammer('karan', 'cricket')
det = karan.printdetails()
#karan.printlanguage()
#print(det)
print(karan.var)

# multilevel inheritance -

class Dad:
    basketball  =  1
class Son(Dad):
    basketball = 3
    dance = 1
    def isdance(self):
        return f"yes i dance {self.dance} no of times"
class Grandson(Son):
    dance = 6

    def isdance(self):# new cpoy lagu hoga
        pass
        return f"Jackson yeah!" \
                f"yes i dance awesomly {self.dance} no of times"

darry = Dad()# instance
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)
# electronic device, pocket gadget, pocket phone multilevel
class Device():
    Android = 2
class Pocket_gadjet(Device):
    Android  = 4
    version = 2
class Pocket_phone(Pocket_gadjet):
    pass

goggle = Device()
samsung = Pocket_gadjet
duo = Pocket_phone
print(duo.Android)
"""








































































































