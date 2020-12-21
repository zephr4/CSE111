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


def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create table")

    try:
        sql = """CREATE TABLE warehouse (
                w_warehousekey decimal(9,0) not null,
                w_name char(100) not null,
                w_capacity decimal(6,0) not null,
                w_suppkey decimal(9,0) not null,
                w_nationkey decimal(2,0) not null)"""
        _conn.execute(sql)

        _conn.commit()
        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e);

    print("++++++++++++++++++++++++++++++++++")


def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop tables")

    try:
        sql = "DROP TABLE warehouse"
        _conn.execute(sql)

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate table")

    try:
        warehouse = [
            (1,'Supplier#000000001___EGYPT', 2044, 1, 4),
            (2, 'Supplier#000000001___ROMANIA', 2044, 1, 9),
            (3, 'Supplier#000000002___VIETNAM', 1876, 2, 21),
            (4, 'Supplier#000000002___SAUDI ARABIA', 1876, 2, 20),
            (5, 'Supplier#000000003___ALGERIA', 2006, 3, 0),
            (6, 'Supplier#000000003___JAPAN', 2006, 3, 12),
            (7, 'Supplier#000000004___CANADA', 2246, 4, 3),
            (8, 'Supplier#000000004___IRAN', 2246, 4, 10),
            (9, 'Supplier#000000005___CANADA', 1730, 5, 3),
            (10, 'Supplier#000000005___EGYPT', 1730, 5, 4),
            (11, 'Supplier#000000006___IRAN', 1732, 6, 10),
            (12, 'Supplier#000000006___CANADA', 1732, 6, 3),
            (13, 'Supplier#000000007___CANADA', 1894, 7, 3),
            (14, 'Supplier#000000007___ROMANIA', 1894, 7, 19),
            (15, 'Supplier#000000008___CANADA', 2088, 8, 3),
            (16, 'Supplier#000000008___EGYPT', 2088, 8, 4),
            (17, 'Supplier#000000009___EGYPT', 1794, 9, 4),
            (18, 'Supplier#000000009___IRAQ', 1794, 9, 11),
            (19, 'Supplier#000000010___GERMANY', 1928, 10, 7),
            (20, 'Supplier#000000010___CANADA', 1928, 10, 3),
            (21, 'Supplier#000000011___EGYPT', 1840, 11, 4),
            (22, 'Supplier#000000011___ROMANIA', 1840, 11, 19),
            (23, 'Supplier#000000012___SAUDI ARABIA', 1618, 12, 20),
            (24, 'Supplier#000000012___INDONESIA', 1618, 12, 9),
            (25, 'Supplier#000000013___EGYPT', 1872, 13, 4),
            (26, 'Supplier#000000013___MOZAMBIQUE', 1872, 13, 16),
            (27, 'Supplier#000000014___CANADA', 2130, 14, 3),
            (28, 'Supplier#000000014___EGYPT', 2130, 14, 4),
            (29, 'Supplier#000000015___SAUDI ARABIA', 2256, 15, 20),
            (30, 'Supplier#000000015___EGYPT', 2256, 15, 4),
            (31, 'Supplier#000000016___SAUDI ARABIA', 1972, 16, 20),
            (32, 'Supplier#000000016___CANADA', 1972, 16, 3),
            (33, 'Supplier#000000017___INDONESIA', 1740, 17, 9),
            (34, 'Supplier#000000017___ROMANIA', 1740, 17, 19),
            (35, 'Supplier#000000018___ROMANIA', 2046, 18, 19),
            (36, 'Supplier#000000018___CANADA', 2046, 18, 3),
            (37, 'Supplier#000000019___ROMANIA', 2436, 19, 19),
            (38, 'Supplier#000000019___EGYPT', 2436, 19, 4),
            (39, 'Supplier#000000020___BRAZIL', 1908, 20, 2),
            (40, 'Supplier#000000020___UNITED STATES', 1908, 20, 24),
            (41, 'Supplier#000000021___CANADA', 1924, 21, 3),
            (42, 'Supplier#000000021___BRAZIL', 1924, 21, 2),
            (43, 'Supplier#000000022___KENYA', 2174, 22, 14),
            (44, 'Supplier#000000022___VIETNAM', 2174, 22, 21),
            (45, 'Supplier#000000023___EGYPT', 1726, 23, 4),
            (46, 'Supplier#000000023___IRAN', 1726, 23, 10),
            (47, 'Supplier#000000024___INDONESIA', 1788, 24, 9),
            (48, 'Supplier#000000024___ALGERIA', 1788, 24, 0),
            (49, 'Supplier#000000025___BRAZIL', 1882, 25, 2),
            (50, 'Supplier#000000025___ALGERIA', 1882, 25, 0),
            (51, 'Supplier#000000026___EGYPT', 1768, 26, 4),
            (52, 'Supplier#000000026___VIETNAM', 1768, 26,21),
            (53, 'Supplier#000000027___EGYPT', 1864, 27, 4),
            (54, 'Supplier#000000027___IRAN', 1864, 27,10),
            (55, 'Supplier#000000028___MOZAMBIQUE', 2274, 28,16),
            (56, 'Supplier#000000028___INDONESIA', 2274, 28, 9),
            (57, 'Supplier#000000029___JAPAN', 1538, 29,12),
            (58, 'Supplier#000000029___INDONESIA', 1538, 29, 9),
            (59, 'Supplier#000000030___CANADA', 2108, 30, 3),
            (60, 'Supplier#000000030___IRAN', 2108, 30,10),
            (61, 'Supplier#000000031___ALGERIA', 1600, 31, 0),
            (62, 'Supplier#000000031___IRAN', 1600, 31,10),
            (63, 'Supplier#000000032___CANADA', 1942, 32, 3),
            (64, 'Supplier#000000032___INDIA', 1942, 32, 8),
            (65, 'Supplier#000000033___EGYPT', 1578, 33, 4),
            (66, 'Supplier#000000033___JAPAN', 1578, 33,12),
            (67, 'Supplier#000000034___ALGERIA', 1698, 34, 0),
            (68, 'Supplier#000000034___MOZAMBIQUE', 1698, 34,16),
            (69, 'Supplier#000000035___ROMANIA', 1932, 35,19),
            (70, 'Supplier#000000035___BRAZIL', 1932, 35, 2),
            (71, 'Supplier#000000036___ALGERIA', 1504, 36, 0),
            (72, 'Supplier#000000036___BRAZIL', 1504, 36, 2),
            (73, 'Supplier#000000037___BRAZIL', 2046, 37, 2),
            (74, 'Supplier#000000037___CANADA', 2046, 37, 3),
            (75, 'Supplier#000000038___JAPAN', 2200, 38,12),
            (76, 'Supplier#000000038___ROMANIA', 2200, 38,19),
            (77, 'Supplier#000000039___SAUDI ARABIA', 1978, 39,20),
            (78, 'Supplier#000000039___CANADA', 1978, 39, 3),
            (79, 'Supplier#000000040___BRAZIL', 1922, 40, 2),
            (80, 'Supplier#000000040___INDONESIA', 1922, 40, 9),
            (81, 'Supplier#000000041___CANADA', 2088, 41, 3),
            (82, 'Supplier#000000041___ALGERIA', 2088, 41, 0),
            (83, 'Supplier#000000042___EGYPT', 1770, 42, 4),
            (84, 'Supplier#000000042___UNITED KINGDOM', 1770, 42,23),
            (85, 'Supplier#000000043___CANADA', 1992, 43, 3),
            (86, 'Supplier#000000043___BRAZIL', 1992, 43, 2),
            (87, 'Supplier#000000044___MOZAMBIQUE', 2090, 44,16),
            (88, 'Supplier#000000044___BRAZIL', 2090, 44, 2),
            (89, 'Supplier#000000045___CANADA', 1932, 45, 3),
            (90, 'Supplier#000000045___IRAN', 1932, 45,10),
            (91, 'Supplier#000000046___MOZAMBIQUE', 2334, 46,16),
            (92, 'Supplier#000000046___CANADA', 2334, 46, 3),
            (93, 'Supplier#000000047___SAUDI ARABIA', 1748, 47,20),
            (94, 'Supplier#000000047___INDONESIA', 1748, 47, 9),
            (95, 'Supplier#000000048___IRAN', 2272, 48,10),
            (96, 'Supplier#000000048___JAPAN', 2272, 48,12),
            (97, 'Supplier#000000049___CANADA', 2020, 49, 3),
            (98, 'Supplier#000000049___UNITED KINGDOM', 2020, 49,23),
            (99, 'Supplier#000000050___SAUDI ARABIA', 2070, 50,20),
            (100, 'Supplier#000000050___GERMANY', 2070, 50, 7),
            (101, 'Supplier#000000051___CANADA', 2764, 51, 3),
            (102, 'Supplier#000000051___SAUDI ARABIA', 2764, 51, 20),
            (103, 'Supplier#000000052___CANADA', 2018, 52, 3),
            (104, 'Supplier#000000052___EGYPT', 2018, 52, 4),
            (105, 'Supplier#000000053___JAPAN', 1894, 53, 12),
            (106, 'Supplier#000000053___BRAZIL', 1894, 53, 2),
            (107, 'Supplier#000000054___BRAZIL', 1892, 54, 2),
            (108, 'Supplier#000000054___SAUDI ARABIA', 1892, 54, 20),
            (109, 'Supplier#000000055___UNITED KINGDOM', 2018, 55, 23),
            (110, 'Supplier#000000055___IRAQ', 2018, 55, 11),
            (111, 'Supplier#000000056___MOROCCO', 2076, 56, 15),
            (112, 'Supplier#000000056___EGYPT', 2076, 56, 4),
            (113, 'Supplier#000000057___CANADA', 1692, 57, 3),
            (114, 'Supplier#000000057___GERMANY', 1692, 57, 7),
            (115, 'Supplier#000000058___ALGERIA', 1746, 58, 0),
            (116, 'Supplier#000000058___EGYPT', 1746, 58, 4),
            (117, 'Supplier#000000059___CANADA', 2008, 59, 3),
            (118, 'Supplier#000000059___IRAN', 2008, 59, 10),
            (119, 'Supplier#000000060___IRAN', 1868, 60, 10),
            (120, 'Supplier#000000060___GERMANY', 1868, 60, 7),
            (121, 'Supplier#000000061___EGYPT', 1930, 61, 4),
            (122, 'Supplier#000000061___IRAN', 1930, 61, 10),
            (123, 'Supplier#000000062___INDONESIA', 1866, 62, 9),
            (124, 'Supplier#000000062___EGYPT', 1866, 62, 4),
            (125, 'Supplier#000000063___IRAN', 1852, 63, 10),
            (126, 'Supplier#000000063___MOZAMBIQUE', 1852, 63, 16),
            (127, 'Supplier#000000064___CANADA', 2184, 64, 3),
            (128, 'Supplier#000000064___IRAN', 2184, 64, 10),
            (129, 'Supplier#000000065___CANADA', 1646, 65, 3),
            (130, 'Supplier#000000065___IRAN', 1646, 65, 10),
            (131, 'Supplier#000000066___EGYPT', 2330, 66, 4),
            (132, 'Supplier#000000066___CANADA', 2330, 66, 3),
            (133, 'Supplier#000000067___CANADA', 1680, 67, 3),
            (134, 'Supplier#000000067___UNITED KINGDOM', 1680, 67, 23),
            (135, 'Supplier#000000068___CANADA', 2108, 68, 3),
            (136, 'Supplier#000000068___ETHIOPIA', 2108, 68, 5),
            (137, 'Supplier#000000069___CANADA', 1770, 69, 3),
            (138, 'Supplier#000000069___BRAZIL', 1770, 69, 2),
            (139, 'Supplier#000000070___INDONESIA', 1780, 70, 9),
            (140, 'Supplier#000000070___ROMANIA', 1780, 70, 19),
            (141, 'Supplier#000000071___CANADA', 2178, 71, 3),
            (142, 'Supplier#000000071___ALGERIA', 2178, 71, 0),
            (143, 'Supplier#000000072___CANADA', 1832, 72, 3),
            (144, 'Supplier#000000072___EGYPT', 1832, 72, 4),
            (145, 'Supplier#000000073___BRAZIL', 2588, 73, 2),
            (146, 'Supplier#000000073___JAPAN', 2588, 73, 12),
            (147, 'Supplier#000000074___IRAN', 1668, 74, 10),
            (148, 'Supplier#000000074___CANADA', 1668, 74, 3),
            (149, 'Supplier#000000075___BRAZIL', 2100, 75, 2),
            (150, 'Supplier#000000075___SAUDI ARABIA', 2100, 75, 20),
            (151, 'Supplier#000000076___IRAN', 1850, 76, 10),
            (152, 'Supplier#000000076___BRAZIL', 1850, 76, 2),
            (153, 'Supplier#000000077___EGYPT', 2134, 77, 4),
            (154, 'Supplier#000000077___KENYA', 2134, 77, 14),
            (155, 'Supplier#000000078___CANADA', 1964, 78, 3),
            (156, 'Supplier#000000078___IRAN', 1964, 78, 10),
            (157, 'Supplier#000000079___IRAN', 1964, 79, 10),
            (158, 'Supplier#000000079___ARGENTINA', 1964, 79, 1),
            (159, 'Supplier#000000080___EGYPT', 1700, 80, 4),
            (160, 'Supplier#000000080___BRAZIL', 1700, 80, 2),
            (161, 'Supplier#000000081___ALGERIA', 1776, 81, 0),
            (162, 'Supplier#000000081___JAPAN', 1776, 81, 12),
            (163, 'Supplier#000000082___CANADA', 2008, 82, 3),
            (164, 'Supplier#000000082___IRAN', 2008, 82, 10),
            (165, 'Supplier#000000083___BRAZIL', 2016, 83, 2),
            (166, 'Supplier#000000083___EGYPT', 2016, 83, 4),
            (167, 'Supplier#000000084___BRAZIL', 1980, 84, 2),
            (168, 'Supplier#000000084___MOROCCO', 1980, 84, 15),
            (169, 'Supplier#000000085___JORDAN', 1756, 85, 13),
            (170, 'Supplier#000000085___UNITED KINGDOM', 1756, 85, 23),
            (171, 'Supplier#000000086___EGYPT', 1926, 86, 4),
            (172, 'Supplier#000000086___MOROCCO', 1926, 86, 15),
            (173, 'Supplier#000000087___EGYPT', 2114, 87, 4),
            (174, 'Supplier#000000087___SAUDI ARABIA', 2114, 87, 20),
            (175, 'Supplier#000000088___ALGERIA', 1752, 88, 0),
            (176, 'Supplier#000000088___VIETNAM', 1752, 88, 21),
            (177, 'Supplier#000000089___ALGERIA', 1936, 89, 0),
            (178, 'Supplier#000000089___IRAN', 1936, 89, 10),
            (179, 'Supplier#000000090___IRAN', 1858, 90, 10),
            (180, 'Supplier#000000090___MOROCCO', 1858, 90, 15),
            (181, 'Supplier#000000091___ALGERIA', 1696, 91, 0),
            (182, 'Supplier#000000091___KENYA', 1696, 91, 14),
            (183, 'Supplier#000000092___JAPAN', 1694, 92, 12),
            (184, 'Supplier#000000092___ALGERIA', 1694, 92, 0),
            (185, 'Supplier#000000093___JORDAN', 1680, 93, 13),
            (186, 'Supplier#000000093___MOROCCO', 1680, 93, 15),
            (187, 'Supplier#000000094___BRAZIL', 1980, 94, 2),
            (188, 'Supplier#000000094___EGYPT', 1980, 94, 4),
            (189, 'Supplier#000000095___EGYPT', 1686, 95, 4),
            (190, 'Supplier#000000095___IRAN', 1686, 95, 10),
            (191, 'Supplier#000000096___MOROCCO', 2054, 96, 15),
            (192, 'Supplier#000000096___CANADA', 2054, 96, 3),
            (193, 'Supplier#000000097___BRAZIL', 1978, 97, 2),
            (194, 'Supplier#000000097___JAPAN', 1978, 97, 12),
            (195, 'Supplier#000000098___CANADA', 1872, 98, 3),
            (196, 'Supplier#000000098___IRAN', 1872, 98, 10),
            (197, 'Supplier#000000099___INDONESIA', 2454, 99, 9),
            (198, 'Supplier#000000099___BRAZIL', 2454, 99, 2),
            (199, 'Supplier#000000100___IRAN', 1874, 00, 10),
            (200, 'Supplier#000000100___JAPAN', 1874, 00, 12),

        ]

        sql = "INSERT INTO warehouse VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, warehouse)

        _conn.commit()
        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")



