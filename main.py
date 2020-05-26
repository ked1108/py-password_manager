from os import system, name
import sqlite3 as sql
import hashlib
import manage as m


conn = sql.connect("database.db")
c = conn.cursor()

def clearscreen():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def login():
    state = True
    while state:
        clearscreen()
        user = input("Enter The User Name:\t")
        password = str(input("Enter The Password:\t"))
        hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
        c.execute("SELECT password FROM Users WHERE user = ? " , (user,))
        # c.execute("SELECT * FROM Users")
        data = c.fetchone()

        for row in data:
            if hashed in row:
                menu(user)
                state = False
                break

            if row[0] == None:
                choice = str(input("Incorrect User Name\nWant To Create A New User?(Y/n)"))
                if choice == "n":
                    continue
                else:
                    create()


def create():
    clearscreen()
    user = str(input("Enter The User Name:\t"))
    password = str(input("Enter The Password:\t"))

    hashed = hashlib.sha256(password.encode('utf-8')).hexdigest()
    c.execute("""INSERT INTO Users(user, password) VALUES(?, ?)""", (user, hashed))
    c.execute("CREATE TABLE IF NOT EXISTS %s (account TEXT, password TEXT)" % (user,))
    conn.commit()
    login()


def menu(user):
    while True:
        clearscreen()
        print("******************")
        print("Welcome ", user)
        print("n: New Account and Password")
        print("v: View A Password")
        print("u: Update A Password")
        print("d: Delete A Password")
        print("q: Exit The Program")
        print("******************")

        print("\n\n\n\n")

        choice = input("Enter Your Choice:\t")

        if choice == "n":
            m.new_pass(user)
        elif choice == "v":
            m.view_pass(user)
        elif choice == "u":
            m.update_pass(user)
        elif choice == "d":
            m.delete_pass(user)
        elif choice == "q":
            exit()
        else:
            continue

if __name__ == '__main__':
    c.execute(""" CREATE TABLE IF NOT EXISTS Users(user TEXT , password TEXT) """)
    conn.commit()
    while True:
        clearscreen()
        print("******************")
        print("1.) Create New Safe")
        print("2.) Login Into Your Safe")
        print("******************")
        print("\n\n\n")
        choice = int(input("Choose:\t"))
        if choice == 1:
            create()
            break
        elif choice == 2:
            login()
            break
        else:
            continue

