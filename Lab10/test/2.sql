DROP TRIGGER IF EXISTS T2;

CREATE TRIGGER T2 
    AFTER UPDATE 
    ON customer
    FOR EACH ROW BEGIN
        update customer
        set c_comment = 'NEGATIVE BALANCE!!!'
        where old.c_acctbal >= 0
                AND new.c_acctbal < 0;
    End;

UPDATE customer
set c_acctbal = -100
where c_nationkey = (select n_nationkey
                     from nation
                     where n_regionkey = 3);

select count(c_custkey)
from customer
where c_acctbal < 0 AND
        c_nationkey = 6;