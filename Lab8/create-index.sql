-- Q1 --
DROP INDEX customer_idx_c_name;
CREATE INDEX customer_idx_c_name ON customer(c_name);

-- Q2 --
DROP INDEX supplier_idx_s_acctbal;
CREATE INDEX supplier_idx_s_acctbal ON supplier(s_acctbal);

-- Q3 --
DROP INDEX lineitem_idx_l_returnflag_l_receiptdate;
CREATE INDEX lineitem_idx_l_returnflag_l_receiptdate ON lineitem(l_returnflag, l_receiptdate);

-- Q4 --
DROP INDEX lineitem_idx_l_shipdate_l_commitdate;
CREATE INDEX lineitem_idx_l_shipdate_l_commitdate ON lineitem(l_shipdate, l_receiptdate);

-- Q5 --
DROP INDEX customer_idx_c_mktsegment;
CREATE INDEX customer_idx_c_mktsegment ON customer(c_mktsegment);

-- Q6 --
DROP INDEX nation_idx_n_nationkey;
DROP INDEX customer_idx_c_custkey;
DROP INDEX orders_idx_o_orderdate;
CREATE INDEX nation_idx_n_nationkey ON nation(n_nationkey);
CREATE INDEX customer_idx_c_custkey ON customer(c_custkey);
CREATE INDEX orders_idx_o_orderdate ON orders(o_orderdate);

-- Q7 --
DROP INDEX lineitem_idx_l_orderkey_l_receiptdate;
DROP INDEX orders_idx_o_custkey_o_orderkey;
DROP INDEX customer_idx_c_name_c_custkey;
CREATE INDEX lineitem_idx_l_orderkey_l_receiptdate ON lineitem(l_orderkey, l_receiptdate);
CREATE INDEX orders_idx_o_custkey_o_orderkey ON orders(o_custkey, o_orderkey);
CREATE INDEX customer_idx_c_name_c_custkey ON customer(c_name, c_custkey);

-- Q8 --
DROP INDEX supplier_idx_s_nationkey_s_acctbal;
DROP INDEX nation_idx_n_regionkey_n_nationkey;
DROP INDEX region_idx_r_name_r_regionkey;
CREATE INDEX supplier_idx_s_nationkey_s_acctbal ON supplier(s_nationkey, s_acctbal);
CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey, n_nationkey);
CREATE INDEX region_idx_r_name_r_regionkey ON region(r_name, r_regionkey);

-- Q9 --
DROP INDEX nation_idx_n_name;
CREATE INDEX nation_idx_n_name ON nation(n_name);

-- Q10 --
DROP INDEX orders_idx_o_custkey_o_orderdate;
DROP INDEX customer_idx_c_nationkey_c_custkey;
DROP INDEX nation_idx_n_regionkey_n_nationkey;
DROP INDEX region_idx_r_regionkey;
CREATE INDEX orders_idx_o_custkey_o_orderdate ON orders(o_custkey, o_orderdate);
CREATE INDEX customer_idx_c_nationkey_c_custkey ON customer(c_nationkey, c_custkey);
CREATE INDEX nation_idx_n_regionkey_n_nationkey ON nation(n_regionkey, n_nationkey);
CREATE INDEX region_idx_r_regionkey ON region(r_regionkey);

--11
DROP INDEX lineitem_idx_l_orderkey_l_discount;
CREATE INDEX lineitem_idx_l_orderkey_l_discount ON lineitem(l_orderkey, l_discount);

--12
DROP INDEX orders_idx_o_custkey_o_orderstatus;
DROP INDEX customer_idx_c_custkey_c_nationkey;
DROP INDEX nation_idx_n_nationkey_n_regionkey;
DROP INDEX region_idx_r_regionkey;
CREATE INDEX orders_idx_o_custkey_o_orderstatus ON orders(o_custkey, o_orderstatus);
CREATE INDEX customer_idx_c_custkey_c_nationkey ON customer(c_custkey, c_nationkey);
CREATE INDEX nation_idx_n_nationkey_n_regionkey ON nation(n_nationkey, n_regionkey);
CREATE INDEX region_idx_r_regionkey ON region(r_regionkey);

--13
DROP INDEX customer_idx_c_nationkey_c_mktsegment;
DROP INDEX nation_idx_n_nationkey_n_regionkey;
DROP INDEX region_idx_r_regionkey_r_name;
CREATE INDEX customer_idx_c_nationkey_c_mktsegment ON customer(c_nationkey, c_mktsegment);
CREATE INDEX nation_idx_n_nationkey_n_regionkey ON nation(n_nationkey, n_regionkey);
CREATE INDEX region_idx_r_regionkey_r_name ON region(r_regionkey, r_name);

--14
DROP INDEX customer_idx_c_nationkey_c_custkey;
DROP INDEX nation_idx_n_name_n_nationkey;
DROP INDEX orders_idx_o_orderpriority;
CREATE INDEX customer_idx_c_nationkey_c_custkey ON customer(c_nationkey, c_custkey);
CREATE INDEX nation_idx_n_name_n_nationkey ON nation(n_name, n_nationkey);
CREATE INDEX orders_idx_o_orderpriority ON orders(o_orderpriority, o_custkey);

--15
DROP INDEX orders_idx_o_orderpriority_o_orderkey;
DROP INDEX lineitem_idx_l_orderkey_l_suppkey;
DROP INDEX supplier_idx_s_suppkey_s_nationkey;
DROP INDEX nation_idx_n_nationkey_n_regionkey;
DROP INDEX region_idx_r_regionkey;
CREATE INDEX orders_idx_o_orderpriority_o_orderkey ON orders(o_orderpriority, o_orderkey);
CREATE INDEX lineitem_idx_l_orderkey_l_suppkey ON lineitem(l_orderkey, l_suppkey);
CREATE INDEX supplier_idx_s_suppkey_s_nationkey ON supplier(s_suppkey, s_nationkey);
CREATE INDEX nation_idx_n_nationkey_n_regionkey ON nation(n_nationkey, n_regionkey);
CREATE INDEX region_idx_r_regionkey ON region(r_regionkey);