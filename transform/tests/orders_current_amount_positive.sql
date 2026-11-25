-- Singular test: no order with a negative amount.
select order_id from {{ ref('orders_current') }} where amount < 0
