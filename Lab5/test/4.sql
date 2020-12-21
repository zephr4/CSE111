select n_name as Nation, count(distinct c_custkey) as NumCust, count(distinct  s_suppkey) as NumSupp
from customer, nation, supplier
where c_nationkey = n_nationkey AND
        n_nationkey = s_nationkey AND
        n_regionkey = 3
group by Nation;