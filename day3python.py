"""
#short hand if else

a = int(input('enter 1:'))
b = int(input('enter 2:'))
#if a>b : print('a b se bada hai bhai|')
print('b a se bada hai bhai|') if a<b else print('a b se bada hai bhai')

#funtion

a = 9
b = 8
c = sum ((a,b)) # buit in func
print(c)

def function1(a, b):
    print('1', a + b)

def function2(a, b): # user defined
    this is func which will calculate average of two string    #this not comment this doc string function first line to identify what function do
    avg = (a+b)/2
    print(avg)
    return avg #return value  (function having doc string)

v = function2(5, 7)
print(v)
#print(function2.__doc__) # for printing doc string

# try except exception handling

num1 = input('enter value')
num2 = input('enter value')
try:
    print("addition of num1 and num2 is",int(num1) +int(num2))

except Exception as tejas:  # when program not to give any error after errot occur and continue running
    print(tejas)
print('any how this want to print ')

# file i/o basics

"r" - open file for reading
"w"- open file for wriiting
"x" -create files if not exist, if file alresdy exist operation failed
"a" - add more content to file at end
"t" - text mode, text data as string deal
"b" - binary mode
"+" - open for update read and eritr both
text and read mode both are default
print(func1.__doc__)

f = open("tej.txt", "rt")
#print(f.readlines()) # for converted into list
#print(f.readline())
#print(f.readline())
#print(f.readline())
#content = f.read()
#print(content)
#for line in f:
#    print(line,end = '')
f.close()

f = open("filewrite1.txt", "w")
a = f.write("tejas is good\n")
print(a)
f.close()

f = open("filewrite1.txt", "a")
a = f.write("tejas is good\n")
print(a)
f.close()

#handle read and write both
f = open("filewrite.txt", "r+")
print(f.read())
f.write("\nthank you")
f.close()

# exercize - pattren print
#input = int n
boolean = 1 or 0
*
**
***
****
false
****
***
**
*

n = int(input("enter the how many * do you want:\n"))
user_input = bool(int((input('tpye of star pattern do you want\n'))))
if user_input == 0:
    for i in range(1, n+1):
        for j in range(1, i+1):
            print('*', end=' ')
        print('')
elif user_input == 1:
    for i in range(n +1 , 0 ,-1):
        for j in range(0, i-1):
            print('*', end=" ")
        print('')
else:
    print('wrong input')

f = open('tej.txt')
print(f.tell()) # telling user where the file pointer current location is
print(f.readline())
f.seek(3)# seek is used to resat the pointer
print(f.tell()) # telling user where the file pointer current location is
print(f.readline())
f.seek(6)
print(f.tell()) # telling user where the file pointer current location is
print(f.readline())
f.close()

#file opening with block

with open('tej.txt') as f: # using with will allow us not to use f.close() so its beneficial for user
    a = f.readlines()
    print(a)

with open('tej.txt') as f: # using with will allo us not to use f.close() so its beneficial for user
    a = f.readline()
    print(a)
"""
