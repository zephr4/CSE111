select r_name as Region, count(c_custkey) as NumCust
from region, customer, nation
WHERE nation.n_nationkey = customer.c_nationkey AND
        r_regionkey = n_regionkey AND
        NOT customer.c_custkey IN(SELECT o_custkey
                                    FROM orders) AND 
        c_acctbal > (select avg(c_acctbal)
                        from customer) 
group by Region;