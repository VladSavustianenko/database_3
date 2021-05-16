import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


origin_con = psycopg2.connect(
    database="laba1",
    user="postgres",
    password="admin"
)
origin_cur = origin_con.cursor()
origin_cur.execute("ROLLBACK")
origin_con.commit()


new_con = psycopg2.connect(
    user="postgres",
    password="admin"
)
new_con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
new_cur = new_con.cursor()
new_cur.execute("ROLLBACK")
new_con.commit()

new_db_name = "laba2"


def close_origin():
    origin_cur.close()
    origin_con.close()


def close_new():
    new_cur.close()
    new_con.close()

