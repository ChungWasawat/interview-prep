from utils.db_sqlalchemy import db_connect
import sqlalchemy

# `psql -U postgres` on sql shell
# `SELECT version();` on sql shell to see database version
eng, conn = db_connect()
"""-----------------------------------show information about database and table-----------------------------------"""
"""show tables or describe table's schema"""
# `\dt` on sql shell to list tables, `\l` to list database
#print(conn.execute(sqlalchemy.text(f"SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema';")).fetchall())
#print(conn.execute(sqlalchemy.text(f"SELECT * FROM information_schema.columns WHERE table_name = 'students';")).fetchall()[0])
#print(conn.execute(sqlalchemy.text(f"SELECT column_name, data_type, is_nullable FROM information_schema.columns WHERE table_name = 'courses';")).fetchall())
#print(conn.execute(sqlalchemy.text(f"SELECT * FROM information_schema.columns WHERE table_name = 'courses_attendance';")).fetchall()[0])
"""insert data"""
courses_table = sqlalchemy.Table("courses", sqlalchemy.MetaData(), autoload_with=eng)
conn.execute(courses_table.insert().values(course_id=5, course_name="Biology", credits=3))

conn.commit()
conn.close()