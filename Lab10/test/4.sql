DROP TRIGGER IF EXISTS T4;

CREATE TRIGGER T4 
    AFTER DELETE 
    ON lineitem
    FOR EACH ROW BEGIN
        update orders
        set o_orderpriority = 'HIGH'
        where o_orderkey = (select old.l_orderkey
                                from lineitem);
    END;

DELETE FROM lineitem
where l_commitdate LIKE '1996-11-%%';

select count(o_orderpriority)
from orders
where o_orderpriority = 'HIGH' AND 
        o_orderdate LIKE '1996-11-%%';