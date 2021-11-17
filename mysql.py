
import sqlite3

dbName = 'DGS_storage.db'


def insertCustomer(fName, lName, email, phone, address, state, city, zipcode):
    con = sqlite3.connect(dbName)

    query = '''
        INSERT INTO Customers
            (fName, lName, email, phone, address, state, city, zipcode)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    con.execute(query, (fName, lName, email, phone, address, state, city, zipcode))

    con.commit()
    con.close()


def getCustomer(cID):
    cur = sqlite3.connect(dbName).cursor()

    c = cur.execute('SELECT * FROM Customers WHERE cID = ?', (cID,))

    return c.fetchall()[0]


def updateCustomer(cID, fName, lName, email, phone, address, state, city, zipcode):
    con = sqlite3.connect(dbName)

    query = '''
        UPDATE Customers
        SET fName = ?, lName = ?, email = ?, phone = ?, address = ?, state = ?, city = ?, zipcode = ?
        WHERE cID = ?'''
    con.execute(query, (fName, lName, email, phone, address, state, city, zipcode, cID))

    con.commit()
    con.close()


def deleteCustomer(cID):
    con = sqlite3.connect(dbName)

    con.execute('DELETE FROM Customers WHERE cID = ?', (cID,))

    con.commit()
    con.close()


def insertProduct(title, minGrade, maxGrade, price):
    con = sqlite3.connect(dbName)

    query = '''
        INSERT INTO Products
            (title, minGrade, maxGrade, price)
            VALUES (?, ?, ?, ?)'''
    con.execute(query, (title, minGrade, maxGrade, price))

    con.commit()
    con.close()


def getProduct(pID):
    cur = sqlite3.connect(dbName).cursor()

    c = cur.execute('SELECT * FROM Products WHERE pID = ?', (pID,))

    return c.fetchall()[0]


def updateProduct(pID, title, minGrade, maxGrade, price):
    con = sqlite3.connect(dbName)

    query = '''
        UPDATE Products
        SET title = ?, minGrade = ?, maxGrade = ?, price = ?
        WHERE pID = ?'''
    con.execute(query, (title, minGrade, maxGrade, price, pID))

    con.commit()
    con.close()


def deleteProduct(pID):
    con = sqlite3.connect(dbName)

    con.execute('DELETE FROM Products WHERE pID = ?', (pID,))

    con.commit()
    con.close()


def insertSale(pID, cID, date, price):
    con = sqlite3.connect(dbName)

    query = '''
        INSERT INTO Sales
            (pID, cID, date, price)
            VALUES (?, ?, ?, ?)'''
    con.execute(query, (pID, cID, date, price))

    con.commit()
    con.close()


def getSale(sID):
    cur = sqlite3.connect(dbName).cursor()

    c = cur.execute('SELECT * FROM Sales WHERE sID = ?', (sID,))

    return c.fetchall()[0]


def updateSale(sID, pID, cID, date, price):
    con = sqlite3.connect(dbName)

    query = '''
        UPDATE Sales
        SET pID = ?, cID = ?, date = ?, price = ?
        WHERE sID = ?'''
    con.execute(query, (pID, cID, date, price, sID))

    con.commit()
    con.close()


def deleteSale(sID):
    con = sqlite3.connect(dbName)

    con.execute('DELETE FROM Sales WHERE sID = ?', (sID,))

    con.commit()
    con.close()


def viewTable(table):
    cur = sqlite3.connect(dbName).cursor()

    view = cur.execute(f'SELECT * FROM {table}')

    return view.fetchall()


def getOptions(table):
    cur = sqlite3.connect(dbName).cursor()

    view = cur.execute(f'SELECT {table[0].lower()}ID FROM {table}')
    options = view.fetchall()
    
    return [v[0] for v in options]


con = sqlite3.connect(dbName)

con.execute('''
    CREATE TABLE IF NOT EXISTS Customers(
        cID integer not null primary key,
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
        pID integer not null primary key,
        title text,
        minGrade integer,
        maxGrade integer,
        price integer)''')
con.execute('''
    CREATE TABLE IF NOT EXISTS Sales(
        sID integer not null primary key,
        pID integer,
        cID integer,
        date text,
        price integer)''')

con.commit()
con.close()
