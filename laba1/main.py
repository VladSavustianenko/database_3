import csv
import re
import psycopg2

con = psycopg2.connect(
    database="laba1",
    user="postgres",
    password="admin"
)

cur = con.cursor()
cur.execute("ROLLBACK")
con.commit()


pattern_mark = re.compile(r'^\d+,\d+$')
pattern_file = re.compile(r'\d{4}')
first_file_name = 'Odata2019File.csv'
second_file_name = 'Odata2020File.csv'
query_file_name = 'Query.csv'


subjects = [
    ['Ukr', 'Українська мова і література'],
    ['Hist', 'Історія України'],
    ['Math', 'Математика'],
    ['Phys', 'Фізика'],
    ['Chem', 'Хімія'],
    ['Bio', 'Біологія'],
    ['Geo', 'Географія'],
    ['Eng', 'Англійська мова'],
    ['Fr', 'Французька мова'],
    ['Deu', 'Німецька мова'],
    ['Sp', 'Іспанська мова'],
]

participants_data = []
exams = []
participant_id = 1
exam_id = 1


def get_subject_name(elem):
    for i in range(len(subjects)):
        if subjects[i][1] == elem:
            return subjects[i][0]


def convert_to_float(elem):
    try:
        return float(elem)
    except:
        return elem


def convert_to_int(elem):
    try:
        return int(elem)
    except:
        return elem


def create_participant_data_table():
    try:
        cur.execute(
            f"CREATE TABLE public.participant_data"
            f"("
            "id integer NOT NULL,"
            "year integer,"
            f"participant_id character varying COLLATE pg_catalog.{'default'} NOT NULL,"
            f"birth integer,"
            f"sex_type_name character varying COLLATE pg_catalog.{'default'},"
            f"reg_name character varying COLLATE pg_catalog.{'default'},"
            f"area_name character varying COLLATE pg_catalog.{'default'},"
            f"ter_name character varying COLLATE pg_catalog.{'default'},"
            f"reg_type_name character varying COLLATE pg_catalog.{'default'},"
            f"ter_type_name character varying COLLATE pg_catalog.{'default'},"
            f"class_profile_name character varying COLLATE pg_catalog.{'default'},"
            f"class_lang_name character varying COLLATE pg_catalog.{'default'},"
            f"eo_name character varying COLLATE pg_catalog.{'default'},"
            f"eo_type_name character varying COLLATE pg_catalog.{'default'},"
            f"eo_reg_name character varying COLLATE pg_catalog.{'default'},"
            f"eo_area_name character varying COLLATE pg_catalog.{'default'},"
            f"eo_ter_name character varying COLLATE pg_catalog.{'default'},"
            f"eo_parent character varying COLLATE pg_catalog.{'default'},"
            f"CONSTRAINT participant_data_pkey PRIMARY KEY (id)"
            f")"
            f"TABLESPACE pg_default;"
            f"ALTER TABLE public.participant_data OWNER to postgres;"
        )
        con.commit()
        print("\nParticipant_data table created!")
    except:
        con.commit()
        print("\nParticipant_data table already exist")


def create_exams_table():
    try:
        cur.execute(
            f"CREATE TABLE public.exams"
            f"("
            f"exam_id integer NOT NULL,"
            f"participant_id integer,"
            f"test character varying COLLATE pg_catalog.{'default'},"
            f"lang character varying COLLATE pg_catalog.{'default'},"
            f"test_status character varying COLLATE pg_catalog.{'default'},"
            f"dpa_level character varying COLLATE pg_catalog.{'default'},"
            f"ball_100 character varying COLLATE pg_catalog.{'default'},"
            f"ball_12 character varying COLLATE pg_catalog.{'default'},"
            f"ball character varying COLLATE pg_catalog.{'default'},"
            f"adapt_scale character varying COLLATE pg_catalog.{'default'},"
            f"pt_name character varying COLLATE pg_catalog.{'default'},"
            f"pt_reg_name character varying COLLATE pg_catalog.{'default'},"
            f"pt_area_name character varying COLLATE pg_catalog.{'default'},"
            f"pt_ter_name character varying COLLATE pg_catalog.{'default'},"
            f"CONSTRAINT exams_pkey PRIMARY KEY (exam_id)"
            f")"
            f"TABLESPACE pg_default;"
            f"ALTER TABLE public.exams OWNER to postgres;"
        )
        con.commit()
        print("Exams table created!")
    except:
        con.commit()
        print("Exams table already exist")


