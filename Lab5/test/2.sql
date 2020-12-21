select r1.r_name as Region, count(s_suppkey) as NumSupp
from region r1, nation, supplier
where r1.r_regionkey = n_regionkey AND
        s_nationkey = n_nationkey AND
        s_acctbal > (select avg(s_acctbal)
                        from supplier, region r2, nation
                        where s_nationkey = n_nationkey AND
                                n_regionkey = r2.r_regionkey
                                AND r2.r_name = r1.r_name)
group by r_name;
