import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("SUCCESS")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("SUCCESS")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def dropTablesandViews(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("DROP TABLES AND VIEWS")

    try:
        sql = "DROP TABLE IF EXISTS Distributor;"
        _conn.execute(sql)

        sql = "DROP TABLE IF EXISTS Product;"
        _conn.execute(sql)

        sql = "DROP TABLE IF EXISTS Price_Cube;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS Q1;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS Q2;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS Q3;"
        _conn.execute(sql)

        sql = "DROP VIEW IF EXISTS Q4;"
        _conn.execute(sql)
        
        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createPrice_Cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("CREATE PRICE_CUBE")

    try:
        sql = """CREATE TABLE IF NOT EXISTS Price_Cube (
                    distributor_type VARCHAR(11) CHECK(distributor_type IN ('Producer', 'Distributor', '*')),
                    product_type VARCHAR(7) CHECK(product_type IN ('pc', 'laptop', 'printer', '*')),
                    num_prod INTEGER,
                    tot_price INTEGER);"""

        _conn.execute(sql)

        _conn.commit()
        print("SUCCESS")    
        
    except Error as e:        
        _conn.rollback()        
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def dropPrice_Cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("DROP PRICE_CUBE")

    try:
        sql = "DROP TABLE IF EXISTS Price_Cube;"
        _conn.execute(sql)

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_tables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("CREATE TABLES")

    try:
        sql = """CREATE TABLE IF NOT EXISTS Product (
                    model INTEGER PRIMARY KEY,
                    type VARCHAR(7),
                    maker VARCHAR(2));"""
        
        _conn.execute(sql)

        sql = """CREATE TABLE IF NOT EXISTS Distributor (
                    model INTEGER,
                    name VARCHAR(2),
                    price INTEGER DEFAULT('NULL'),
                    FOREIGN KEY(model) REFERENCES Product(model) ON UPDATE CASCADE);"""

        _conn.execute(sql)
  
        sql = """CREATE TABLE IF NOT EXISTS Price_Cube (
                    distributor_type VARCHAR(11) CHECK(distributor_type IN ('Producer', 'Distributor', '*')),
                    product_type VARCHAR(7) CHECK(product_type IN ('pc', 'laptop', 'printer', '*')),
                    num_prod INTEGER,
                    tot_price INTEGER);"""

        _conn.execute(sql)

        sql = """CREATE VIEW IF NOT EXISTS Q1 AS
                    SELECT 'Producer' as distributor_type, Product.type as product_type, 
                            count(Distributor.name) as num_prod, sum(Distributor.price) as tot_price
                    FROM Product, Distributor
                    WHERE Product.model = Distributor.model AND
                            Product.maker = Distributor.name
                    GROUP BY distributor_type, product_type
                    UNION
                    SELECT 'Distributor' as distributor_type, Product.type as product_type, 
                            count(Distributor.name) as num_prod, sum(Distributor.price) as tot_price
                    FROM Product, Distributor
                    WHERE Product.model = Distributor.model AND
                            Distributor.name LIKE 'D%'
                    GROUP BY distributor_type, product_type;"""

        _conn.execute(sql)

        sql = """CREATE VIEW IF NOT EXISTS Q2 AS
                    SELECT '*' as distributor_type, Product.type as product_type, 
                            count(Distributor.name) as num_prod, sum(Distributor.price) as tot_price
                    FROM Product, Distributor
                    WHERE Product.model = Distributor.model AND
                            Product.maker = Distributor.name OR
                            Distributor.name LIKE 'D%'
                    GROUP BY product_type;"""

        _conn.execute(sql)

        sql = """CREATE VIEW IF NOT EXISTS Q3 AS
                    SELECT 'Distributor' as distributor_type, '*' as product_type, 
                            count(Distributor.name) as num_prod, sum(Distributor.price) as tot_price
                    FROM Product, Distributor
                    WHERE Product.model = Distributor.model AND
                            Distributor.name LIKE 'D%'
                    GROUP BY distributor_type
                    UNION
                    SELECT 'Producer' as distributor_type, '*' as product_type, 
                            count(Distributor.name) as num_prod, sum(Distributor.price) as tot_price
                    FROM Product, Distributor
                    WHERE Product.model = Distributor.model AND
                            Product.maker = Distributor.name
                    GROUP BY distributor_type;"""

        _conn.execute(sql)

        sql = """CREATE VIEW IF NOT EXISTS Q4 AS
                    SELECT '*' as distributor_type, '*' as product_type, 
                            count(Distributor.name) as num_prod, sum(Distributor.price) as tot_price
                    FROM Product, Distributor
                    WHERE Product.model = Distributor.model AND
                            Product.maker = Distributor.name OR
                            Distributor.name LIKE 'D%';"""

        _conn.execute(sql)

        _conn.commit()
        print("SUCCESS")    
        
    except Error as e:        
        _conn.rollback()        
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populate_tables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("POPULATE TABLES")

    try:
        file = open('product.txt', 'r')
        lines = file.readlines()
       
        for line in lines:
            tok = line.strip().split('|')
            sql = """INSERT INTO Product(model, type, maker) 
                        VALUES(?, ?, ?);"""
            args = [tok[0], tok[1], tok[2]]
            _conn.execute(sql, args)
            _conn.commit()

        file = open('distributor.txt', 'r')
        lines = file.readlines()
       
        for line in lines:
            tok = line.strip().split('|')
            sql = """INSERT INTO Distributor(model, name, price) 
                        VALUES(?, ?, ?);"""
            args = [tok[0], tok[1], tok[2]]
            _conn.execute(sql, args)
            _conn.commit()

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def build_data_cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("BUILD DATA CUBE")

    try:
        sql = """INSERT INTO Price_Cube
                    SELECT *
                    FROM Q1
                    UNION
                    SELECT *
                    FROM Q2
                    UNION 
                    SELECT *
                    FROM Q3
                    UNION
                    SELECT *
                    FROM Q4;"""
        
        _conn.execute(sql)
        _conn.commit()

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)



    print("++++++++++++++++++++++++++++++++++")