def create_subjects_table():
    try:
        cur.execute(
            "CREATE TABLE public.subjects"
            "("
            "subject_id integer NOT NULL,"
            f"subject_name character varying COLLATE pg_catalog.{'default'},"
            f"subject_desc character varying COLLATE pg_catalog.{'default'},"
            "CONSTRAINT subjects_pkey PRIMARY KEY (subject_id)"
            ")"
            "TABLESPACE pg_default;"
            "ALTER TABLE public.subjects OWNER to postgres;"
        )
        con.commit()
        print("Subjects table created!")
    except:
        con.commit()
        print("Subjects table already exist")


def get_participants_data_count():
    try:
        cur.execute(
            "SELECT COUNT(*) FROM participant_data"
        )
        return cur.fetchall()[0][0]
    except:
        return 0


def get_exams_count():
    try:
        cur.execute(
            "SELECT COUNT(*) FROM exams"
        )
        return cur.fetchall()[0][0]
    except:
        return 0


def add_participants():
    print_message = True
    counter = get_participants_data_count()
    total = len(participants_data)
    print("\nParticipants inserting...")
    for participant in range(counter, len(participants_data)):
        try:
            cur.execute(
                f"INSERT INTO participant_data VALUES"
                f"("
                f"{participants_data[participant][0]}, {participants_data[participant][1]}, '{participants_data[participant][2]}',"
                f"'{participants_data[participant][3]}', '{participants_data[participant][4]}', '{participants_data[participant][5]}',"
                f"'{participants_data[participant][6]}', '{participants_data[participant][7]}', '{participants_data[participant][8]}',"
                f"'{participants_data[participant][9]}', '{participants_data[participant][10]}', '{participants_data[participant][11]}',"
                f"'{participants_data[participant][12]}', '{participants_data[participant][13]}', '{participants_data[participant][14]}',"
                f"'{participants_data[participant][15]}', '{participants_data[participant][16]}', '{participants_data[participant][17]}'"
                f")"
            )
            con.commit()
            print_message = True
            counter += 1
        except:
            print_message = False
            con.commit()

        if counter / 100000 == int(counter / 100000) and counter > 0 and print_message:
            print(f"{counter} of {total} participants are inserted...")
    print(f"Participants inserted! Added {counter} of {total}")


def add_exams():
    print_message = True
    counter = get_exams_count()
    total = len(exams)
    print("\nExams inserting...")
    for exam in range(counter, len(exams)):
        try:
            cur.execute(
                f"INSERT INTO exams VALUES"
                f"("
                f"{exams[exam][0]}, {exams[exam][1]}, '{exams[exam][2]}',"
                f"'{exams[exam][3]}', '{exams[exam][4]}', '{exams[exam][5]}',"
                f"'{exams[exam][6]}', '{exams[exam][7]}', '{exams[exam][8]}',"
                f"'{exams[exam][9]}', '{exams[exam][10]}', '{exams[exam][11]}',"
                f"'{exams[exam][12]}', '{exams[exam][13]}'"
                f")"
            )
            con.commit()
            print_message = True
            counter += 1
        except:
            print_message = False
            con.commit()

        if counter / 100000 == int(counter / 100000) and counter > 0 and print_message:
            print(f"{counter} of {total} exams are inserted...")
    print(f"Exams inserted! Added {counter} of {total}")


