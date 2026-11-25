-- Orders as received, with a clean country code.
select
    order_id,
    customer_id,
    amount,
    upper(trim(country)) as country,
    order_ts,
    cast(order_ts as date) as order_date
from {{ source('raw', 'orders') }}
