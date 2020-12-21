import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

# def truncatePriceRange(_conn):    
#     print("++++++++++++++++++++++++++++++++++")    
#     print("Truncate PriceRange")    
    
#     try:        
#         sql = """TRUNCATE TABLE PriceRange"""        
#         _conn.execute(sql)
#         _conn.commit() 

#         print("success") 

#     except Error as e:        
#         _conn.rollback()       
#         print(e)    
        
#     print("++++++++++++++++++++++++++++++++++")

def dropPriceRange(_conn):    
    # print("++++++++++++++++++++++++++++++++++")    
    # print("Drop PriceRange")    
    
    try:        
        sql = """DROP TABLE PriceRange"""        
        _conn.execute(sql)
        _conn.commit() 

        # print("success") 

    except Error as e:        
        _conn.rollback()       
        # print(e)    
        
    # print("++++++++++++++++++++++++++++++++++")

def createPriceRange(_conn):    
    # print("++++++++++++++++++++++++++++++++++")    
    # print("Create Table PriceRange")    
    
    try:        
        sql = """CREATE TABLE PriceRange (
                maker VARCHAR(1),
                type VARCHAR(7),
                min INTEGER,
                max INTEGER)""" 

        _conn.execute(sql)
        _conn.commit() 

        # print("success") 

    except Error as e:        
        _conn.rollback()       
        # print(e)    
        
    # print("++++++++++++++++++++++++++++++++++")

def populatePriceRange(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate PriceRange")

    try:

        sql = """SELECT distinct pr1.maker, pr1.type, min(pc.price), max(pc.price)
                    from Product pr1, PC pc
                    where pr1.model = pc.model
                 group by pr1.maker
                 UNION
                 SELECT distinct pr2.maker, pr2.type, min(lt.price), max(lt.price)
                    from Product pr2, Laptop lt
                    where pr2.model = lt.model
                 group by pr2.maker
                 UNION
                 SELECT distinct pr3.maker, pr3.type, min(pt.price), max(pt.price)
                    from Product pr3, Printer pt
                    where pr3.model = pt.model
                 group by pr3.maker"""
        
        cur = _conn.cursor()
        cur = _conn.execute(sql)

        rows = cur.fetchall()
        for info in rows:
            sql = """INSERT INTO PriceRange(maker, type, min, max) 
                        VALUES(?, ?, ?, ?)"""
            args = [info[0], info[1], info[2], info[3]]        
            _conn.execute(sql, args)       
            _conn.commit()
            
        print("success")    
        
    except Error as e:        
        _conn.rollback()        
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def printPriceRange(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Print PriceRange\n")

    try:
        sql = """select *
                from PriceRange"""
        
        cur = _conn.cursor()        
        cur.execute(sql)

        l = '{:<10} {:<20} {:>20} {:>20}'.format("maker", "product", "minPrice", "maxPrice")
        print(l)
        print("-------------------------------------------------------------------------")        
        rows = cur.fetchall()        
        for row in rows:            
            l = '{:<10} {:<20} {:>20} {:>20}'.format(row[0], row[1], row[2], row[3])            
            print(l)

        print("\nsuccess")

    except Error as e:
        _conn.rollback             
        print(e)

    print("++++++++++++++++++++++++++++++++++")

# I added _type just to generalize it a bit more 
def insertPC(_conn, _type, _maker, _model, _speed, _ram, _hd, _price):
    print("++++++++++++++++++++++++++++++++++")

    try:
        sql = """INSERT INTO PC(model, speed, ram, hd, price)
                    VALUES(?, ?, ?, ?, ?)"""
        args = [_model, _speed, _ram, _hd, _price]

        _conn.execute(sql, args)
        _conn.commit()

        l = 'Insert PC ({}, {}, {}, {}, {})'.format(_maker, _model, _speed, _ram, _hd, _price)
        print(l)
        
        # Since we are adding entirely new models for the makers we add it to the Product table as well
        sql = """INSERT INTO Product(maker, model, type)
                    VALUES(?, ?, ?)"""
        args = [_maker, _model, _type]

        _conn.execute(sql, args)
        _conn.commit()

    except Error as e:        
        _conn.rollback()        
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def updatePrinter(_conn, _model, _price):
    print("++++++++++++++++++++++++++++++++++")

    try:
        sql = """UPDATE Printer
                    SET price = (?)
                    WHERE model = (?)"""
        args = [_price, _model]

        _conn.execute(sql, args)
        _conn.commit()

        l = 'Update Printer ({}, {})'.format(_model, _price)
        print(l)

    except Error as e:        
        _conn.rollback()        
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def deleteLaptop(_conn, _model):
    print("++++++++++++++++++++++++++++++++++")
    
    try:
        sql = """DELETE FROM Laptop 
                    WHERE model = (?)"""
        args = [_model]

        _conn.execute(sql, args)
        _conn.commit()

        l = 'Delete Laptop ({})'.format(_model)
        print(l)

        sql = """DELETE FROM Product 
                    WHERE model = (?)"""
        args = [_model]

        _conn.execute(sql, args)
        _conn.commit()

    except Error as e:        
        _conn.rollback()        
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropPriceRange(conn)
        createPriceRange(conn)
        populatePriceRange(conn)
        printPriceRange(conn)

        file = open('input.in', 'r')
        lines = file.readlines()
        for line in lines:
            print(line.strip())

            tok = line.strip().split(' ')
            if tok[0] == 'I':
                insertPC(conn, tok[1], tok[2], tok[3], tok[4], tok[5], tok[6], tok[7])
            elif tok[0] == 'U':
                updatePrinter(conn, tok[2], tok[3])
            elif tok[0] == 'D':
                deleteLaptop(conn, tok[2])

            dropPriceRange(conn)
            createPriceRange(conn)
            populatePriceRange(conn)
            printPriceRange(conn)

        file.close()

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
