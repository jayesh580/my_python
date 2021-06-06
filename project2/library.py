class Library:
    def __init__(self, bookList):
        self.bookList = bookList

    def displayAvailableBooks(self):
        print("Books Present in this Library are :")
        for book in self.bookList:
            print("*  "+book)

    def saveFile(self):
        with open("D:\python\project2\data.txt", 'w') as f:
            for book in self.bookList:
                f.write(book+"\n")        

    def borrowBook(self, bookName):
        if bookName in self.bookList:
            print(f"You have borrow {bookName}. Please keep it clean and safe, and also return this book within 30 days")
            self.bookList.remove(bookName)
            return True
        else :
             print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
             return False

    def returnBook(self, bookName):
        self.bookList.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")


class Student:
    def requestBook(self):
        self.book = input("Enter the name of the book which you want to borrow : ")
        return self.book 

    def returnBook(self):
        self.book = input("Enter the name of the book which you want to return : ")
        return self.book 
        
if __name__ == "__main__":
    with open("D:\python\project2\data.txt", 'r') as f:
        a = f.readlines()
        li = [x.strip() for x in a]
    centraLibrary = Library(li)
    student = Student()
    while(True):
        welcomeMsg = '''\n ====== Welcome to CSMIT Library ======
        Please Chose an option : 
        1. Show all books which are available
        2. Borrow a book from Library
        3. Add/Return a Book
        4. save
        5. Exit
        '''
        print(welcomeMsg)
        a = int(input("Enter your choice : "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            centraLibrary.saveFile()
        elif a == 5:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()