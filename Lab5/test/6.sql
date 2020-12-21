select p_mfgr as Manufacturer
from part, supplier, partsupp
where p_partkey = ps_partkey AND
        ps_suppkey = s_suppkey AND
        s_name = 'Supplier#000000053' AND
        ps_availqty = (select min(ps_availqty)
                        from partsupp
                        where ps_suppkey = 53);