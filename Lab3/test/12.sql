select r_name as region, count(o_orderstatus) as status
from region, orders, customer, nation 
where o_custkey = c_custkey and
        c_nationkey = n_nationkey and 
        n_regionkey = r_regionkey and 
        o_orderstatus = 'F'
group by r_name
order by status desc;