import csv
import re
from pymongo import MongoClient
cluster = MongoClient("mongodb://localhost:27017")
db = cluster["laba4"]

student_table = db["student"]
exam_table = db["exam"]
subject_table = db["subject"]


pattern_mark = re.compile(r'^\d+,\d+$')
pattern_file = re.compile(r'\d{4}')
first_file_name = 'Odata2019File.csv'
second_file_name = 'Odata2020File.csv'
query_file_name = 'Query.csv'


students_data = []
exams = []
student_id = 1
exam_id = 1


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


def convert_to_int(elem):
    try:
        return int(float(elem))
    except:
        return elem


def get_subject_name(elem):
    for i in range(len(subjects)):
        if subjects[i][1] == elem:
            return subjects[i][0]


def add_subjects():
    counter = 0
    print("\nSubjects inserting...")
    for i in range(len(subjects)):
        try:
            subject_table.insert_one({
                "_id": i + 1,
                "name": subjects[i][0],
                "description": subjects[i][1]
            })
            counter += 1
        except:
            pass
    print(f"Subjects inserted! Added {counter} subjects")


def add_students():
    print_message = True
    counter = student_table.count()
    total = len(students_data)
    print("\nStudents inserting...")
    for i in range(counter, len(students_data), 10000):
        try:
            student_table.insert_many(students_data[i:i+10000])
            print_message = True
            counter += 10000
        except:
            print_message = False

        if counter / 100000 == int(counter / 100000) and counter > 0 and print_message:
            print(f"{counter} of {total} students are inserted...")
    print(f"Students inserted! Added {counter} of {total}")


def add_exams():
    print_message = True
    counter = exam_table.count()
    total = len(exams)
    print("\nExams inserting...")
    for i in range(counter, len(exams), 10000):
        try:
            exam_table.insert_many(exams[i:i+10000])
            print_message = True
            counter += 10000
        except:
            print_message = False

        if counter / 100000 == int(counter / 100000) and counter > 0 and print_message:
            print(f"{counter} of {total} exams are inserted...")
    print(f"Exams inserted! Added {counter} of {total}")


def query():
    data = list(exam_table.aggregate([
        {
            '$match':
                {
                    'test': 'Ukr',
                    'ball_100':
                        {
                            '$nin': ['null', 0],
                        },
                }
        },
        {
            '$lookup':
                {
                    'from': 'student',
                    'localField': 'student_id',
                    'foreignField': '_id',
                    'as': 'student',
                }
        },
        {
            '$project':
                {
                    '_id': 1,
                    'student.year': 1,
                    'test': 1,
                    'ball_100': 1,
                    'student.reg_name': 1,
                }
        },
        {
            '$group':
                {
                    '_id':
                        {
                            'year': '$student.year',
                            'test': '$test',
                            'reg_name': '$student.reg_name',
                        },
                    'avg_ball_100':
                        {
                            '$avg': '$ball_100',
                        },
                }
        },
        {
            '$sort':
                {
                    '_id.year': 1,
                }
        }
    ]))

    with open(query_file_name, mode='w') as query_file:
        query_writer = csv.writer(query_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            query_writer.writerow([row['_id']['year'][0], row['_id']['test'], row['_id']['reg_name'][0], row['avg_ball_100']])


def get_data(csvfile, file_name, student_id, exam_id):
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
        students_data.append({
            "_id": student_id,
            "year": int(data_year),
            "student_id": row[0],
            "birth": row[1],
            "sex_type_name": row[2],
            "reg_name": row[3],
            "area_name": row[4],
            "ter_name": row[5],
            "reg_type_name": row[6],
            "ter_type_name": row[7],
            "class_profile_name": row[8],
            "class_lang_name": row[9],
            "eo_name": row[10],
            "eo_type_name": row[11],
            "eo_reg_name": row[12],
            "eo_area_name": row[13],
            "eo_ter_name": row[14],
            "eo_parent": row[15],
        })

        for i in range(16, len(row), 10):
            if row[i] == subjects[0][1]:
                exams.append({
                    "_id": exam_id,
                    "student_id": student_id,
                    "test": subjects[0][0],
                    "lang": None,
                    "test_status": row[i + 1],
                    "dpa_level": None,
                    "ball_100": convert_to_int(row[i + 2]),
                    "ball_12": convert_to_int(row[i + 3]),
                    "ball": convert_to_int(row[i + 4]),
                    "adapt_scale": convert_to_int(row[i + 5]),
                    "pt_name": row[i + 6],
                    "pt_reg_name": row[i + 7],
                    "pt_area_name": row[i + 8],
                    "pt_ter_name": row[i + 9],
                })
                exam_id += 1
            elif row[i] == subjects[7][1] or row[i] == subjects[7][1] or row[i] == subjects[7][1] or row[i] == \
                    subjects[7][1]:
                exams.append({
                    "_id": exam_id,
                    "student_id": student_id,
                    "test": get_subject_name(row[i]),
                    "lang": None,
                    "test_status": row[i + 1],
                    "dpa_level": row[i + 4],
                    "ball_100": convert_to_int(row[i + 2]),
                    "ball_12": convert_to_int(row[i + 3]),
                    "ball": convert_to_int(row[i + 4]),
                    "adapt_scale": None,
                    "pt_name": row[i + 6],
                    "pt_reg_name": row[i + 7],
                    "pt_area_name": row[i + 8],
                    "pt_ter_name": row[i + 9],
                })
                exam_id += 1
            elif all(row[i:i + 10]):
                exams.append({
                    "_id": exam_id,
                    "student_id": student_id,
                    "test": get_subject_name(row[i]),
                    "lang": row[i + 1],
                    "test_status": row[i + 2],
                    "dpa_level": None,
                    "ball_100": convert_to_int(row[i + 3]),
                    "ball_12": convert_to_int(row[i + 4]),
                    "ball": convert_to_int(row[i + 5]),
                    "adapt_scale": None,
                    "pt_name": row[i + 6],
                    "pt_reg_name": row[i + 7],
                    "pt_area_name": row[i + 8],
                    "pt_ter_name": row[i + 9],
                })
                exam_id += 1
        student_id += 1
    return [student_id, exam_id]


with open(first_file_name, newline='', encoding="cp1251") as first_file:
    print("Getting data from the first file...")
    ids = get_data(first_file, first_file_name, student_id, exam_id)

    with open(second_file_name, newline='', encoding="cp1251") as second_file:
        print("Getting data from the second file...")
        get_data(second_file, second_file_name, ids[0], ids[1])


add_students()
add_exams()
add_subjects()
query()
