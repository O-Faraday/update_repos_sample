select country, sum(amount) as revenue
from {{ source('raw', 'orders') }}
group by country
