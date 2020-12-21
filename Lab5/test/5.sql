select s_name as Supplier, p_size as Size, min(ps_supplycost) as MinCost
from supplier, part, partsupp, nation
where nation.n_nationkey = supplier.s_nationkey AND
        s_suppkey = ps_suppkey AND
        ps_partkey = p_partkey AND
        substr(p_type, length(p_type) - 4, length(p_type)) = 'STEEL' AND 
        s_suppkey = ps_suppkey AND 
        ps_partkey = p_partkey AND 
        n_regionkey = 1
group by Size;
