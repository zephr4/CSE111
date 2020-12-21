select count(*)
from orders, customer, nation
where o_custkey = c_custkey and     
        c_nationkey = n_nationkey and
        o_orderpriority = '1-URGENT' and 
        o_orderdate >= '1994-01-01' and 
        o_orderdate < '1997-01-01' and
        n_name = 'FRANCE';
        