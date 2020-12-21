-- CREATE TRIGGER insert_date_orders 
--     AFTER INSERT 
--     ON orders
--     FOR EACH ROW
--     BEGIN
--         insert into orders
--             select *
--             from orders
--             where OLD.o_orderdate = '2020-12-01';
--     END;

-- INSERT INTO orders VALUEs(1111111123321, 321, 0, 56000.91, 1992-02-21, 'HIGH', 'Clerk#000000409', 0, 'inserted value')

-- select count(o_orderkey)
-- from orders
-- where o_orderdate = '2020-12-01';
DROP TRIGGER IF EXISTS T1;

CREATE TRIGGER T1 
    AFTER INSERT 
    ON orders
    FOR EACH ROW BEGIN
        update orders
        set o_orderdate = '2020-12-01'
        WHERE o_orderkey = new.o_orderkey;
    END;

INSERT INTO orders
    select *
    from orders
    WHERE '1995-11-%%';

select count(distinct o_orderkey)
from orders
WHERE o_orderdate LIKE '2020-%%-%%';