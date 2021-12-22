"""
# *args and **kwarge
#def function_name_print(a,b,c,d,e):
#    print(a,b,c,d,e) #not skillable

# args use when the input change multuiple time and we dont wanr erroe

def funargs(normal, *argsrohan, **kwargsbala):# contain in tuple rule is normal-> then args-> then kwargs
    #print(type(args)) #tuple
    print(normal)
    for item in argsrohan:
        print(item)
    print('\nnow i would like to introduced some of our heros')
    for key, value in kwargsbala.items():
        print(f"{key} is {value}")
#function_name_print('harry','rohan','tejas','sanket','rishika')
har = ['harry','rohan','tejas','sanket','rishika','tejal']
normal = 'I AM NOMAL ARHUMENTS AND STUDENTS ARE'
kw = {'rohan':'monitor','harry':'fitness instructor','tejas':'programmer', 'rishika':'tejas girlfriend'}
funargs(normal, *har, **kw)

#time module
import time
initial = time.time() # time contain time funct having tick of one sec
k = 0
while(k<45):
    print("this is tejas")
    time.sleep(2)
    k+=1

print("while loop ran in",time.time() - initial, 'seconds')
initial2 = time.time()
for i in range(45):

    print('this is tejas')

#print("for loop ran in",time.time() - initial2, 'seconds')

#localtime = time.asctime(time.localtime(time.time()))
#print(localtime)

# virtual enviroment and requirement
"""
#enmerates function - it takes iterable and and with them having and maintaining count of itration
l1 = ['bhindi','aloo','chopsticks','chowmein']
i = 1
for item in l1:
    if i%2 != 0:
        print(f"jarvis please by {item}")
    i = i +1
l1 = ['bhindi','aloo','chopsticks','chowmein']
for index, item in enumerate(l1):
    if index%2 == 0:
        print(f"jarvis please by {item}"
"""
how import works

import sys
print(sys.path) # importing hierrarchyfromm
import rishu
from rishu import a
print(a)# wrong way its create complexity
print(rishu.a)# best way
rishu.printjoke('this is me')

# if __name__ == __main__

#join function
lis = ['john','cena','randy','orton','sheamus',
       'khali','jindar mehal']
#for item in lis:
 #   print(item,'and', end= ' ')
a = ' and '.join(lis)
print(a,'other wwe superstars')

################################map
numbers = [ '3','34','64']
numbers = list(map(int, numbers))#map always return object
# map func -> apply  one fuc to overall list
#for i in range(len(numbers)):
 #   numbers[i] = int(numbers[i])
numbers[2] = numbers[2] + 1
#print(numbers[2])
#def sq(a):
#    return a*a
#num = [2,3,4,5,6,7,8,9]
#square = list(map(sq, num))
#print(square)

num = [2,3,4,5,6,7,8,9]
square = list(map(lambda x:x*x*x, num))
print(square)


def square(a):
    return a*a
def cube(a):
    return  a*a*a
func = [square, cube]
for i in range(5): # when we used map list use also thier
    val = list(map(lambda x:x(i), func))
    print(val)

####################### filter
# filter function - creating list where given func return true
list_1 =[1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num > 5
greater_than_5 = list(filter(is_greater_5, list_1))
print(greater_than_5)


#############################reduce
# reduce is part of functools module
from functools import reduce
list_1 = [1,2,3,4,2]
num = 0
for i in list_1:
    num = num + i
#print(num)

from functools import reduce
num = reduce(lambda x,y:x*y, list_1) # reduce work like this
print(num) """