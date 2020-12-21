PRAGMA foreign_keys = on;

create table Classes(
    class varchar(32) PRIMARY KEY,
    type varchar(2),  
    country varchar(32) NOT NULL,
    numGuns integer,
    bore integer,
    displacement integer,
    CHECK(type IN ('bb', 'bc'))
); 

create table Ships(
    name varchar(32) PRIMARY KEY,
    class varchar(32) NOT NULL,
    launched integer,
    FOREIGN KEY(class) REFERENCES Classes(class) ON DELETE CASCADE ON UPDATE CASCADE   
);

create table Battles(
    name varchar(32) PRIMARY KEY,
    date text
);

create table Outcomes(
    ship varchar(32) REFERENCES Ships(name) ON DELETE SET NULL ON UPDATE SET NULL,
    battle varchar(32) REFERENCES Battles(name) ON DELETE CASCADE ON UPDATE CASCADE,
    result varchar(32),
    CHECK(result In ('ok','sunk','damaged'))
);

-- #1 --
insert into Classes (class, type, country, numGuns, bore, displacement)
values ('Bismarck', 'bb', 'Germany', 8, 15, 42000),
        ('Iowa', 'bb', 'USA', 9, 16, 46000),
        ('Kongo', 'bc', 'Japan', 8, 14, 32000),
        ('North Carolina', 'bb', 'USA', 9, 16, 37000),
        ('Renown', 'bc', 'Britain',6, 15, 32000),
        ('Revenge', 'bb', 'Britain', 8, 15, 29000),
        ('Tennessee', 'bb', 'USA', 12, 14, 32000),
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

-- #2 --
DELETE FROM Classes 
WHERE displacement > 50000 OR 
        numGuns > 10;

-- #3 --
-- How can this be automated?? --
-- I tried to use JOIN variations, but no success --
insert into Classes (class, type, country, numGuns, bore, displacement)
values ('Missouri', 'bb', 'USA', 9, 16, 46000),
        ('New Jersey', 'bb', 'USA', 9, 16, 46000),
        ('Wisconsin', 'bb', 'USA', 9, 16, 46000),
        ('Washington', 'bb', 'USA', 9, 16, 37000),
        ('California', 'bb', 'USA', 12, 14, 32000);

UPDATE Ships 
SET class = 'California'
WHERE name = 'California';

UPDATE Ships 
SET class = 'Washington'
WHERE name = 'Washington';

UPDATE Ships 
SET class = 'New Jersey'
WHERE name = 'New Jersey';

UPDATE Ships 
SET class = 'Missouri'
WHERE name = 'Missouri';

UPDATE Ships 
SET class = 'Winsconsin'
WHERE name = 'Winsconsin';

-- #4 --
DELETE FROM Battles 
WHERE name = 'North Cape';

-- #5 --
UPDATE Battles
SET name = 'North Cape'
WHERE name = 'Guadalcanal';

-- #6 --
UPDATE Battles
SET name = 'Strait of Surigao' 
WHERE name = 'Surigao Strait';

-- #7 --
DELETE FROM Ships
WHERE class IN (SELECT class 
                FROM Ships
                GROUP BY class
                having count(class) > 4);
-- #8 --
SELECT *
FROM Ships;

-- #9 --
SELECT * 
FROM Outcomes;
