select region1, region2, count(o_orderkey) as total_price
from (select *, r_name as region1
        from region, orders, nation, customer
        where o_custkey = c_custkey AND
                c_nationkey = n_nationkey AND
                n_regionkey = r_regionkey),
     (select *, r_name as region2
        from region, nation, supplier, lineitem 
        where s_suppkey = l_suppkey AND
                s_nationkey = n_nationkey AND
                n_regionkey = r_regionkey)
where o_orderkey = l_orderkey
group by region1, region2;