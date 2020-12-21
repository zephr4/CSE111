select c_mktsegment,
        min(c_acctbal) as mini,
        max(c_acctbal) as maxi,      
        avg(c_acctbal) as average,
        sum(c_acctbal) as total
from customer
group by c_mktsegment
order by total desc;