-- Written to the guidance: merged on its key, tested, reads through ref().
{{ config(materialized='incremental', incremental_strategy='merge', unique_key='order_id') }}
select
    o.order_id,
    o.customer_id,
    c.country,
    o.amount,
    o.order_date
from {{ ref('stg_orders') }} o
join {{ ref('stg_customers') }} c on c.customer_id = o.customer_id
{% if is_incremental() %}
where o.order_date >= (select max(order_date) from {{ this }})
{% endif %}
