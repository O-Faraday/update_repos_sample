-- Merged without unique_key: a re-run of the same day adds its rows again (DBT-002). No test (DBT-003).
{{ config(materialized='incremental', incremental_strategy='merge') }}
select
    order_date,
    country,
    count(*) as orders,
    sum(amount) as revenue
from {{ ref('stg_orders') }}
{% if is_incremental() %}
where order_date >= (select max(order_date) from {{ this }})
{% endif %}
group by order_date, country
