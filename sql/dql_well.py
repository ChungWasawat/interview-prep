"""
use duckdb as sql
"""
import os
from dotenv import load_dotenv

import duckdb

#variables
load_dotenv()
path = os.getenv("WELL_DATA_PATH", default="NaN")
well_path = f"{path}\\well.parquet"
prod_path = f"{path}\\production.parquet"
eqm_path = f"{path}\\equipment.parquet"
mtn_path = f"{path}\\maintenance.parquet"

# q1
q1 = duckdb.sql(f"select well_name,                     \
                    sum(oil_volume) as total_oil,       \
                    sum(gas_volume) as total_gas,       \
                    sum(water_volume) as total_water,   \
                    total_oil+total_gas+total_water as total_prod   \
                from '{well_path}' w                    \
                join '{prod_path}' p                    \
                on w.well_id = p.well_id                \
                where extract('year' FROM production_date) = 2023 and   \
                    extract('month' FROM production_date) = 7   \
                group by well_name                      \
                ")                  
#print(q1)

# q2
q2 = duckdb.sql(f"select w.well_id, well_name,  \
                from '{well_path}' w            \
                left join '{prod_path}' p       \
                on w.well_id = p.well_id        \
                where extract('year' FROM production_date) = 2023   \
                group by 1, 2                   \
                having sum(gas_volume) =0")
#print(q2)

# q3
q3 = duckdb.sql(f"select well_name, equipment_type, description     \
                from '{well_path}' w            \
                inner join '{eqm_path}' e       \
                on w.well_id = e.well_id        \
                inner join '{mtn_path}' m       \
                on e.equipment_id = m.equipment_id      \
                where extract('month' FROM maintenance_date) = 7    \
                order by 1, 2 ")          
#print(q3)

# q4
q4 = duckdb.sql(f"select well_name,             \
                    round( avg(oil_volume), 2)  as average_daily_oil    \
                from '{well_path}' w            \
                left join '{prod_path}' p       \
                on w.well_id = p.well_id        \
                where location = 'Lake Joshuabury'  \
                group by well_name              \
                ")
#print(q4)

# q5 use preceding, following
q5 = duckdb.sql(f"select well_name, production_date, water_volume,      \
                sum(water_volume) over (partition by w.well_id order by production_date rows between 1 preceding and current row) as current_and_prev1, \
                sum(water_volume) over (partition by w.well_id order by production_date rows between 1 preceding and 1 following) as prev1_and_next1    \
                from '{well_path}' w                                    \
                left join '{prod_path}' p on w.well_id = p.well_id      \
                order by w.well_id, production_date")                
# print(q5)

# q6 use unbounded instead of number before preceding/ following
q6 = duckdb.sql(f"select well_name, production_date, water_volume,      \
                max(water_volume) over (partition by w.well_id order by production_date rows unbounded preceding) as past_max_water_prod    \
                from '{well_path}' w                                    \
                left join '{prod_path}' p on w.well_id = p.well_id      \
                order by w.well_id, production_date ")  
#print(q6)

# q7
q7 = duckdb.sql(f"select strftime(production_date, '%Y-%m-01')          \
                from '{prod_path}'")
q7_5 = duckdb.sql(f"select well_id, cast(production_date as date), cast(prev_prod as date)              \
                from ( select well_id, production_date,                 \
                lag(production_date) over (partition by well_id order by production_date) as prev_prod  \
                from '{prod_path}' )                                    \
                where production_date - prev_prod > 3 ") 
# it should be "interval 5 day" instead of 5 if the result reture interval, not bigint
# so I can use 'range between interval 3 day preceding and interval 3 day following'
print(q7_5)

