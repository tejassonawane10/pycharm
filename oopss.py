# Tejas, shravani and saksh, vaibhavi
#Dictionary
class Library:
    def __init__(self, list, name):
        self.booklist = list
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have following books in our Library: {self.name}")
        for book in self.booklist:
            print(book)
    def lendBooks(self, user, book):
        if Book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            print("Book has Dictionry has been updated. you can take book know ")
        else:
            print(f"book is already been used by {self.lendDict[book]}")
    def addBooks(self, book):
        self.booklist.append(book)
        print("book has been added to book list")
    def returnBook(self):
        self.booklist.remove(book)
if __name__ == '__main__':
    harry = Library(['python', 'Rich daddy poor daddy', 'harry potter', 'c++ basics', 'algorithms by clrs'], 'codewithharry')
    while(True):
        print("Welcome to the {harry.name} library. Enter your choice to continue")
        print("1. Display books")
        print("2. lend a  books")
        print("3. add a  books")
        print("4. return a  books")
        user_choice = int(input())
        if user_choice == 1:
            harry.displayBooks()
        elif user_choice == 2:
            Book = input('enter the name of the book you want to lend:')
            user = input("enter your name")
            harry.lendBooks(user, Book)
        elif user_choice == 3:
            book = input('enter the name of the book you want to add:')
            harry.addBooks(book)
        elif user_choice == 4:
            book = input('enter the name of the book you want to return:')
            harry.returnBook(book)
        else:
         print("not a valid option")

        print("Press q to quit and c to continue")
        user_choice2 = ''
        while(user_choice2!= 'c' and user_choice2!= 'q'):
            user_choice2 = input()
        if user_choice2 == 'q':
            exit()

        elif user_choice == 'c':
            continue

















