def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    try:
        sql = """select *
                from warehouse"""
        
        cur = _conn.cursor()
        cur.execute(sql)
        output = open("output/1.out", "w")

        l = '{:>10} {:>5} {:>40} {:>10} {:>10}'.format("wId", "wName", "wCap", "sId", "nId")
        print(l, file = output)

        rows = cur.fetchall()
        for row in rows:
            l = '{:>10} {:<46} {:<12} {:>2} {:>10}'.format(row[0], row[1], row[2], row[3], row[4])
            print(l, file = output)
        
        output.close()
        print("SUCCESS")

    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    try:
        sql = """select n_name as nation, count(w_capacity) as numW, sum(w_capacity) as totCap
                from nation, warehouse
                where n_nationkey = w_nationkey
                group by n_name
                order by numW DESC;"""

        cur = _conn.cursor()
        cur.execute(sql)
        output = open("output/2.out", "w")

        l = '{:<25} {:>13} {:>10}'.format('nation', 'numW', 'totCap')
        print(l, file = output)
        # print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:<20} {:>18} {:>10}'.format(row[0], row[1], row[2])
            print(l, file = output)
            # print(l)

        output.close()
        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")



def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    Input = open("input/3.in", "r")
    nation = Input.read().splitlines()
    #print(nation)

    try:
        sql = """select distinct s_name, n1.n_name, w_name
                from supplier, nation n1, nation n2, warehouse
                where n2.n_nationkey = w_nationkey AND 
                        n2.n_name = ? AND 
                        n1.n_nationkey = s_nationkey AND 
                        s_suppkey = w_suppkey"""

        cur = _conn.cursor()
        cur.execute(sql, nation)
        output = open("output/3.out", "w")

        l = '{:<10} {:>16} {:>23}'.format('supplier', 'nation', 'warehouse')
        print(l, file = output)
        # print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:<20} {:<20} {:>25}'.format(row[0], row[1], row[2])
            print(l, file = output)
            # print(l)

        output.close()
        Input.close()

        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)

