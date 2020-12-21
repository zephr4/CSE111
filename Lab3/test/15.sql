select substr(o_orderdate, 1, 4) as year, r_name as region, count(o_orderpriority) as PO
from orders, region, nation, supplier, lineitem
where s_suppkey = l_suppkey and 
        l_orderkey = o_orderkey and 
        s_nationkey = n_nationkey and 
        n_regionkey = r_regionkey and 
        o_orderpriority = '1-URGENT'
group by year, region
order by year, region, PO desc;