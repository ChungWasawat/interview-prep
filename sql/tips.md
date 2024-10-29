# Tips
## Creating dashboard  
* Scenario: You are designing a data set for a dashboard. The dashboard should be able to show metrics at **day, week, month, and year** levels (assume these are drop-downs on the dashboard).
* __Question 1__: What clarifying questions would you ask the dashboard team? [Answer from Joseph Machado](https://github.com/josephmachado/adv_data_transformation_in_sql/blob/main/concepts/query_templates/workshop_solutions.ipynb)
1. Metrics Scope:
    * What **specific metrics** are required to be displayed on the dashboard (e.g., sales, revenue, number of orders, user sign-ups, etc.)?
2. Filtering and Segmentation:
    * Will the dashboard **require filtering or segmentation based on dimensions** like region, product category, user demographics, etc.?
    * Are there **any drill-down** capabilities (e.g., from year to quarter to month) that need to be supported?
3. Performance Requirements:
    * What are the **performance expectations** for the dashboard (e.g., should the data load in <ins>real-time, or is some delay acceptable</ins>)?
    * How **often will the data be refreshed** (real-time, hourly, daily, etc.)?
4. Historical Data:
    * **How much historical data needs** to be maintained and made available on the dashboard?
5. Visualization Requirements:
    * Are there **any specific visualization requirements or preferences** that <ins>might affect how the data is structured</ins> (e.g., time series charts, heatmaps, etc.)?
6. Data Volume and Scalability:
    * What is **the expected data volume**, and do you foresee this data volume <ins>growing significantly over time</ins>?
    * Should the design **account for scalability** to handle increasing data volume or additional metrics in the future?
* __Question 2__: How would you design the table to be used by the dashboard software? What are the considerations you need to be mindful of? [Answer from Joseph Machado](https://github.com/josephmachado/adv_data_transformation_in_sql/blob/main/concepts/query_templates/workshop_solutions.ipynb)   
**Table Design:**
1. Fact Table Structure:
    * Granularity: **Design a fact table at the finest level** of granularity required, such as <ins>daily transactions or events</ins>. This allows for flexible aggregation at higher levels (weekly, monthly, yearly) as needed.
    * Date Dimension: **Include a date_key foreign key** that links to a date dimension table. This date dimension should include columns for the day, week, month, quarter, and year to facilitate easy aggregation.
    * Metrics Columns: Include **columns for each metric required by the dashboard**, such as total_sales, total_orders, total_revenue, etc.
2. Date Dimension Table:
    * Date Hierarchy: Design the date dimension table to **include columns like date, day_of_week, week_of_year, month, quarter, and year**.
    * Fiscal Calendar: If the organization uses a <ins>fiscal calendar</ins>, **include fiscal year, fiscal quarter, and fiscal month columns**.
    * Special Dates: Include **flags or indicators for holidays, weekends, or other significant dates** that might affect metrics.
3. Pre-Aggregation and Summary Tables:
    * Aggregated Tables: Consider **creating pre-aggregated summary tables at the weekly, monthly, and yearly** levels to improve query performance on the dashboard. These tables can be <ins>refreshed periodically</ins>.
    * Partitioning: **Partition the data by date, week, or month** to optimize query performance and manage large data volumes efficiently.
4. Partitions and Optimization:
    * Partitions: **Create appropriate partitions on commonly queried columns**, such as date_key, order_id, and customer_id, to improve query performance. !!!Index columns help to speed up query performance
    * Materialized Views: If the database supports **materialized views**, consider using them to store pre-computed aggregates that are frequently accessed. 
5. Handling Historical Data:
    * Data Retention: Implement a **data retention** strategy that <ins>balances performance and storage costs</ins>. For example, keep detailed daily data for the most recent years and aggregate older data.
    * Archiving: **Archive historical data** that is no longer required for the dashboard but may need to be retained for compliance or historical analysis. !!!Cold storage?
6. Data Quality and Validation:
    * Data Integrity: **Ensure referential integrity between the fact and dimension tables**.
    * Validation Checks: Implement **data validation** checks to ensure accuracy, such as <ins>verifying that totals match expected values and that all dates are populated in the date dimension</ins>.

**Considerations:**   
1. Performance: The design should ensure that queries run quickly, even as data volume grows. <ins>Pre-aggregated tables, partitioning, and indexing are critical considerations</ins>.
2. Scalability: The design should be scalable to <ins>handle increasing data volumes and the addition of new metrics or dimensions in the future</ins>.
3. Flexibility: The table design should be flexible enough to <ins>support different levels of granularity</ins> and the ability to drill down from year to quarter to month to day.
4. Data Refresh: Ensure that the data refresh process is efficient and that the dashboard <ins>displays up-to-date information based on the refresh frequency</ins>.
5. User Experience: Design the data structure to support a smooth and responsive user experience on the dashboard, <ins>with minimal delays when switching between different views (day, week, month, year)</ins>.

## Steps to dissect legacy SQL
1. Understand the input data sets, what they mean, and who/what generates them, and speak to the people who created the tables that your queries use.
2. Speak with the stakeholders using the data, what metrics they are typically looking at, Understand the metric distribution over time, what the purpose of this query (if they know) is & how they use the query results.
3. Speak with your manager to identify the use case for the query and a general idea about the data sets used (and the warehouse data model) and how the stakeholders use the output.