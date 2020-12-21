select n_name, min(s_acctbal)
from nation, supplier
where n_nationkey = s_nationkey
group by n_name
having count(*) < 3;