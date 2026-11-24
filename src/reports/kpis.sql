-- The same revenue by country as src/reports/kpis.py, kept in SQL by another team.
CREATE OR REPLACE TABLE demo.update_repos_sample.revenue_by_country_sql AS
SELECT upper(trim(country)) AS country, sum(amount) AS revenue
FROM demo.update_repos_sample.orders_raw
GROUP BY upper(trim(country));
