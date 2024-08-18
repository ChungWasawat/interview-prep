import os
from dotenv import load_dotenv

from faker import Faker
import random
from datetime import datetime, timedelta
from collections import OrderedDict

import pandas as pd
import duckdb

# constant variables
fake = Faker()
Faker.seed(42)
random.seed(42)

load_dotenv()
path = os.getenv("DATA_PATH", default="NaN")
dataset_path = f"{path}\\well\\"


def create_date(start_date:datetime, days:int) -> datetime:
    end_date = datetime(2023,12,31).date()

    date = fake.date_between_dates(start_date, start_date+timedelta(days=days) )
    if date <= end_date:
        return date
    else:
        return end_date


def create_well(well_dict:dict, well_n:int) -> dict:
    for i in range(1, well_n+1):
        well_dict['well_id'].append(i)
        well_dict['well_name'].append(fake.first_name_nonbinary())
        well_dict['location'].append(fake.city())
        well_dict['depth'].append(fake.random_int(min=20, max=40))

    return well_dict

def create_prod(production_dict:dict, production_n:int, well_n:int) -> dict:
    sdate = datetime(2023,1,1)

    i = 1
    while i < production_n+1:
        temp = create_date(sdate, 7)

        production_dict['production_id'].append(i)
        production_dict['production_date'].append( temp )
        production_dict['well_id'].append(random.randint(1, well_n))
        production_dict['oil_volume'].append( random.choices([0, 2, 4, 6, 8], weights = [70, 4, 3, 2, 1])[0] )
        production_dict['gas_volume'].append( random.choices([0, 2, 4, 6, 8], weights = [70, 4, 3, 2, 1])[0] )
        production_dict['water_volume'].append( random.choices([0, 2, 4, 6, 8], weights = [40, 7, 5, 3, 1])[0] )

        i+=1
        sdate = temp

    return production_dict

def create_eqm(equipment_dict:dict, equipment_n:int, well_n:int) -> dict:
    sdate = datetime(2023,1,1)

    for i in range(1, equipment_n+1):
        equipment_dict['equipment_id'].append(i)
        equipment_dict['equipment_type'].append(fake.random_choices(elements=OrderedDict([("a", 0.4), ("b", 0.4) , ("c", 0.2)]), length=1)[0] )
        equipment_dict['well_id'].append(random.randint(1, well_n))

        temp = create_date(sdate, 25)
        equipment_dict['installation_date'].append( temp )
        sdate = temp

    return equipment_dict

def create_mtn(maintenance_dict:dict, maintenance_n:int, equipment_n:int) -> dict:
    sdate = datetime(2023,4,1)

    for i in range(1, maintenance_n+1):
        maintenance_dict['maintenance_id'].append(i)
        maintenance_dict['equipment_id'].append(random.randint(1, equipment_n))
        maintenance_dict['description'].append(fake.sentence(nb_words=10))

        temp = create_date(sdate, 10)
        maintenance_dict['maintenance_date'].append( temp )
        sdate = temp

    return maintenance_dict

if __name__ == "__main__":
    well_row = 5
    prod_row = 60
    eqm_row = 20
    mtn_row = 45

    well_dict = {'well_id': [],  'well_name': [],  'location': [], 'depth': []}
    production_dict = {'production_id': [],  'well_id': [],  'production_date': [], 'oil_volume': [], 'gas_volume': [], 'water_volume': []}
    equipment_dict = {'equipment_id': [],  'equipment_type': [],  'installation_date': [], 'well_id': []}
    maintenance_dict = {'maintenance_id': [],  'equipment_id': [],  'maintenance_date': [], 'description': []}

    """create dataframe"""
    well_data = create_well(well_dict, well_row)
    df_well = pd.DataFrame(well_data)

    prod_data = create_prod(production_dict, prod_row, well_row)
    df_prod = pd.DataFrame(prod_data)

    eqm_data = create_eqm(equipment_dict, eqm_row, well_row)
    df_eqm = pd.DataFrame(eqm_data)

    mtn_data = create_mtn(maintenance_dict, mtn_row, eqm_row)
    df_mtn = pd.DataFrame(mtn_data)

    """write dataframe into files"""
    duckdb.sql("SELECT * FROM df_well").write_parquet(f"{dataset_path}well.parquet")
    duckdb.sql("SELECT * FROM df_prod").write_parquet(f"{dataset_path}production.parquet")
    duckdb.sql("SELECT * FROM df_eqm").write_parquet(f"{dataset_path}equipment.parquet")
    duckdb.sql("SELECT * FROM df_mtn").write_parquet(f"{dataset_path}maintenance.parquet")


