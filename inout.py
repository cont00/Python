import pickle
import os

path = "C:\\Temp\\"

def data_Load():
    ex1 = os.path.exists(path + 'book.txt')
    if ex1 == False:
        print("저장된 book list가 없습니다.")
    ex2 = os.path.exists(path + 'Library.txt')
    if ex2 == False:
        print("저장된 Library list가 없습니다.")

    f = open(path + 'book.txt', 'rb')
    data2 = pickle.load(f)
    f.close()
    bookList = data2

    f = open(path + 'Library.txt', 'rb')
    data3 = pickle.load(f)
    f.close()
    library_records = data3


def book_In(book_Date, book_Title, writer, pubilsher, genre, state):
    ex = os.path.exists(path + 'book.txt')
    if ex == False:
        f = open(path + 'book.txt', 'wb')
        data = []
        data.append([book_Date, book_Title, writer, pubilsher, genre, state])
        pickle.dump(data , f)
        f.close()
        bookList = data
    else:
        f = open(path + 'book.txt', 'wb')
        pickle.dump(bookList , f)
        f.close()
        #print(data2)
#book_Insert('book_Date', 'book_Title', 'writer', 'pubilsher', 'genre', 'state')

def Library_In(borrow_date , member_name , member_phone , status):
    #library_records = []
    ex = os.path.exists(path + 'Library.txt')
    if ex == False:
        f = open(path + 'Library.txt', 'wb')
        data = []
        data.append([borrow_date , member_name , member_phone , status])
        pickle.dump(data , f)
        f.close()
        library_records = data
    else:
        f = open(path + 'Library.txt', 'wb')
        pickle.dump(library_records , f)
        f.close()
        #print(data3)
#Library_In('borrow_date' , 'member_name' , 'member_phone' , 'status')