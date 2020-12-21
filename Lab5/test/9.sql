select count(ps_partkey) as SuppliedParts
from partsupp, supplier  
where ps_suppkey = s_suppkey AND
        s_nationkey = '3' AND
        (ps_availqty * ps_supplycost) IN(select (ps_availqty * ps_supplycost) AS ps_totalValue
                                            from partsupp
                                            order by ps_totalValue DESC
                                            limit(8000*0.03));