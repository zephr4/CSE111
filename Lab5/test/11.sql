select p_name as Part
from part
inner join lineitem
on p_partkey = l_partkey AND 
    l_extendedprice * (1-l_discount) = (select max(l_extendedprice * (1-l_discount))
                                                            from lineitem)
    where julianday(l_shipdate) > julianday('1994-08-02')
group by Part; 