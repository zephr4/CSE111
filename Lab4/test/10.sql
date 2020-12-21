select p_type as Promo, avg(l_discount) as avg_discount
from lineitem, part 
where l_partkey = p_partkey AND
        p_type LIKE '%PROMO%'
group by Promo;