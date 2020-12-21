
select n_name as nation, count(o_orderkey) as num_orders
from nation, orders, region, customer
where o_custkey = c_custkey AND
        c_nationkey = n_nationkey AND
        n_regionkey = r_regionkey AND
        r_regionkey = '2'
group by nation;