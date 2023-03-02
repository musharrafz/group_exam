import psycopg2
from dotenv import load_dotenv
import os
load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv('DBNAME'),
    user=os.getenv('DBUSER'),
    password=str(os.getenv('DBPASS')),
    host=os.getenv('DBHOST')
)

cursor = conn.cursor()

cursor.execute("""
create table if not exists users(
    id serial primary key,
    user_id bigint not null,
    full_name varchar(255) not null,
    group_id bigint not null,
    group_name varchar(255) not null
);
""")
conn.commit()



def get_info_from_db(user_id: int) -> list:
    query = f"select * from users where user_id={user_id}"
    cursor.execute(query)
    lst = []
    for i in cursor.fetchall():
        lst.append(i)
    return lst

def update_data(data: list) -> None:
    cursor.execute("truncate users;")
    conn.commit()
    query = """insert into users(user_id, full_name, group_id, group_name) values(%s,%s,%s,%s);"""
    cursor.executemany(query,data)
    conn.commit()