-- Orders and revenue per day and country.
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
