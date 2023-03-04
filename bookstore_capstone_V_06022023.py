import sqlite3


# create a database connection
db = sqlite3.connect('ebookstore_db')
cursor = db.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS books (i_d INTEGER PRIMARY KEY, title TEXT, author TEXT, qty INTEGER)''')
print('Table created')
db.commit()

# populate the bookstore to start with
bookstore_start = [
(3001,'A Tale of Two Cities','Charles Dickens',30),
(3002,"Harry Potter and the Philosopher's Stone",'J.K.Rowling',40),
(3003,'The Lion, the Witch and the Wardrobe','C.S.Lewis',25),
(3004,'The Lord of the Rings','J.R.R Tolkien',37),
(3005,'Alice in Wonderland','Lewis Carroll',12),
(3006,'Tintin in America', 'Herge', 5000),
(3007,'Tintin and the Picaros', 'Herge', 5000),
(3008,'Tintin and the Blue Lotus', 'Herge', 5000),
(3009,'The Calculus Affair','Herge', 5000),
(3010,'Explorers on the Moon','Herge', 5000)
]
cursor.executemany(''' INSERT INTO books(i_d,title,author,qty)VALUES(?,?,?,?)''',bookstore_start)
print('Bookstore set-up complete')
db.commit()


def enter_book_to_db():
    '''Add a book to the database'''
    i_d = int(input("Enter the ID of the book you want to add: ")) # check if the ID is valid and not in the database already
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    qty = int(input("Enter the quantity of the book: "))
    cursor.execute('''INSERT INTO books VALUES(?,?,?,?)''', (i_d, title, author, qty))
    print('Record inserted')
    db.commit()
    main()


def update_book_in_db():
    '''Update a book in the database'''
    cursor.execute('''SELECT * FROM books''')
    data = cursor.fetchall()
    print(data)
    i_d = int(input("Enter the ID of the book you want to update: ")) # check if the ID is valid and not in the database already
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    qty = int(input("Enter the quantity of the book: "))
    cursor.execute('''UPDATE books SET title =?, author =?, qty =? WHERE i_d =?''', (title, author, qty, i_d))
    print('Record updated')
    db.commit()
    main()


def delete_book_in_db():
    '''Delete a book from the database'''
    cursor.execute('''SELECT * FROM books''')
    data = cursor.fetchall()
    print(data)
    i_d_check = int(input("Enter the ID of the book you want to delete: ")) # check if the ID is valid and not in the database already
    cursor.execute('''DELETE FROM books WHERE i_d =?''', (i_d_check,))
    print('Record deleted')
    db.commit()
    main()


def search_book_in_db():
    '''A basic search function for the user, which assumes that the user has entered a valid ID and knows the book ID'''
    i_d_check = int(input("Enter the number of the book you want to view: "))
    db = sqlite3.connect('ebookstore_db')
    cursor = db.cursor()
    cursor.execute('''SELECT * FROM books WHERE i_d =?''', (i_d_check,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db.close()
    main()


def main():
    '''The main part of the program which provides a basic menu to the user'''
    while True:
        choice = int(input('''
        Please choose one of the following options:

        1. Add a book
        2. Update a book
        3. Delete a book
        4. Search a book
        0. Exit
        _________ : '''))
        if choice == 1:
            return enter_book_to_db()
        elif choice == 2:
            update_book_in_db()
        elif choice == 3:
            delete_book_in_db()
        elif choice == 4:
            search_book_in_db()
        elif choice == 0:
            exit()
        else:
            print("Invalid choice")
            continue


# calls the main function
main()