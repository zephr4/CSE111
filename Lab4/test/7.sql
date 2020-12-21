select n_name as country, o_orderstatus as status, count(o_orderkey) as num_orders
from nation, orders, customer, region
where o_custkey = c_custkey AND
        c_nationkey = n_nationkey AND
        n_regionkey = r_regionkey AND
        r_regionkey = '3'
group by country, status;
