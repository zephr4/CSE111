select count(distinct s_name) as Supplier
from supplier, partsupp, part
where s_suppkey = ps_suppkey AND
        ps_partkey = p_partkey AND
        substr(p_type, 1, 15) = 'MEDIUM POLISHED' AND 
        p_size IN (3, 23, 36, 49);