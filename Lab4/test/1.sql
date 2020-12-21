select c_name as customer, sum(o_totalprice) as total
from customer, orders, nation 
where c_custkey = o_custkey AND
        c_nationkey = n_nationkey AND
        o_orderdate >= '1996-01-01' AND
        o_orderdate < '1997-01-01' AND
        n_name = 'RUSSIA'
group by customer;
