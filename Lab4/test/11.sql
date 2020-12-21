select n_name as country, s_name as supplier, max(s_acctbal) as balance
from nation, supplier
where n_nationkey = s_nationkey
group by country;