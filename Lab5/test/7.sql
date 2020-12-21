select o_orderpriority as Priority, count(l_partkey) as NumParts
from orders, lineitem
where o_orderkey = l_orderkey AND
        o_orderdate >= '1996-01-01' AND
        o_orderdate < '1997-01-01' AND
        julianday(l_receiptdate) - julianday(l_commitdate) > 0
group by Priority 
order by Priority desc;