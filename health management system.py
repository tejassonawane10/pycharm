"""
HEALTH MANAGEMENT SYSTEM
3 client harry rohan hammad
def getdate():
import daterime
return datetime.datetime.now()
total 6 files
write a functionthat when execute takes as input client name
one more function that to retrive exercize or food for any client
lock or retrive
name
excercize or diet

"""
import datetime
def gettime():
    return datetime.datetime.now()

def selectname():
    names = {1:"harry",2:"rohan",3:"hammad"}
    b = {1:"food", 2:"exercize"}
    for key, value in names.items():
        print("press", key, "for", value,"\n", end = "")
    n = int(input("...."))
    if n > 3:
        print("please select 1 or 2 or 3")
        exit()
    else:
        return n
def select_task():
    task = {1:"food",2:"exercize"}
    for keys, value in task.items():
        print("press",keys,"for",value,"\n",end="")
    y =  int(input("....."))
    if y > 2:
        print("please select 1 or 2")
        exit()
    else:
        return y
def select_file_action():
    action = {1:"store",2:"retrive"}
    for keys, value in action.items():
        print("press", keys, "for",value,"\n",end="")
    x = int(input("...."))
    if x > 2:
        print(" select 1 or 2")
        exit()
    else:
        return x

def action(n,x,y):
    if n == 1 and x==1 and y ==1:
        value = input("type here\n")
        with open("harry food.txt","a") as harryfood:
            harryfood.write((str([str(gettime)])) +":"+value+"\n")
            print("successfully written")
    elif n == 1 and x==1 and y ==2:
        value = input("type here\n")
        with open("harry exercize.txt","a") as harryexercize:
            harryexercize.write((str([str(gettime)])) +":"+value+"\n")
            print("successfully written")
    elif n == 2 and x==1 and y ==1:
        value = input("type here\n")
        with open("rohan food.txt","a") as rohanfood:
            rohanfood.write((str([str(gettime)])) +":"+value+"\n")
            print("successfully written")
    elif n == 2 and x==1 and y ==2:
        value = input("type here\n")
        with open("rohan exercize.txt","a") as rohanexercize:
            rohanexercize.write((str([str(gettime)])) +":"+value+"\n")
            print("successfully written")
    elif n == 3 and x==1 and y ==1:
        value = input("type here\n")
        with open("hammad food.txt","a") as hammadfood:
            hammadfood.write((str([str(gettime)])) +":"+value+"\n")
            print("successfully written")
    elif n == 3 and x==1 and y ==2:
        value = input("type here\n")
        with open("hammad exercize.txt","a") as hammadexercize:
            hammadexercize.write((str([str(gettime)])) +":"+value+"\n")
            print("successfully written")

    elif n ==1 and x ==2 and y ==1:
        with open("harry food.txt", "r")as harryfood:
            a = harryfood.read()
            print(a)

    elif n ==1 and x ==2 and y ==2:
        with open("harry exercize.txt", "r")as harryexercize:
            a = harryexercize.read()
            print(a)


    elif n == 2 and x == 2 and y == 1:
        with open("rohan food.txt", "r") as rohanfood:
            a = rohanfood.read()
            print(a)


    elif n ==2 and x ==2 and y == 2:
        with open("rohan exercize.txt", "r")as rohanexercize:
            a = rohanexercize.read()
            print(a)

    elif n ==3 and x ==2 and y ==1:
        with open("hammad food.txt", "r")as hammadfood:
            a = hammadfood.read()
            print(a)

    elif n ==3 and x ==2 and y ==2:
        with open("hammad exercize.txt", "r")as hammadexercize:
            a = hammadexercize.read()
            print(a)


n = selectname()
y = select_task
x = select_file_action()

action (n,y,x)
