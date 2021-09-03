# Joe Olpin
# Accounts Receivable
# 9/2-3/2021

import sqlite3

dbName = 'DGS_storage.db'


def insertCustomer(cID, fName, lName, email, phone, address, state, city, zipcode):
    con = sqlite3.connect(dbName)

    iquery = f'''
        INSERT INTO Customers
            (cID, fName, lName, email, phone, address, state, city, zipcode)
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    con.execute(iquery, (cID, fName, lName, email, phone, address, state, city, zipcode))

    con.commit()
    con.close()


def insertProduct(pID, title, minGrade, maxGrade, price):
    con = sqlite3.connect(dbName)

    iquery = f'''
        INSERT INTO Products
            (pID, title, minGrade, maxGrade, price)
            VALUES
            (?, ?, ?, ?, ?)'''
    con.execute(iquery, (pID, title, minGrade, maxGrade, price))

    con.commit()
    con.close()


def insertSale(pID, cID, date, price):
    con = sqlite3.connect(dbName)

    iquery = f'''
        INSERT INTO Sales
            (pID, cID, date, price)
            VALUES
            (?, ?, ?, ?)'''
    con.execute(iquery, (pID, cID, date, price))

    con.commit()
    con.close()


def getCustomer(cID):
    cur = sqlite3.connect(dbName).cursor()

    c = cur.execute(f'SELECT * FROM Customers WHERE cID={cID}')

    return c.fetchall()


def viewTable(table):
    cur = sqlite3.connect(dbName).cursor()

    view = cur.execute(f'SELECT * FROM {table}')

    return view.fetchall()


def edit():
    pass


con = sqlite3.connect(dbName)

con.execute('''
    CREATE TABLE IF NOT EXISTS Customers(
        cID integer,
        fName text,
        lName text,
        email text,
        phone text,
        address text,
        state text,
        city text,
        zipcode integer)''')
con.execute('''
    CREATE TABLE IF NOT EXISTS Products(
        pID integer,
        title text,
        minGrade integer,
        maxGrade integer,
        price integer)''')
con.execute('''
    CREATE TABLE IF NOT EXISTS Sales(
        pID integer,
        cID integer,
        date text,
        price integer)''')

con.commit()
con.close()