def print_Product(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT PRODUCT")

    try:
        sql = """SELECT *
                    FROM Product
                    ORDER BY model asc;"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:<20} {:<20} {:<20}'.format("model", "type", "maker")
        print('------------------------------------------------')
        print(l)
        print('------------------------------------------------')

        rows = cur.fetchall()
        for row in rows:
            l = '{:<20} {:<20} {:<20}'.format(row[0], row[1], row[2])
            print(l)

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def print_Distributor(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DISTRIBUTOR")

    try:
        sql = """SELECT *
                    FROM Distributor
                    ORDER BY model asc;"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:<20} {:<5} {:>20}'.format("model", "name", "price")
        print('------------------------------------------------')
        print(l)
        print('------------------------------------------------')

        rows = cur.fetchall()
        for row in rows:
            l = '{:<20} {:<20} {:<20}'.format(row[0], row[1], row[2])
            print(l)

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def printD(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT ALL D%")

    try:
        sql = """SELECT Distributor.name as distributor_type
                    FROM Distributor
                    WHERE Distributor.name LIKE 'D%';"""

        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:<20}'.format("name")
        print('------------------------------------------------')
        print(l)
        print('------------------------------------------------')

        rows = cur.fetchall()
        for row in rows:
            l = '{:<20}'.format(row[0])
            print(l)

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

def print_Cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DATA CUBE")

    try:
        sql = """SELECT *
                    FROM Price_Cube;"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        l = '{:<20} {:<20} {:>10} {:>10}'.format("dist", "prod", "cnt", "total")
        print('----------------------------------------------------------------')
        print(l)
        print('----------------------------------------------------------------')

        rows = cur.fetchall()
        for row in rows:
            l = '{:<20} {:<20} {:>10} {:>10}'.format(row[0], row[1], row[2], row[3])
            print(l)

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)


    print("++++++++++++++++++++++++++++++++++")


def modifications(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("MODIFICATIONS")

    file = open('modifications.txt', 'r')
    lines = file.readlines()
    for line in lines:
        tok = line.strip().split(' ')

        print("-------------------------------------------------")
        if (tok[0] == 'Product') and (tok[1] == 'I'):
            try:
                print("INSERT INTO PRODUCT: {0}, {1}, {2}".format(tok[2], tok[3], tok[4]))

                sql = """INSERT INTO Product(model, type, maker) 
                            VALUES(?, ?, ?);"""
                args = [tok[2], tok[3], tok[4]]

                _conn.execute(sql, args)

                sql = """INSERT INTO Distributor(model, name, price) 
                            VALUES(?, ?, ?);"""
                args = [tok[2], tok[3], 0]

                _conn.execute(sql, args)
                print("SUCCESS")
                print("-------------------------------------------------")
            except Error as e:        
                _conn.rollback()        
                print(e)

        elif (tok[0] == 'Product') and (tok[1] == 'D'):
            try:
                print("DELETE FROM PRODUCT: {0}".format(tok[2]))

                # When we delete from the parent table we also have to first delete the reference pointer in the child table.
                #   In this case, we have to delete the child table row where Distributor.model = tok[2].
                sql = """DELETE FROM Distributor
                            WHERE model = (?)"""
                args = [tok[2]]

                _conn.execute(sql, args)
                        
                sql = """DELETE FROM Product
                            WHERE model = (?);"""
                args = [tok[2]]

                _conn.execute(sql, args)
                print("SUCCESS")
                print("-------------------------------------------------")
            except Error as e:        
                _conn.rollback()        
                print(e)

        elif (tok[0] == 'Distributor') and (tok[1] == 'I'):
            try:
                print("INSERT INTO Distributor: {0}, {1}, {2}".format(tok[2], tok[3], tok[4]))

                # Update because of assignment requirements that are given
                sql = """UPDATE Distributor
                            SET price = (?),
                                 name = (?)
                            WHERE model = (?);"""
                args = [tok[4], tok[3], tok[2]]

                _conn.execute(sql, args)
                print("SUCCESS") 
                print("-------------------------------------------------") 
            except Error as e:        
                _conn.rollback()        
                print(e)

        elif (tok[0] == 'Distributor') and (tok[1] == 'D'):
            try:
                print("DELETE FROM Distributor: {0}, {1}".format(tok[2], tok[3]))

                # Update because of assignment requirements that are given
                sql = """UPDATE Distributor
                            SET price = 'NULL'
                            WHERE model = (?) AND
                                    name = (?);"""
                args = [tok[2], tok[3]]

                _conn.execute(sql, args)
                print("SUCCESS")
                print("-------------------------------------------------")
            except Error as e:        
                _conn.rollback()        
                print(e)

        _conn.commit()

    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    # Why is my foreign_keys not working????
    conn.execute("PRAGMA foreign_keys = 1")
    with conn:
        dropTablesandViews(conn)
        create_tables(conn)

        populate_tables(conn)

        print_Product(conn)
        print_Distributor(conn)
        # printD(conn)

        build_data_cube(conn)
        print_Cube(conn)
        
        modifications(conn)

        print_Product(conn)
        print_Distributor(conn)
        
        dropPrice_Cube(conn)
        createPrice_Cube(conn)
        build_data_cube(conn)
        print_Cube(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()