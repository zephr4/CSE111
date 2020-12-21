select max(l_discount) as Max_Discount
from lineitem, orders
where l_orderkey = o_orderkey AND
        o_orderdate >= '1995-05-01' AND
        o_orderdate < '1995=06-01' AND
        l_discount < (select avg(l_discount)
                        from lineitem);
                    