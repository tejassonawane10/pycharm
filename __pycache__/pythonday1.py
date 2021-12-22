
#python('hello world')
print('tejas', end = ' vishwanath ')
print('sonawane')
print('tejas','sonawane')
print('tejas','vishwanath','sonawane')
print('c:\tejas')
print('c:\\nejas')
print("c:\'tejas'")
print('tejas \n is ggod \t boy \q')
print('tejas \b sonawane')
"""
var1 = 'hello world' # string variable
var2 = 4 # integer variagble
var3 = 36.7 # float variable
#print(var1)
#print(type(var3)) # type function
#print(var2 + var3)
var_a = '54'
var_b = '32'
#print(int(var_a) + int(var_b)) # typecasting

"""
str()
int()
float()

"""
#print(10 * 'hello world \n')
#print(100 *str(int(var_a) + int(var_b)))
"""print('enter your num:')
inpnum = input()
# print("you enter:", int(inpnum) + 10)

print('enter your numbers:')
a = int(input())
b = int(input())
print('sumk is ',a + b)
"""
# string

mystr = 'tejas is a goodboy'
#print(len(mystr))
#print(mystr[::-1])reverse
#print(mystr[::-2])

"""
print(type(mystr))
print(mystr.isalnum()) #true or false SPACES IS  THEIR
print(mystr.isalnum()) # TRUE OR FALSE SPACE IS NOT
print(mystr.isalpha())
print(mystr.endswith('boy'))
print(mystr.count('o'))
print(mystr.capitalize())
print(mystr.find('is'))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace('is', 'are'))
# index start from 0 >> 0123456        -1-2-3-4-5-5<<<
"""

# list
grocery = [ 'harpic', 'vim bar', 'deodrant', 'bhindi', 'lollypop', 56]
#print(grocery[3])
numbers = [2,7,9,11,3]
#print(numbers[2])
#numbers.sort()
#numbers.reverse()
#print(numbers[1:5:2]) # not usede -1 more value like -2,-3 for rverse it not work properly
#print(numbers)
#print(len(numbers))
#print(max(numbers))
#print(min(numbers))
#numbers.append(22)
#print(numbers)
"""
numb = []
numb.append(22)
numb.append(22)
numb.append(22)
print(numb)

numbers.insert(1, 67)
print(numbers)
numbers.insert(4, 5545)
print(numbers)
numbers.remove(9)
numbers.remove(5545)
numbers.pop()
print(numbers)
"""

#tuple
numbers = [2,7,9,11,3]
##numbers[1]= 2121
#print(numbers)
# mutable = can cahnge(list), immutable == cannot cahnge(tuple)
#tp = (1,)
#print(tp)
"""
a = 1
b = 8
a,b = b,a
print(a,b)
"""
#dictionary is nothing but key valuse pairs
d1 = {}
#print(type(d1))
d2 = {'tejas':'burger','rupesh':'fish','nilesh':'roti','rohan':{'b':'maggie','l':'roti','d':'chicken'}}
"""
print(d2)
d2['ankit'] = 'junkfood'
d2[420.666] = 'kababs'
print(d2)
del d2[420.666]
print(d2)
#print(d2['rohan']['l'])

#d3 = d2
#d3 = d2.copy()
#del d3['tejas']
print(d2.get('tejas'))
d2.update({'rishika':'star'})
print(d2.keys())
print(d2.items())
#print(d3)
"""
#### apni dictionary

dictionary = {"python":"its a programming language","float":"its data type","mutable":"can be change","immutable":"cannot be change"}
number = int(input())
number2 = int(input())
number3 = number + number2
print(number3)

