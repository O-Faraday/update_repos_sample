-- Customers without their personal columns.
select
    customer_id,
    upper(trim(country)) as country
from {{ source('shop', 'customers') }}
