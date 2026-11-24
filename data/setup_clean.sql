-- Written to Databricks guidance: nothing here should be reported.
CREATE TABLE IF NOT EXISTS demo.update_repos_sample.orders_gold_clean (
  country STRING COMMENT 'Country code, upper case.',
  day DATE COMMENT 'Business day.',
  revenue DECIMAL(12, 2) COMMENT 'Sum of the order amounts.'
)
COMMENT 'Revenue by country and day (gold).'
CLUSTER BY (day);

CREATE OR REPLACE FUNCTION demo.update_repos_sample.country_code(country STRING)
  RETURNS STRING
  COMMENT 'Two-letter upper-case country code, NULL when empty.'
  RETURN nullif(upper(substr(trim(country), 1, 2)), '');
