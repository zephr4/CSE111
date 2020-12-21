select (select sum(l_extendedprice*(1-l_discount))
        from lineitem, orders, customer, nation, supplier
        where o_orderkey = l_orderkey AND 
                o_custkey = c_custkey AND 
                c_nationkey = n_nationkey AND 
                s_suppkey = l_suppkey AND 
                n_regionkey = 3 AND 
                strftime('%Y', l_shipdate) = '1996' AND 
                s_nationkey = 24)/
(select sum(l_extendedprice*(1-l_discount))
from lineitem, orders, customer, nation
where o_orderkey = l_orderkey AND 
        o_custkey = c_custkey AND 
        c_nationkey = n_nationkey AND 
        n_regionkey = 3 AND 
        strftime('%Y', l_shipdate) = '1996')