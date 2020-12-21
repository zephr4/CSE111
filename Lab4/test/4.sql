select s_name as supplier, count(p_partkey) as num_parts
from supplier, part, partsupp, nation 
where p_partkey = ps_partkey AND
        ps_suppkey = s_suppkey AND
        s_nationkey = n_nationkey AND
        p_size < '30' AND
        n_name = 'CHINA'
group by supplier;
