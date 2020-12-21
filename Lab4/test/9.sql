select count(distinct o_clerk) as num_clerk
from orders, supplier, nation, lineitem
where s_nationkey = n_nationkey AND
        s_suppkey = l_suppkey AND
        o_orderkey = l_orderkey AND
        n_name = 'CANADA';