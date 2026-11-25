-- Written to the guidance: reads through ref(), merged on its key, tested (marts.yml).
{{ config(materialized='incremental', incremental_strategy='merge', unique_key='customer_id') }}
select
    c.customer_id,
    c.country,
    count(o.order_id) as orders,
    sum(o.amount) as revenue
from {{ ref('stg_customers') }} c
left join {{ ref('stg_orders') }} o on o.customer_id = c.customer_id
group by c.customer_id, c.country
