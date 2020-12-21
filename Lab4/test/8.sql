select n_name as country, count(distinct o_orderkey) as num_orders
from orders, nation, supplier, partsupp, lineitem
where s_nationkey = n_nationkey AND
        s_suppkey = ps_suppkey AND
        ps_suppkey = l_suppkey AND
        l_orderkey = o_orderkey AND
        o_orderdate >= '1994-01-01' AND
        o_orderdate < '1995-01-01' AND
        o_orderstatus = 'F'
group by country
having num_orders > 300;
