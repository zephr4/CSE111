select n_name as country, avg(s_acctbal) as avg_balance
from nation, supplier
where n_nationkey = s_nationkey
group by country;