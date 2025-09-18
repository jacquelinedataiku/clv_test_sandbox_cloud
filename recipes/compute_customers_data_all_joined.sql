SELECT 
    "customers_data_prepared"."customer_id" AS "customer_id",
    "customers_data_prepared"."age" AS "age",
    "customers_data_prepared"."price_first_item_purchased" AS "price_first_item_purchased",
    "customers_data_prepared"."gender" AS "gender",
    "customers_data_prepared"."revenue" AS "revenue",
    "customers_data_prepared"."original_dataset" AS "original_dataset",
    "web_data_prepared"."ip" AS "ip",
    "web_data_prepared"."ip_geopoint" AS "ip_geopoint",
    "web_data_prepared"."ip_country_code" AS "ip_country_code",
    "web_data_prepared"."pages_visited" AS "pages_visited",
    "web_data_prepared"."campain" AS "campain",
    "web_data_prepared"."is_id_ends_d" AS "is_id_ends_d"
  FROM "PUBLIC"."node-093312e5_SC_CLV_GOVERN_EXAMPLE_CUSTOMERS_DATA_PREPARED" "customers_data_prepared"
  INNER JOIN "PUBLIC"."node-093312e5_SC_CLV_GOVERN_EXAMPLE_WEB_DATA_PREPARED" "web_data_prepared"
    ON "customers_data_prepared"."customer_id" = "web_data_prepared"."customer_id"
  
  WHERE "web_data_prepared"."ip_country_code" = '${country_code_var}'