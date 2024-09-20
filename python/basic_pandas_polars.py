import os
from dotenv import load_dotenv

import pandas as pd
import polars as pl
import datetime

#https://www.rhosignal.com/posts/polars-pandas-cheatsheet/

"""-------------------------------------------------variables-------------------------------------------------"""
load_dotenv()
path = os.getenv("STUDENT_DATA_PATH", default="NaN")
student_csv = f"{path}\\student.csv"
student_parquet = f"{path}\\student.parquet"

"""find more information about command"""
#print(help(pd.Series.loc))
"""Series"""
s_pd = pd.Series([3, -5, 7, 4],  index=['a',  'b',  'c',  'd'])
s_pd2 = pd.Series([7, -2, 3],  index=['a',  'c',  'd'])
#print(s_pd['b'])
#print(s_pd[(s_pd < -1) | (s_pd > 2)])
s_pdo = s_pd.drop(['a',  'c'])

"""-------------------------------------------------Arithmetic Operations-------------------------------------------------"""
#print(s_pd + s_pd2)                    #only show shared columns
#print(s_pd.add(s_pd2, fill_value=0))
#print(s_pd.sub(s_pd2, fill_value=2))
#print(s_pd.div(s_pd2, fill_value=4))
#print(s_pd.mul(s_pd2, fill_value=3))

"""-------------------------------------------------DataFrame-------------------------------------------------"""
data = {'Country': ['Belgium',  'India',  'Brazil', 'Ghana', 'India'],
        'Capital': ['Brussels',  'New Delhi',  'Brasilia', 'Accra', None],
        'Continent': ['Europe',  'Asia',  'South America', 'Africa', 'Asia'],
        'Population': [11190846, 1303171035, 207847528, 5062000, 155555555],
        'Area': [15595488, 545484631, 548494777, 77411222, 789634848]} 

data2 = {
        '1': {'Country': 'China', 'Capital':'Shanghai', 'Continent': 'Asia', 'Population': 34342334543, 'Area': 55554518},
        '2': {'Country': 'Australia', 'Capital': 'Canberra', 'Continent': 'Oceania', 'Population': 151648349, 'Area': 978745325 }
    }
       
data2_converted = [val for val in data2.values()]

df_pd = pd.DataFrame(data)
df_pd2 = pd.DataFrame.from_dict(data2, orient='index')

df_pl = pl.DataFrame(data)
df_pl2 = pl.DataFrame(data2_converted)
df_pl2 = pl.from_dicts(data2_converted)

"""-------------------------------------------------data profiling-------------------------------------------------"""
# pandas
#print(df_pd.head(5))
#print(df_pd.tail(5))
#print(df_pd.shape)
#print(df_pd.index)
#print(df_pd.columns)
#print(df_pd.info())
#print(df_pd.count())
#print(df_pd.describe())
#print(df_pd.drop_duplicates())
# polars
#print(df_pl.head(n=5))
#print(df_pl.tail(n=5))
#print(df_pl.shape)
#print(df_pl.unique())                  #show unique rows

"""-------------------------------------------------basic agg function-------------------------------------------------"""
# pandas
#print(df_pd['Country'].sum(skipna=True))
#print(df_pd['Population'].cumsum(axis=0))
#print(df_pd['Population'].min()/df_pd['Population'].max())
#print(df_pd['Population'].mean())
#print(df_pd.groupby(by=['Continent'])['Area'].mean())
# polars
#print(df_pl.sum())
#print(df_pl.select( [  pl.sum("Area").alias("sum_area"), ]) )
#print(df_pl['Population'].min()/df_pl['Population'].max())
#print(df_pl['Population'].mean())
#print(df_pl)
#print(df_pl.group_by(by='Continent').agg( [ pl.mean('Area').alias("Area_mean")] ))

"""-------------------------------------------------dataframe manipulation-------------------------------------------------"""
# pandas
df_pdc = df_pd.copy()
df_pdc.rename(columns={"Country":"Countries"}, inplace=True)
df_pdo = pd.concat([df_pd,df_pd2])
df_pdo = pd.pivot_table(df_pd, values='Population', index=['Continent'], columns=['Area'], aggfunc="sum", fill_value=0)
df_pdo = df_pd.drop('Country', axis=1) 
df_pdo = df_pd.dropna()
df_pdo = df_pd["Capital"].fillna("Missed data") #fillna(value={"col1":0, "col2":2}, axis=1)
df_pdc['multiplied_result'] = df_pdc['Population'] * df_pdc['Area']
# polars
df_plc = df_pl.clone()
df_plc = df_plc.rename({"Country":"Countries"})
df_plo = pl.concat([df_pl, df_pl2])
df_plo = df_pl.pivot( "Area", index="Continent", values="Population", aggregate_function="sum",)
df_plo = df_pl.drop('Country')
df_plo = df_pl.with_columns([(pl.col('Population') * pl.col('Area')).alias('multiplied_result')])

"""-------------------------------------------------selecting-------------------------------------------------"""
# pandas
#print(df_pd[1:])
#print(df_pd.iloc([0], [0]))            #return 'Belgium'
#print(df_pd.at([0],  ['Country']))     #return 'Belgium'
# polars
#print(df_pl.sample(frac=0.5))
#print(df_pl[1:])
#print(df_pl[1:, :2])

"""-------------------------------------------------change datatype-------------------------------------------------"""
# pandas
df_pd2[["Population"]] = df_pd2[["Population"]].astype(float)
# polars
df_pl2[["Population"]] = df_pl2.select(pl.col("Population").cast(pl.Float64))

