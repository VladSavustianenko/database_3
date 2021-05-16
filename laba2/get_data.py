import config


def create_location_view():
    config.origin_cur.execute(
        "CREATE OR REPLACE VIEW Location AS "
        "SELECT ROW_NUMBER() OVER(ORDER BY reg_name ASC) AS location_id, reg_name, area_name, ter_name, ter_type_name "
        "FROM ("
        "SELECT DISTINCT reg_name, area_name, ter_name, ter_type_name "
        "FROM Participant_data "
        ") AS Locations "
        "GROUP BY reg_name, area_name, ter_name, ter_type_name"
    )
    config.origin_con.commit()


def create_school_view():
    config.origin_cur.execute(
        "CREATE OR REPLACE VIEW School AS "
        "SELECT ROW_NUMBER() OVER(ORDER BY eo_name ASC) AS school_id, eo_name, eo_type_name, location_id, eo_parent "
        "FROM ( "
        "SELECT DISTINCT eo_name, eo_type_name, Location.location_id, eo_parent "
        "FROM Participant_data "
        "JOIN Location ON Participant_data.ter_name = Location.ter_name "
        ") AS Schools"
    )
    config.origin_con.commit()


def create_student_view():
    config.origin_cur.execute(
        "CREATE OR REPLACE VIEW Student AS "
        "SELECT participant_id AS out_id, birth, sex_type_name, reg_type_name, class_profile_name "
        "FROM Participant_data"
    )
    config.origin_con.commit()


def create_exam_view():
    config.origin_cur.execute(
        "CREATE OR REPLACE VIEW Exam AS "
        "SELECT DISTINCT exam_id, participant_data.participant_id AS out_id, participant_data.year, test, pt_name, "
        "Location.location_id, lang, test_status, dpa_level, adapt_scale, ball_100, ball_12, ball "
        "FROM exams "
        "LEFT JOIN participant_data ON exams.participant_id = participant_data.id "
        "LEFT JOIN Location ON exams.pt_ter_name = Location.ter_name"
    )
    config.origin_con.commit()


def get_location():
    create_location_view()
    config.origin_cur.execute(
        "SELECT * FROM Location"
    )
    return config.origin_cur.fetchall()


def get_school():
    create_school_view()
    config.origin_cur.execute(
        "SELECT * FROM School"
    )
    return config.origin_cur.fetchall()


def get_student():
    create_student_view()
    config.origin_cur.execute(
        "SELECT * FROM Student"
    )
    return config.origin_cur.fetchall()


def get_exam():
    create_exam_view()
    config.origin_cur.execute(
        "SELECT * FROM Exam"
    )
    return config.origin_cur.fetchall()
