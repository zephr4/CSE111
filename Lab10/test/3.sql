DROP TRIGGER IF EXISTS T3;

CREATE TRIGGER T3 
    AFTER UPDATE 
    ON customer
    FOR EACH ROW
    when old.c_acctbal < 0 AND new.c_acctbal >= 0
    BEGIN
        update customer
        set c_comment = 'Positive balance!'
        where old.c_custkey = new.c_custkey;
    END;

UPDATE customer
set c_acctbal = 100
where c_nationkey = 19;

select count(c_custkey)
from customer, nation
where c_nationkey = n_nationkey AND
        n_regionkey = 3 AND 
        c_acctbal < 0;