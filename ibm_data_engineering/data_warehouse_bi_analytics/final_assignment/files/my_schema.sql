CREATE TABLE MyDimDate (
    date_id INT PRIMARY KEY NOT NULL,
    year INT
    month TINYINT,
    month_name VARCHAR(9),
    quarter TINYINT,
    quarter_name VARCHAR(2),
    day TINYINT,
    weekday TINYINT,
    weekday_name VARCHAR(9)
);

CREATE TABLE MyDimWaste (
    waste_type_id INT PRIMARY KEY NOT NULL,
    waste_type VARCHAR(10) NOT NULL
);


CREATE TABLE MyDimZone (
    zone_id INT PRIMARY KEY NOT NULL,
    zone_name VARCHAR(7) NOT NULL,
    city VARCHAR(14) NOT NULL
);


CREATE TABLE MyFactTrips (
    trip_id INT PRIMARY KEY NOT NULL,
    date_id INT REFERENCES MyDimDate(date_id)
    waste_type_id INT REFERENCES MyDimWaster(waste_id),
    zone_id INT REFERENCES MyDimZone(zone_id),
    waste_collected FLOAT
);
