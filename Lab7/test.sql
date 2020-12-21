select n_name as nation, COUNT(w_capacity) as numW, w_capacity as totCap
from nation, warehouse
where n_nationkey = w_nationkey
group by n_name
order by numW DESC;