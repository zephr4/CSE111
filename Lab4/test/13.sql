select count(l_orderkey) as Supplied
from (select *
        from supplier, nation, region, lineitem
        where s_suppkey = l_suppkey AND
                s_nationkey = n_nationkey AND
                n_regionkey = r_regionkey AND
                r_name = 'ASIA'),
     (select *
        from customer, orders, nation
        where c_custkey = o_custkey AND
                c_nationkey = n_nationkey AND
                n_name = 'ARGENTINA')
where l_orderkey = o_orderkey;