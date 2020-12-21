select distinct l_receiptdate, count(*)
from lineitem, orders, customer
where c_name = 'Customer#000000106' and 
        c_custkey = o_custkey and 
        l_orderkey = o_orderkey
group by l_receiptdate;