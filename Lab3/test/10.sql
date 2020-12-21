select sum(o_totalprice)
from orders, customer, nation, region
where o_custkey = c_custkey and 
        c_nationkey = n_nationkey and 
        n_regionkey = r_regionkey and 
        r_name = 'EUROPE' and 
        o_orderdate >= '1996-01-01' and 
        o_orderdate < '1997-01-01';