select o_orderpriority as Priority, count(distinct o_orderkey) as NumOrders
from orders, lineitem
where o_orderkey = l_orderkey AND 
        l_commitdate < l_receiptdate AND
        o_orderdate >= '1996-10-01' AND 
        o_orderdate <= '1996-12-31'
group by Priority
order by Priority ASC;