"""
var1 = 6
var2 = 56
var3 = int(input())
if var3>var2:
    print('greater')
elif var3==var2:
    print('equal')
else:
    print('smaller')

list1 = [5, 7, 3]
if 5 not in list1:
    print('present')
else:
    print('not in list')

print('enter the age is')
age = int(input('the age is:'))
if age > 18:
    print('you car drive')
elif age == 18:
    print('we will thinl on you')
else:
    print('you cant drive')
exercize 2;
45  * 3 = 555, 56 + 9 , 56/ 6= 4

print('enter first number:')
num1 = int(input())
print('enter second number:')
num2 = int(input())
print('selct operators +,-,*,/')
operator = input()
if num1 == 45 and num2 == 3 and operator == '*':
    print(555)
elif num1 == 56 and num2 == 9 and operator == '+':
    print(43)
elif num1 == 56 and num2 == 6 and operator == '/':
    print(4)
elif num1  and num2  and operator == '+':
    print(num1 + num2 )
elif num1  and num2  and operator == '-':
    print(num1 - num2)

elif num1  and num2  and operator == '*':
    print(num1 * num2)

elif num1  and num2  and operator == '/':
    print(num1 / num2)
else:
    print('invalid input')

# loops
list = [['tejas',1],['sanket',2],['rishika',3],['tejal',250]]
dict1 = dict(list)
for item in dict1:
    print(item)
#for item,lollypop in dict1.items():
 #   print(item,lollypop)

items = [int,float,'tejas',5,4,3,4,55,66,6,433,5,444]
for item in items:
    if str(item).isnumeric() and item>=6:
        print(item)

#while loop
#break and continue
i = 0
while(True):
    if i +1<5:
        i = i+1
        print(i,end='      ')
        continue
    print(i + 1, end = ',')
    if i == 44:
        i = i +1
        break
    i = i+1
print('end')


while(True):
    a = int(input('enter a number '))
    if a >= 100:
        print('congratulation greater than 100')
        break
    else:
        print('try again')
        continue

exercize 3

number = 18
total_guesses = 9
count_gusses = 0
remaining_gusses = 0
while(total_guesses > count_gusses):
    number = int(input('enter a number'))
    print(number)
    if (number > 18):
        print('to hight make it low')
    elif (number < 18 ):
        print('to low make it high')
    else:
        print('won')
        print('you acived your target in gusses count:',count_gusses)
        print('still the gusses remain:',remaining_gusses)
        break


    count_gusses = count_gusses + 1
    print('number of guess',count_gusses)
    remaining_gusses = total_guesses - count_gusses
    print('remaining gusses are',remaining_gusses)

# operators in python
#arithmatic operator
print('5 + 6 is', 5+6)
print('5 - 6 is', 5-6)
print('5 * 6 is', 5*6)
print('5 / 6 is', 5/6)
print('5 // 6 is', 5//6) # floor division
print('5 ** 6 is', 5**6) # raise to
print('5 % 6 is', 5%6)

#assignment operator
x = 5
print(x)
x +=7
print(x)

# comparison operator
a = 56565
print( a==5)

#logical operator
i = 5
a = True
b = False
print(a or b)
print(a and b)
print(not a)

#identity operator
a = 1
b = 0
print(a is not b)
print(a is not b)

#membership operator
list1 = [3,3,233,35,32,39]
print(3 not in list1)
print(3  in list1)

#biwise operator
print (0 and 1)
print(1 and 1)
print(0 and 10)
