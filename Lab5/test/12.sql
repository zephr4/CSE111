select sum(ps_supplycost) as TotalCost
from partsupp, part, lineitem
where ps_partkey = p_partkey AND 
        p_partkey = l_partkey AND 
        l_suppkey = ps_suppkey AND 
        p_retailprice < 1000 AND 
        l_shipdate >= '1996-01-01' AND
        l_shipdate < '1997-01-01' AND
        l_suppkey NOT IN (select distinct l_suppkey
                            from lineitem
                            where l_shipdate >= '1995-01-01' AND
                                    l_shipdate < '1996-01-01' AND
                                    l_extendedprice < 2000);