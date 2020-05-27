from os import system, name
import string
import sqlite3
import random
import re

conn = sqlite3.connect('database.db')
c = conn.cursor()

def clearscreen():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')

def pass_gen(size = 12, chars = string.ascii_letters + string.digits):
    clearscreen()
    return ''.join(random.choice(chars) for _ in range(size))

def check_input(input_val):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(input_val) == None:
        return True
    else:
        return False
def new_pass(user):
    clearscreen()
    account = str(input("Enter The Account Name:\t"))
    if check_input(account):
        size = 12
        try:
            size = int(input("Enter The Length Of The Password(default: 12):\t"))
        except ValueError:
            size = 12

        password = pass_gen(size)
        query = " INSERT INTO %s VALUES(?, ?) " % (user,)
        c.execute(query, (account, password))
        conn.commit()

    else:
        print("Error Parsing Input!")

    choice = str(input("Return Back To The Menu"))
    if choice == 'q':
        pass
    else:
        pass

def view_pass(user):
    clearscreen()
    account = str(input("Enter The Account Name:\t"))
    if check_input(account):
        query = "SELECT password FROM %s WHERE account = ? " % (user,)
        c.execute(query, (account,))
        password = c.fetchone()
        print(password[0])

    else:
        print("Error Parsing Input!")

    choice = str(input("Return Back To The Menu"))
    if choice == 'q':
        pass
    else:
        pass


def update_pass(user):
    clearscreen()
    account = str(input("Enter The Account Name:\t"))
    if check_input(account):
        size = 12
        try:
            size = int(input("Enter The Length Of The Password(default: 12):\t"))
        except ValueError:
            size = 12
        password = pass_gen(size)
        query = "UPDATE %s SET password = ? WHERE account = ?" % (user,)
        c.execute(query, (password, account,))
        conn.commit()
        print("Password Updated!")

    else:
        print("Error Parsing Input!")

    choice = str(input("Return Back To The Menu"))
    if choice == 'q':
        pass
    else:
        pass


def delete_pass(user):
    clearscreen()
    try:
        account = str(input("Enter The Account Name:\t"))
        if check_input(account):
            query = "DELETE FROM %s WHERE account = ?" % (user,)
            c.execute(query, (account,))
            conn.commit()
            print("Password Deleted!")

        else:
            print("Error Parsing Input!")

    except sqlite3.Error as error:
        print("Failed To Delete Query", error)

    choice = str(input("Return Back To The Menu"))
    if choice == 'q':
        pass
    else:
        pass
