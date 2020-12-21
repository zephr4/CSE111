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

# def dropAllViews(_conn):
#     print("++++++++++++++++++++++++++++++++++")
#     print("Drop all Views")

#     try:
#         sql1 = """drop view V1"""
#         cur = _conn.cursor()
#         cur.execute(sql1)

#         sql2 = """drop view V2"""
#         cur = _conn.cursor()
#         cur.execute(sql2)

#         sql5 = """drop view V5"""
#         cur = _conn.cursor()
#         cur.execute(sql5)

#         sql10 = """drop view V10"""
#         cur = _conn.cursor()
#         cur.execute(sql10)
        
#         sql151 = """drop view V151"""
#         cur = _conn.cursor()
#         cur.execute(sql151)
        
#         sql152 = """drop view V152"""
#         cur = _conn.cursor()
#         cur.execute(sql152)

#         _conn.commit()
#         print("success")

#     print("++++++++++++++++++++++++++++++++++")

def create_View1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V1")
    
    try:
        sql = """CREATE VIEW V1 AS
                    select c_custkey, c_name, c_address, c_phone, c_acctbal, c_mktsegment, c_comment, n_name, r_name 
                    from customer, nation, region
                    where c_nationkey = n_nationkey AND 
                            n_regionkey = r_regionkey"""

        cur = _conn.cursor()
        cur.execute(sql)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V2")


    try:
        sql = """CREATE VIEW V2 AS
                    select s_suppkey, s_name, s_address, s_phone, s_acctbal, s_comment, n_name, r_name
                    from supplier, nation, region
                    where s_nationkey = n_nationkey AND 
                            n_regionkey = r_regionkey"""

        cur = _conn.cursor()
        cur.execute(sql)

        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V5")

    try:
        sql = """CREATE VIEW V5 AS
                    select o_orderkey, o_custkey, o_orderstatus, o_totalprice, strftime('%Y', o_orderdate) as o_orderyear, o_orderpriority, o_clerk, o_shippriority, o_comment 
                    from orders"""

        cur = _conn.cursor()
        cur.execute(sql)
        
        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def create_View10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V10")

    try:
        sql = """CREATE VIEW V10 AS
                    select p_type, avg(l_discount) as avg_discount
                    from part, lineitem
                    where p_partkey = l_partkey
                    group by p_type"""

        cur = _conn.cursor()
        cur.execute(sql)
        
        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def create_View151(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V151")

    try:
        sql = """CREATE VIEW V151 AS
                    select c_custkey, c_name, c_nationkey, c_acctbal 
                    from customer
                    where c_acctbal < 0"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        
        _conn.commit()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_View152(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create V152")

    try:
        view = """CREATE VIEW V152 AS
                    select s_suppkey, s_name, s_nationkey, s_acctbal 
                    from supplier
                    where s_acctbal < 0"""

        cur = _conn.cursor()
        cur.execute(view)
        
        _conn.commit()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    try:
        sql = """select c_name, round(sum(o_totalprice), 2) 
                    from V1, orders
                    where c_custkey = o_custkey AND 
                        strftime('%Y', o_orderdate) = '1996' AND 
                        n_name = 'RUSSIA' 
                    group by c_name"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/1.out', 'w')

        for x in result:
            l = '{:<18}|{:<10}'.format(x[0],x[1])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    try:
        sql = """select n_name, count(*) 
                    from V2
                    group by n_name"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/2.out', 'w')

        for x in result:
            l = '{:<1}|{:<10}'.format(x[0],x[1])
            print(l, file = output)

        output.close()
        print("success")
        
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    try:
        sql = """select n_name, count(o_custkey) 
                    from V1, orders
                    where c_custkey = o_custkey AND 
                            r_name = 'ASIA'
                    group by n_name"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/3.out', 'w')

        for x in result:
            l = '{:<1}|{:<10}'.format(x[0],x[1])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    try:
        sql = """select s_name as Supplier, count(p_partkey) as numParts
                    from V2, partsupp, part
                    where s_suppkey = ps_suppkey AND
                            ps_partkey = p_partkey AND
                            n_name = 'CHINA' AND
                            p_size < 30
                    group by Supplier"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/4.out', 'w')

        for x in result:
            l = '{:<1}|{:<10}'.format(x[0],x[1])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    try:
        sql = """select count(o_orderkey)
                    from V1, V5
                    where c_custkey = o_custkey AND
                            n_name = 'PERU' AND
                            o_orderyear = '1996'"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/5.out', 'w')

        for x in result:
            l = '{:<1}'.format(x[0])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    try:
        sql = """select s_name, o_orderpriority, count(*) 
                    from supplier, V5, nation, lineitem
                    where n_nationkey = s_nationkey AND 
                        n_regionkey = 1 AND 
                        l_orderkey = o_orderkey AND 
                        l_suppkey = s_suppkey
                    group by s_name, o_orderpriority"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/6.out', 'w')

        for x in result:
            l = '{:<1}|{:<1}|{:<1}'.format(x[0],x[1],x[2])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")

    try:
        sql = """select n_name, o_orderstatus, count(*) 
                    from V1, V5
                    where c_custkey = o_custkey AND 
                            r_name = 'EUROPE'
                    group by n_name, o_orderstatus"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/7.out', 'w')

        for x in result:
            l = '{:<1}|{:<1}|{:<1}'.format(x[0],x[1],x[2])
            print(l, file = output)
        
        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q8")
    
    try:
        sql = """select n_name, count(distinct o_orderkey) 
                    from V2, V5, lineitem
                    where o_orderyear = '1994' AND 
                        o_orderstatus = 'F' AND 
                        o_orderkey = l_orderkey AND 
                        l_suppkey = s_suppkey
                    group by n_name
                    having count(distinct o_orderkey) > 300"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/8.out', 'w')

        for x in result:
            l = '{:<1}|{:<1}'.format(x[0],x[1])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")
    
    try:
        sql = """select count(distinct o_clerk) 
                    from V2, V5, lineitem
                    where o_orderkey = l_orderkey AND 
                        l_suppkey = s_suppkey AND 
                        n_name = 'CANADA'"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/9.out', 'w')

        for x in result:
            l = '{:<1}'.format(x[0])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")

    try:
        sql = """select p_type, round(avg_discount, 16) 
                    from V10
                    where substr(p_type, 1, 5) = 'PROMO'
                    group by p_type"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/10.out', 'w')

        for x in result:
            l = '{:<1}|{:<1}'.format(x[0],x[1])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")

    try:
        sql = """select n_name, s_name, max(s_acctbal) 
                    from V2
                    group by n_name"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/11.out', 'w')

        for x in result:
            l = '{:<1}|{:<1}|{:<1}'.format(x[0],x[1],x[2])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")

    try:
        sql = """select n_name, round(avg(s_acctbal), 11) 
                    from V2
                    group by n_name"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/12.out', 'w')

        for x in result:
            l = '{:<1}|{:<1}'.format(x[0],x[1])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")

    try:
        sql = """select count(*) 
                    from V1, lineitem, orders
                    where o_orderkey = l_orderkey AND 
                        o_custkey = c_custkey AND 
                        l_suppkey IN (select s_suppkey 
                                        from V2
                                        where r_name = 'ASIA') AND 
                        c_custkey IN (select c_custkey 
                                        from V1
                                        where n_name = 'ARGENTINA')"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/13.out', 'w')

        for x in result:
            l = '{:<1}'.format(x[0])
            print(l, file = output)

        output.close()
        print("success")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")

    try:
        sql = """select region1, region2, count(o_orderkey) as TotalPrice
                    from (select *, r_name as region1
                            from V151, V152, region
                            where o_custkey = c_custkey AND
                                    c_nationkey = n_nationkey AND
                                    n_regionkey = r_regionkey),
                         (select *, r_name as region2
                            from V151, V152, region
                            where s_suppkey = l_suppkey AND
                                    s_nationkey = n_nationkey AND
                                    n_regionkey = r_regionkey)"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/14.out', 'w')

        for x in result:
            l = '{:<1}|{:<1}|{:<1}'.format(x[0],x[1],x[2])
            print(l, file = output)
        output.close()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")

    try:
        sql = """select count(distinct o_orderkey) 
                    from orders, lineitem
                    where o_orderkey = l_orderkey AND 
                            o_custkey IN (select c_custkey 
                                            from V151) AND 
                            l_suppkey IN (select s_suppkey 
                                            from V152)"""

        cur = _conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        output = open('output/15.out', 'w')

        for x in result:
            l = '{:<1}'.format(x[0])
            print(l, file = output)
        output.close()
        print("success")
    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"data/tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        # dropAllViews(conn)

        create_View1(conn)
        Q1(conn)

        create_View2(conn)
        Q2(conn)

        Q3(conn)
        Q4(conn)

        create_View5(conn)
        Q5(conn)

        Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)

        create_View10(conn)
        Q10(conn)

        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)

        create_View151(conn)
        create_View152(conn)
        Q15(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
