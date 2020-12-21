select Distinct n_name 
from nation, customer, orders
where c_custkey = o_custkey and 
        c_nationkey = n_nationkey and 
        o_orderdate >= '1995-03-10' and 
        o_orderdate <= '1995-03-12';
