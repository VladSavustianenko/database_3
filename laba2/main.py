import psycopg2
import csv


# підключення до бази даних
def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database="laba1",
            user="postgres",
            password="admin"
        )
        print("З'єднання з базою даних  успішне")
    except:
        print(f"Connection error")
    return connection


conn = create_connection()
cursor = conn.cursor()


def statistical_query():
    select_query = '''
    SELECT Results.subject_year, Results.subject_name, avg(Results.Ball100), Locations.RegName
    FROM Results JOIN Participant ON
        Results.OUTID = Student.OUTID
    JOIN Locations ON
        Student.loc_id = Locations.loc_id
    WHERE Results.subject_name = 'Українська мова і література'
    GROUP BY Location.RegName, TestResult.subject_year, Results.subject_name
    '''
    cursor.execute(select_query)

    with open('Query.csv', 'w', encoding="utf-8") as result_csv:
        csv_writer = csv.writer(result_csv)
        header_row = ['Область', 'Рік', 'Середній бал з фізики']
        csv_writer.writerow(header_row)
        for row in cursor:
            csv_writer.writerow(row)


statistical_query()


cursor.close()
conn.close()