def add_subjects():
    counter = 0
    print("\nSubjects inserting...")
    for subject in range(len(subjects)):
        try:
            cur.execute(
                f"INSERT INTO subjects VALUES({subject + 1}, '{subjects[subject][0]}', '{subjects[subject][1]}')"
            )
            con.commit()
            counter += 1
        except:
            con.commit()
    print(f"Subjects inserted! Added {counter} subjects")


def query():
    cur.execute(
        "SELECT participant_data.year, subjects.subject_desc, ROUND(AVG(CAST(exams.ball_100 AS NUMERIC)), 3) as ball_100, participant_data.reg_name "
        "FROM exams "
        "JOIN subjects ON exams.test = subjects.subject_name "
        "JOIN participant_data ON exams.participant_id = participant_data.id "
        "WHERE exams.ball_100 != 'None' AND exams.test = 'Ukr' AND exams.test_status = 'Зараховано' "
        "GROUP BY participant_data.year, subjects.subject_desc, participant_data.reg_name "
        "ORDER BY participant_data.year, ball_100 DESC"
    )
    data = cur.fetchall()
    con.commit()

    with open(query_file_name, mode='w') as query_file:
        query_writer = csv.writer(query_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            query_writer.writerow(row)


def get_data(csvfile, file_name, participant_id, exam_id):
    reader = csv.reader(csvfile, delimiter=';')
    head = next(reader)
    head.insert(0, "year")
    data = enumerate(reader)
    data_year = re.findall(pattern_file, file_name)[0]
    for n, row in data:
        for b, i in enumerate(row):
            row[b] = row[b].replace("’", "`")
            row[b] = row[b].replace("'", "`")
            if re.match(pattern_mark, i):
                row[b] = row[b].replace(",", ".")
            if i == "null":
                row[b] = None
        participants_data.append([participant_id, data_year, *row[0:16]])

        for i in range(16, len(row), 10):
            if row[i] == subjects[0][1]:
                exams.append(
                    [exam_id, participant_id, subjects[0][0], None, row[i + 1], None,
                     convert_to_float(row[i + 2]), convert_to_int(row[i + 3]), convert_to_int(row[i + 4]),
                     convert_to_int(row[i + 5]), row[i + 6],
                     row[i + 7], row[i + 8], row[i + 9]]
                )
                exam_id += 1
            elif row[i] == subjects[7][1] or row[i] == subjects[7][1] or row[i] == subjects[7][1] or row[i] == \
                    subjects[7][1]:
                exams.append(
                    [exam_id, participant_id, get_subject_name(row[i]), None, row[i + 1],
                     row[i + 4], convert_to_float(row[i + 2]), convert_to_int(row[i + 3]),
                     convert_to_int(row[i + 5]), None, row[i + 6],
                     row[i + 7], row[i + 8], row[i + 9]]
                )
                exam_id += 1
            elif all(row[i:i + 10]):
                exams.append(
                    [exam_id, participant_id, get_subject_name(row[i]), row[i + 1], row[i + 2],
                     None, convert_to_float(row[i + 3]), convert_to_int(row[i + 4]),
                     convert_to_int(row[i + 5]), None, row[i + 6],
                     row[i + 7], row[i + 8], row[i + 9]]
                )
                exam_id += 1
        participant_id += 1
    return [participant_id, exam_id]


with open(first_file_name, newline='', encoding="cp1251") as first_file:
    print("Getting data from the first file...")
    ids = get_data(first_file, first_file_name, participant_id, exam_id)

    with open(second_file_name, newline='', encoding="cp1251") as second_file:
        print("Getting data from the second file...")
        get_data(second_file, second_file_name, ids[0], ids[1])


create_participant_data_table()
create_exams_table()
create_subjects_table()

add_participants()
add_exams()
add_subjects()

query()

cur.close()
con.close()
