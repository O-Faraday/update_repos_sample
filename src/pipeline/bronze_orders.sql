-- Bronze orders, no expectation on the rows.
CREATE OR REFRESH STREAMING TABLE orders_bronze
AS SELECT * FROM STREAM read_files('/Volumes/main/update_repos_sample/raw/orders', format => 'csv');
