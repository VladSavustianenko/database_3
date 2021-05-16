import config
import csv

import create_database
import get_data
import set_data

create_database.create()

# set_data.set_location(get_data.get_location())
# set_data.set_school(get_data.get_school())
# set_data.set_student(get_data.get_student())
# set_data.set_exam(get_data.get_exam())


with open('Query.csv', mode='w') as query_file:
    config.new_cur.execute(
        "SELECT Exam.year, Exam.test, ROUND(AVG(CAST(Exam.ball_100 AS numeric)), 3), Location.reg_name "
        "FROM Exam "
        "JOIN Location ON Exam.location_id = Location.location_id "
        "WHERE Exam.test = 'Ukr' "
        "GROUP BY Exam.year, Exam.test, Location.reg_name"
    )
    data = config.new_cur.fetchall()

    query_writer = csv.writer(query_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in data:
        query_writer.writerow(row)


config.close_origin()
config.close_new()
