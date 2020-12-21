select count(o_orderkey)
from orders, nation, customer
where o_custkey = c_custkey AND
        c_nationkey = n_nationkey AND
        n_name = 'PERU' AND
        o_orderdate >= '1996-01-01' AND
        o_orderdate < '1997-01-01';
