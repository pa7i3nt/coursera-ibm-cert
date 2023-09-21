#!/bin/sh

## Write your code here to load the data from sales_data table in Mysql server to a sales.csv.
## Select the data which is not more than 4 hours old from the current time.
mysql -u root -pNzI4NS1naWFuZ2Zu -e "select * from sales.sales_data where timestamp >= DATE_SUB(NOW(), INTERVAL 4 HOUR);" | tr '\t' ',' > sales.csv

 export PGPASSWORD=Mjk3ODEtZ2lhbmdm;

psql --username=postgres --host=localhost --dbname=sales_new -c "truncate table dimdate; truncate table sales_data; truncate table factsales;"

 psql --username=postgres --host=localhost --dbname=sales_new -c "\COPY sales_data(rowid,product_id,customer_id,price,quantity,timestamp) FROM '/home/project/sales.csv' delimiter ',' csv header;" 

 ## Delete sales.csv present in location /home/project

rm sales.csv

 ## Write your code here to load the DimDate table from the data present in sales_data table

 psql --username=postgres --host=localhost --dbname=sales_new -c  "INSERT INTO DimDate (SELECT dateid,EXTRACT(day from timestamp),EXTRACT(month from timestamp),EXTRACT(year from timestamp) FROM sales_data);" 

## Write your code here to load the FactSales table from the data present in sales_data table

psql --username=postgres --host=localhost --dbname=sales_new -c  "INSERT INTO FactSales (SELECT rowid,product_id,customer_id,price,price*quantity FROM sales_data);"

 ## Write your code here to export DimDate table to a csv

 psql --username=postgres --host=localhost --dbname=sales_new -c "\COPY DimDate TO '/home/project/DimDate.csv' DELIMITER ',' CSV HEADER;"

 ## Write your code here to export FactSales table to a csv
 
 psql --username=postgres --host=localhost --dbname=sales_new -c "\COPY FactSales TO '/home/project/FactSales.csv' DELIMITER ',' CSV HEADER;"