def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    Input = open("input/4.in", "r")
    args = Input.read().splitlines()
    #print(args)

    try:
        sql = """select w_name, w_capacity
                from warehouse, nation, region
                where n_nationkey = w_nationkey AND 
                    n_regionkey = r_regionkey AND 
                    r_name = ? AND 
                    w_capacity > ?
                order by w_capacity desc"""

        cur = _conn.cursor()
        cur.execute(sql, (args[0], args[1]))
        output = open("output/4.out", "w")

        l = '{:<40} {:>10}'.format("warehouse", "capacity")
        print(l, file = output)
        # print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:<36} {:>10}'.format(row[0], row[1])
            print(l, file = output)
            # print(l)

        output.close()
        Input.close()
        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")

def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    Input = open("input/5.in", "r")
    args = Input.read().splitlines()
    # print(args)

    try:
        sql = """select r_name, w_capacity
                    from region, warehouse, supplier, nation
                    where s_nationkey = n_nationkey AND
                            s_suppkey = w_suppkey AND
                            n_nationkey = ?"""

        cur = _conn.cursor()
        cur.execute(sql, args)
        output = open("output/5.out", "w") 

        l = '{:<40} {:>10}'.format("warehouse", "capacity")
        print(l, file = output)
        # print(l)

        rows = cur.fetchall()
        for row in rows:
            l = '{:<36} {:>10}'.format(row[0], row[1])
            print(l, file = output)
            # print(l)

        output.close()
        Input.close()
        print("SUCCESS")

    except Error as e:
        _conn.rollback()
        print(e)
    print("++++++++++++++++++++++++++++++++++")


def main():
    database = r"data/tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        createTable(conn)
        populateTable(conn)

        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
