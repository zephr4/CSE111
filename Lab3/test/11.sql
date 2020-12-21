select o_custkey as cust, count(l_discount) as num_discount
from orders, lineitem
where o_orderkey = l_orderkey and 
        l_discount >= 0.05
group by o_custkey
having num_discount >= 70
order by cust desc;

