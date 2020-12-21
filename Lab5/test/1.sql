select count(c_custkey) as NumCust
from customer, nation
where c_nationkey = n_nationkey AND
        n_regionkey != 3 AND
        n_regionkey != 0;