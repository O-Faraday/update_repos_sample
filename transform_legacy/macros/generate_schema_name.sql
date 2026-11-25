{#- Uses the custom schema as is, without the target schema (DBT-007): where the models land depends on
    this macro, not on dbt's default naming. -#}
{% macro generate_schema_name(custom_schema_name, node) -%}
    {%- if custom_schema_name is none -%}{{ target.schema }}{%- else -%}{{ custom_schema_name | trim }}{%- endif -%}
{%- endmacro %}
