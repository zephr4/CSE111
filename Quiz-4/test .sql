SELECT distinct pr1.maker, pr1.type, min(pc.price) as min, max(pc.price) as max
    from Product pr1, PC pc
    where pr1.model = pc.model
group by pr1.maker
UNION
SELECT distinct pr2.maker, pr2.type, min(lt.price), max(lt.price)
    from Product pr2, Laptop lt
    where pr2.model = lt.model
group by pr2.maker
UNION
SELECT distinct pr3.maker, pr3.type, min(pt.price), max(pt.price)
    from Product pr3, Printer pt
    where pr3.model = pt.model
group by pr3.maker