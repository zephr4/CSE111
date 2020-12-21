select n_name as nation, count(s_nationkey) as suppliers
from supplier, nation 
where s_nationkey = n_nationkey
group by nation;