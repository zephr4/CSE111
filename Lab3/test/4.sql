select avg(julianday(l_shipdate) - julianday(l_commitdate)) as averageCompletions
from lineitem
where l_shipdate >= l_commitdate;