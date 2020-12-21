/* Andy Alvarenga -- Quiz 2 */

create table Classes(
    c_class varchar(32) PRIMARY KEY,
    c_type varchar(2),  
    c_country varchar(32),
    c_numGuns integer,
    c_bore integer,
    c_displacement integer
); 

create table Ships(
    s_name varchar(32),
    s_class varchar(32),
    s_launched integer   
);

create table Battles(
    b_name varchar(32),
    b_date text
);

create table Outcomes(
    o_ship varchar(32),
    o_battle varchar(32),
    o_result varchar(32)
);

insert into Classes (c_class, c_type, c_country, c_numGuns, c_bore, c_displacement)
values ('Bismarck', 'bb', 'Germany', 8, 15, 42000),
        ('Iowa', 'bb', 'USA', 9, 16, 46000),
        ('Kongo', 'bc', 'Japan', 8, 14, 32000),
        ('North Carolina', 'bb', 'USA', 9, 16, 37000),
        ('Renown', 'bc', 'Britain',6, 15, 32000),
        ('Revenge', 'bb', 'Britain', 8, 15, 29000),
        ('Tennessee', 'bb', 'USA',12,14,32000),
        ('Yamato', 'bb', 'Japan', 9, 18, 65000);

insert into Ships (s_name, s_class, s_launched)
values ('California', 'Tennessee', 1915),
        ('Haruna', 'Kongo', 1915),
        ('Hiei', 'Kongo', 1915),
        ('Iowa', 'Iowa', 1933),
        ('Kirishima', 'Kongo', 1915),
        ('Kongo', 'Kongo', 1913),
        ('Missouri', 'Iowa', 1935),
        ('Musashi', 'Yamato', 1942),
        ('New Jersey', 'Iowa', 1936),
        ('North Carolina', 'North Carolina',1941),
        ('Ramillies', 'Revenge',1917),
        ('Renown', 'Renown', 1916),
        ('Repulse', 'Renown', 1916),
        ('Resolution', 'Revenge', 1916),
        ('Revenge', 'Revenge', 1916),
        ('Royal Oak', 'Revenge', 1916),
        ('Royal Sovereign', 'Revenge', 1916),
        ('Tennessee', 'Tennessee', 1915),
        ('Washington', 'North Carolina', 1941),
        ('Wisconsin', 'Iowa', 1940),
        ('Yamato', 'Yamato', 1941);

insert into Battles (b_name, b_date)
values ('Denmark Strait', 05-24-41),
        ('Guadalcanal', 11-15-42),
        ('North Cape', 12-26-43),
        ('Surigao Strait', 10-25-44);

insert into Outcomes (o_ship, o_battle, o_result)
values ('California', 'Surigao Strait', 'ok'),
        ('Kirishima', 'Guadalcanal', 'sunk'),
        ('Resolution', 'Denmark Strait', 'ok'),
        ('Wisconsin', 'Guadalcanal', 'damaged'),
        ('Tennessee', 'Surigao Strait', 'ok'),
        ('Washington', 'Guadalcanal', 'ok'),
        ('New Jersey', 'Surigao Strait', 'ok'),
        ('Yamato', 'Surigao Strait', 'sunk'),
        ('Wisconsin', 'Surigao Strait', 'damaged');

/* 1. Find the class name and the country of the classes that carry guns of at least 15-inch bore. */  
select c_class as Class, c_country as Country
from Classes
where c_bore >= 15;

/* 2. Find the ships launched prior to 1918. */
select s_name as Ship 
from Ships
where s_launched < 1918;

/* 3. Find the ships sunk in the battle of Surigao Strait. */
select o_ship as Ship
from Outcomes
where o_battle = 'Surigao Strait' AND o_result = 'sunk';

/* 4. List the ships with a displacement larger than 40,000 tons built after 1921. */
select s_name as Ship
from Ships, Classes
where s_class = c_class AND 
        c_displacement > 40000 AND
        s_launched > 1921;

/* 5. List the name, displacement, and number of guns of the ships engaged in the battle of Surigao Strait. */
select s_name as Ship, c_displacement as Displacement, c_numGuns as Guns
from Ships, Classes, Outcomes
where s_class = c_class AND
        s_name = o_ship AND
        o_battle = 'Surigao Strait';

/* 6. List  the  name  of  all  the  ships  from  the  database.   Ships  appear  in Ships, Classes,  and Outcomes tables.  All of them have to be printed. */
select s_name as Ship
from Ships;

/* 7.  Find the classes that have exactly two ships in the class. */
select c_class as Class
from Classes, Ships
where s_class = c_class
group by class
having count(s_class) = 2;

/* 8. Find the countries that have both bb and bc ships. */
select c1.c_country as Country
from Classes c1, Classes c2
where c1.c_country = c2.c_country AND
        c1.c_type = 'bb' AND
        c2.c_type = 'bc';

/* 9. Find the ships that survived a battle in which they were damaged and then fought in another battle. */
select o_ship as Ship 
from Outcomes
group by Ship
having count(o_result) > 1;

/* 10. For every class with at least three ships, find the number of ships of that class sunk in battle.
        If a class has zero sunk ships, this number has to be included in the result together with the class. */
select c_class as Class, count(s_name) as NumShips, o_result as Result
from Classes, Ships, Outcomes
where c_class = s_class AND
        s_name = o_ship AND
        Result = 'sunk'
group by Class;
-- UNION
-- select count(o_ship) as NumShips, o_result as Result
-- from Ships, Outcomes
-- where s_name = o_ship AND 
--         o_result = 'sunk';