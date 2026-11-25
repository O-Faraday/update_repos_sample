-- Reads the customers table by its name, not through source() (DBT-001). No test (DBT-003).
select
    c.customer_id,
    c.country,
    count(o.order_id) as orders,
    sum(o.amount) as revenue
from demo.update_repos_sample.customers c
left join {{ ref('stg_orders') }} o on o.customer_id = c.customer_id
group by c.customer_id, c.country
