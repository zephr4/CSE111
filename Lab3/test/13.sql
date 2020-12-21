select avg(c_acctbal) as Average
from customer, nation, region
where c_nationkey = n_nationkey and 
        n_regionkey = r_regionkey and 
        r_name = 'AFRICA' and 
        c_mktsegment = 'MACHINERY';