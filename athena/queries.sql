-- Create external table
CREATE EXTERNAL TABLE ride_data (
    city STRING,
    total_revenue DOUBLE,
    total_rides INT,
    avg_fare DOUBLE
)
PARTITIONED BY (year INT, month INT)
STORED AS PARQUET
LOCATION 's3://your-bucket-name/processed/ride_data/';

-- Load partitions
MSCK REPAIR TABLE ride_data;

-- Top cities by revenue
SELECT city, SUM(total_revenue) AS revenue
FROM ride_data
GROUP BY city
ORDER BY revenue DESC;

-- Monthly ride trends
SELECT year, month, SUM(total_rides) AS rides
FROM ride_data
GROUP BY year, month
ORDER BY year, month;

-- Average fare by city
SELECT city, AVG(avg_fare) AS avg_fare
FROM ride_data
GROUP BY city;
