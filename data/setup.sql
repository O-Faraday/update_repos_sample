-- Synthetic data of the sample project, in catalog `demo`, schema
-- `update_repos_sample`. Every row is invented. Run once, statement by
-- statement (see data/README.md). Re-running replaces the tables.
--
-- Left missing on purpose, to keep REF-001 cases: the vector index
-- policy_index, the endpoint sample-shipping-endpoint, and the tables the
-- notebooks create themselves (customer_contacts, events_clean).

CREATE SCHEMA IF NOT EXISTS demo.update_repos_sample;

CREATE VOLUME IF NOT EXISTS demo.update_repos_sample.raw;

-- Orders: no table or column comment (GOV-001).
CREATE OR REPLACE TABLE demo.update_repos_sample.orders_raw (
  order_id BIGINT,
  customer_id BIGINT,
  amount DECIMAL(10, 2),
  country STRING,
  order_ts TIMESTAMP
);

INSERT INTO demo.update_repos_sample.orders_raw VALUES
  (1001, 1, 25.40, 'FR', TIMESTAMP '2026-10-01 09:12:00'),
  (1002, 2, 180.00, 'DE', TIMESTAMP '2026-10-01 10:05:00'),
  (1003, 3, 72.15, 'fr ', TIMESTAMP '2026-10-02 14:30:00'),
  (1004, 1, 310.99, 'FR', TIMESTAMP '2026-10-03 08:45:00'),
  (1005, 4, 12.00, 'ES', TIMESTAMP '2026-10-03 17:20:00'),
  (1006, 5, 95.50, 'it', TIMESTAMP '2026-10-04 11:00:00'),
  (1007, 2, 45.00, 'DE', TIMESTAMP '2026-10-05 13:10:00'),
  (1008, 6, 220.00, 'BE', TIMESTAMP '2026-10-06 16:40:00');

-- Customers: personal columns. The email is masked by a function, the phone
-- is not (PII-001 on phone only).
CREATE OR REPLACE TABLE demo.update_repos_sample.customers (
  customer_id BIGINT COMMENT 'Customer key.',
  full_name STRING COMMENT 'Invented full name.',
  email STRING COMMENT 'Invented email address.',
  phone STRING COMMENT 'Invented phone number.',
  country STRING COMMENT 'Country code as entered.'
) COMMENT 'Customers of the sample shop (synthetic).';

INSERT INTO demo.update_repos_sample.customers VALUES
  (1, 'Alice Martin', 'alice.martin@example.invalid', '+33 6 00 00 00 01', 'FR'),
  (2, 'Bruno Keller', 'bruno.keller@example.invalid', '+49 151 0000002', 'DE'),
  (3, 'Chloe Petit', 'chloe.petit@example.invalid', '+33 6 00 00 00 03', 'fr '),
  (4, 'Diego Ruiz', 'diego.ruiz@example.invalid', '+34 600 000 004', 'ES'),
  (5, 'Elena Rossi', 'elena.rossi@example.invalid', '+39 300 000 0005', 'it'),
  (6, 'Femke Peeters', 'femke.peeters@example.invalid', '+32 470 00 00 06', 'BE');

-- Column mask: only the account group admins sees the full email.
CREATE OR REPLACE FUNCTION demo.update_repos_sample.mask_email(email STRING)
  RETURNS STRING
  COMMENT 'Column mask: hides the local part of an email outside the admins group.'
  RETURN CASE WHEN is_account_group_member('admins') THEN email
              ELSE regexp_replace(email, '^[^@]+', '***') END;

ALTER TABLE demo.update_repos_sample.customers
  ALTER COLUMN email SET MASK demo.update_repos_sample.mask_email;

-- Events: the source of src/ingest/stream_events.py.
CREATE OR REPLACE TABLE demo.update_repos_sample.events_raw (
  event_id BIGINT,
  customer_id BIGINT,
  event_type STRING,
  event_ts TIMESTAMP
) COMMENT 'Raw web events (synthetic).';

INSERT INTO demo.update_repos_sample.events_raw VALUES
  (1, 1, 'view', TIMESTAMP '2026-10-01 09:00:00'),
  (2, 1, 'cart', TIMESTAMP '2026-10-01 09:10:00'),
  (3, 2, 'view', TIMESTAMP '2026-10-01 10:00:00'),
  (4, 3, 'view', TIMESTAMP '2026-10-02 14:00:00'),
  (5, 3, 'purchase', TIMESTAMP '2026-10-02 14:30:00');

-- Policies: documented table and columns (no GOV-001), read by ai_query.
CREATE OR REPLACE TABLE demo.update_repos_sample.policies (
  policy_id INT COMMENT 'Policy key.',
  title STRING COMMENT 'Short title.',
  text STRING COMMENT 'Full text of the policy.'
) COMMENT 'Shop policies answered by the GenAI notebook (synthetic).';

INSERT INTO demo.update_repos_sample.policies VALUES
  (1, 'Refunds', 'Orders can be refunded within 30 days if the items are unused.'),
  (2, 'Shipping', 'Orders ship within 2 working days; delivery takes 3 to 5 days in Europe.'),
  (3, 'Privacy', 'Customer data is used only to process orders and is never sold.');

-- Functions: one documented SQL function, one Python function without comment.
CREATE OR REPLACE FUNCTION demo.update_repos_sample.amount_band(amount DECIMAL(10, 2))
  RETURNS STRING
  COMMENT 'Order size band: small under 50, medium under 200, large above.'
  RETURN CASE WHEN amount < 50 THEN 'small' WHEN amount < 200 THEN 'medium' ELSE 'large' END;

CREATE OR REPLACE FUNCTION demo.update_repos_sample.normalize_country(country STRING)
  RETURNS STRING
  LANGUAGE PYTHON
  AS $$
code = (country or "").strip().upper()
return code[:2] if code else None
$$;
