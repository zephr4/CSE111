select s_name as supplier, o_orderpriority as status, count(o_orderkey)
from nation, orders, supplier, part, partsupp, lineitem, region
where n_regionkey = r_regionkey AND
        n_nationkey = s_nationkey AND
        s_suppkey = ps_suppkey AND
        ps_partkey = p_partkey AND
        p_partkey = l_partkey AND
        l_orderkey = o_orderkey AND 
        l_suppkey = ps_suppkey AND
        r_regionkey = '1'
group by supplier, status;