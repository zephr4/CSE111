DROP TRIGGER IF EXISTS T5;

CREATE TRIGGER T5
    AFTER DELETE
    ON partsupp
    FOR EACH ROW BEGIN
        DELETE FROM partsupp
        where ps_partkey = old.ps_partkey;

        DELETE FROM lineitem
        where l_partkey = old.ps_partkey;
    END;

DELETE FROM partsupp
where ps_suppkey = (select p2.ps_suppkey
                    from partsupp p2, supplier
                    where p2.ps_suppkey = s_suppkey AND
                            s_nationkey = 6 OR
                            s_nationkey = 7);

select n_name, count(*)
from nation, partsupp, supplier
where n_nationkey = s_nationkey AND
        ps_suppkey = s_suppkey AND
        n_regionkey = 3
group by n_name;