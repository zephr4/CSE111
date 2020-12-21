select r1.r_name Region1, r2.r_name as Region2, strftime('%Y', l_shipdate) as Year, sum(l_extendedprice*(1-l_discount)) as Sum
from region r1, region r2, lineitem
INNER JOIN nation n1, nation n2, supplier, customer, orders
on r1.r_regionkey = n1.n_regionkey AND 
    r2.r_regionkey = n2.n_regionkey AND 
    n1.n_nationkey = s_nationkey AND 
    s_suppkey = l_suppkey AND 
    n2.n_nationkey = c_nationkey AND 
    c_custkey = o_custkey AND 
    o_orderkey = l_orderkey
where strftime('%Y', l_shipdate) = '1996' OR strftime('%Y', l_shipdate) = '1995'
group by Region1, Region2, Year;