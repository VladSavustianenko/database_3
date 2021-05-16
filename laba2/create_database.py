import psycopg2
import config


def create_database():
    try:
        config.new_cur.execute(f"CREATE DATABASE {config.new_db_name}")
        config.new_con.commit()
        print(f"Database {config.new_db_name} created!\n")

        config.close_new()
        config.new_con = psycopg2.connect(
            database=config.new_db_name,
            user="postgres",
            password="admin"
        )
        config.new_cur = config.new_con.cursor()
        config.new_cur.execute("ROLLBACK")
        config.new_con.commit()
    except:
        config.new_con.commit()
        config.close_new()
        print(f"Database {config.new_db_name} already exist\n")

        config.new_con = psycopg2.connect(
            database=config.new_db_name,
            user="postgres",
            password="admin"
        )
        config.new_cur = config.new_con.cursor()
        config.new_cur.execute("ROLLBACK")
        config.new_con.commit()


def create_exam_table():
    try:
        config.new_cur.execute(
            f"CREATE TABLE Exam ("
            f"exam_id integer NOT NULL,"
            f"out_id character varying,"
            f"year integer,"
            f"test character varying,"
            f"pt_name character varying,"
            f"location_id integer,"
            f"lang character varying,"
            f"test_status character varying,"
            f"dpa_level character varying,"
            f"adapt_scale integer,"
            f"ball_100 integer,"
            f"ball_12 integer,"
            f"ball integer,"
            f"constraint PK_EXAM primary key (exam_id)"
            f")"
        )
        config.new_con.commit()
        print(f"Table Exam created!")
    except:
        config.new_con.commit()
        print(f"Table Exam already exist")


def create_location_table():
    try:
        config.new_cur.execute(
            f"CREATE TABLE Location ("
            f"location_id integer NOT NULL,"
            f"reg_name character varying,"
            f"area_name character varying,"
            f"ter_name character varying,"
            f"ter_type_name character varying,"
            f"constraint PK_LOCATION primary key (location_id)"
            f")"
        )
        config.new_con.commit()
        print(f"Table Location created!")
    except:
        config.new_con.commit()
        print(f"Table Location already exist")


def create_school_table():
    try:
        config.new_cur.execute(
            f"CREATE TABLE School ("
            f"school_id integer NOT NULL,"
            f"eo_name character varying,"
            f"eo_type_name character varying,"
            f"location_id integer,"
            f"eo_parent character varying,"
            f"constraint PK_SCHOOL primary key (school_id)"
            f")"
        )
        config.new_con.commit()
        print(f"Table School created!")
    except:
        config.new_con.commit()
        print(f"Table School already exist")


def create_student_table():
    try:
        config.new_cur.execute(
            f"CREATE TABLE Student ("
            f"out_id character varying NOT NULL,"
            f"birth integer,"
            f"sex_type_name character varying,"
            f"reg_type_name character varying,"
            f"class_profile_name character varying,"
            f"constraint PK_Student primary key (out_id)"
            f")"
        )
        config.new_con.commit()
        print(f"Table Student created!")
    except:
        config.new_con.commit()
        print(f"Table Student already exist")


def create():
    create_database()

    create_exam_table()
    create_location_table()
    create_school_table()
    create_student_table()
