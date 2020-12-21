/*Andy Alvarenga*/
/*1*/
create table Classes(
    class varchar(32) PRIMARY KEY,
    type varchar(2),  
    country varchar(32),
    numGuns integer,
    bore integer,
    displacement integer
); 

create table Ships(
    name varchar(32),
    class varchar(32),
    launched integer   
);

create table Battles(
    name varchar(32),
    date text
);

create table Outcomes(
    ship varchar(32),
    battle varchar(32),
    result varchar(32)
);
/*2*/
insert into Classes (class, type, country, numGuns, bore, displacement)
values ('Bismarck', 'bb', 'Germany', 8, 15, 42000),
        ('Iowa', 'bb', 'USA', 9, 16, 46000),
        ('Kongo', 'bc', 'Japan', 8, 14, 32000),
        ('North Carolina', 'bb', 'USA', 9, 16, 37000),
        ('Renown', 'bc', 'Britain',6, 15, 32000),
        ('Revenge', 'bb', 'Britain', 8, 15, 29000),
        ('Tennessee', 'bb', 'USA',12,14,32000),
        ('Yamato', 'bb', 'Japan', 9, 18, 65000);

insert into Ships (name, class, launched)
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

insert into Battles (name, date)
values ('Denmark Strait', '05-24-41'),
        ('Guadalcanal', '11-15-42'),
        ('North Cape', '12-26-43'),
        ('Surigao Strait', '10-25-44');

insert into Outcomes (ship, battle, result)
values ('California', 'Surigao Strait', 'ok'),
        ('Kirishima', 'Guadalcanal', 'sunk'),
        ('Resolution', 'Denmark Strait', 'ok'),
        ('Wisconsin', 'Guadalcanal', 'damaged'),
        ('Tennessee', 'Surigao Strait', 'ok'),
        ('Washington', 'Guadalcanal', 'ok'),
        ('New Jersey', 'Surigao Strait', 'ok'),
        ('Yamato', 'Surigao Strait', 'sunk'),
        ('Wisconsin', 'Surigao Strait', 'damaged');

/*3*/
select class, country
from Classes
group by class
having bore >= 15;

/*4*/
select name, launched
from Ships
group by name
having launched < 1918;

/*5*/
select ship, result
from Outcomes
where battle = 'Surigao Strait';

/*6*/
select name
from Ships
where class IN (
    select class
    from Classes
    where displacement >= 40000
);

/*7*/
select ship, displacement, numGuns
from Outcomes, Classes
where battle = 'Surigao Strait' AND class IN(
    select class
    from Ships
    where name = ship);

/*8*/
select name
from Ships;

/*9*/
select class
from Ships
group by class
having count(class) = 2;

/*10*/
select country
from Classes
group by country
having count(country) = 2;

/*11*/
select ship, result
from Outcomes
group by ship, result
having count(*) > 1;
