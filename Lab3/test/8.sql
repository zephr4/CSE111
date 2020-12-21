select s_name
from supplier, nation, region 
where s_nationkey = n_nationkey and    
        n_regionkey = r_regionkey and 
        r_name = 'ASIA' and 
        s_acctbal < '1000';