"""-------------------------------------------------filtering-------------------------------------------------"""
# pandas
#print(df_pd[df_pd['Population']>1200000000])
# polars
#print(df_pl.filter((pl.col("Population") >1200000000 ) | (pl.col("Country") == "Belgium")))
#print(df_pl.select(pl.col(pl.INTEGER_DTYPES).exclude('Area')))

"""-------------------------------------------------sorting-------------------------------------------------"""
# pandas
#print(df_pd.sort_index())
#print(df_pd.sort_values(by='Country') )
#print(df_pd.rank())
# polars
#print(df_pl.sort('Country'))
#print(df_pl.with_row_index())

"""-------------------------------------------------lambda-------------------------------------------------"""
# pandas
f = lambda x: x*2
df_pdo = df_pd.apply(f)
#df_pdxx = df_pd.applymap(f)            #need all columns to be int?
# polars
df_plo = df_pl.select(
    pl.struct(["Population", "Area"])
    .map_elements(lambda x: x["Population"] + x["Area"], return_dtype=pl.Int64)
    .alias("Test_Lambda"),
    (pl.col("Population") + pl.col("Area")).alias("Normal_operation"),
)

"""-------------------------------------------------read/ write data-------------------------------------------------"""
# read more about excel file manipulation
"""csv"""
# pandas
#df_pd = pd.read_csv(f"{student_csv}", header=None, nrows=5)
#df_pd.to_csv(f"{path}\\student_test_pd.csv")
# polars
#df_pl = pl.read_csv(f"{student_csv}", has_header=True)
#df_pl.write_csv(f"{path}\\student_test_pl.csv")
"""parquet"""
#pandas
#df_pd = pd.read_parquet(f"{student_parquet}")
#df_pd.to_parquet(f"{path}\\student_test_pd.parquet")
#polars
#df_pl = pl.read_parquet(f"{student_parquet}")
#df_pl.write_parquet(f"{path}\\student_test_pl.parquet")
"""sql"""
from py_modules.db import db_connect
import sqlalchemy
from dateutil.relativedelta import relativedelta

def compute_age(date_of_birth):
    return relativedelta(datetime.date.today(), date_of_birth).years

eng, conn = db_connect()
student = conn.execute(sqlalchemy.text(f"select * from students")).fetchall()
course = conn.execute(sqlalchemy.text(f"select * from courses")).fetchall()
course_att = conn.execute(sqlalchemy.text(f"select * from courses_attendance")).fetchall()
conn.close()
#pandas
pd_student = pd.DataFrame(student)
pd_course = pd.DataFrame(course)
pd_course_att = pd.read_sql("select * from courses_attendance", eng)
merged_pd_course = pd_course_att.merge(pd_course, how="left", left_on="course_id", right_on="course_id")
# computing age from this one is a little complicated, 
#pd_student_age1 = datetime.date.today() - pd_student['date_of_birth']
# timestamp doesn't work with date and .strftime("%d %m %Y") make it string so still doesn't work with date
#pd_student_age2 = datetime.datetime.now() - pd_student['date_of_birth'] 
pd_student['age'] = pd_student['date_of_birth'].apply(compute_age)
#polars
pl_student = pl.from_pandas(pd_student)
#pl_course = pl.DataFrame(course ,orient="row")
pl_course = pl.from_pandas(pd_course)
pl_course_att = pl.read_database(query="SELECT * FROM courses_attendance",connection=eng,)  
merged_pl_course = pl_course_att.join(pl_course, on="course_id", how="left")
pl_student = pl_student.with_columns(pl.col("date_of_birth").map_elements(compute_age, return_dtype=pl.Int64).alias("age2"))
"""api"""
import requests
#1
#pandas
url_currency = "https://r2de3-currency-api-vmftiryt6q-as.a.run.app/gbp_thb" #list of dicts
# convert http request to json
result_conversion_rate = requests.get(url_currency).json()
conversion_rate = pd.DataFrame(result_conversion_rate)
conversion_rate = conversion_rate.drop(columns=['id'])
conversion_rate['date'] = pd.to_datetime(conversion_rate['date'])
#polars
conversion_rate_pl = pl.DataFrame(result_conversion_rate)
conversion_rate_pl = conversion_rate_pl.drop('id')
conversion_rate_pl = conversion_rate_pl.with_columns( pl.col("date").str.to_datetime(format="%Y-%m-%d") )


"""-------------------------------------------------datetime-------------------------------------------------"""
d_date = {'date': {0: '28-01-2022  5:25:00',
  1: '27-02-2022  6:25:00',
  2: '30-03-2022  7:25:00',
  3: '29-04-2022  8:25:00',
  4: '31-05-2022  9:25:00'},
 'date_short': {0: 'Jan-2022', 1: 'Feb-2022', 2: 'Mar-2022', 3: 'Apr-2022', 4: 'May-2022'},
 'unixtime': {0 : 1643365500, 1: 1645961100, 2: 1648643100, 3: 1651238700, 4: 1654007100 }}
#pandas
df_pd = pd.DataFrame(d_date)
#df_pd['date'] = pd.to_datetime(df_pd['date'], format='%d-%m-%Y %H:%M:%S')
df_pd['date'] = df_pd['date'].astype('datetime64[ns]')
df_pd['unixtime'] = pd.to_datetime(df_pd['unixtime'], unit="s")
#polars
d_date_converted = {key: list(val.values()) for key, val in d_date.items()}
df_pl = pl.DataFrame(d_date_converted)
df_pl = df_pl.with_columns( pl.col("date").str.to_datetime(format="%d-%m-%Y %H:%M:%S") )
df_pl = df_pl.with_columns( pl.from_epoch(pl.col('unixtime')) )
