select count(distinct o_orderkey) as num_orders
from (select *
        from customer, orders
        where c_custkey = o_custkey AND
                c_acctbal < 0),
     (select *
        from supplier, lineitem
        where s_suppkey = l_suppkey AND
                s_acctbal < 0)
where o_orderkey = l_orderkey;