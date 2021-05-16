import config


def set_location(data):
    print("\nInserting Location...")
    counter = 0
    for i in range(len(data)):
        try:
            config.new_cur.execute(
                """INSERT INTO Location VALUES(%s, %s, %s, %s, %s)""",
                (
                    data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]
                )
            )
            config.new_con.commit()
            counter += 1
        except:
            config.new_con.commit()
    print(f"{counter} rows inserted")


def set_school(data):
    print("\nInserting School...")
    counter = 0
    for i in range(len(data)):
        try:
            config.new_cur.execute(
                """INSERT INTO School VALUES(%s, %s, %s, %s, %s)""",
                (
                    data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]
                )
            )
            config.new_con.commit()
            counter += 1
        except:
            config.new_con.commit()
    print(f"{counter} rows inserted")


def set_student(data):
    print("\nInserting Student...")
    print_message = True
    counter = 0
    for i in range(len(data)):
        try:
            config.new_cur.execute(
                """INSERT INTO Student VALUES(%s, %s, %s, %s, %s)""",
                (
                    data[i][0], data[i][1], data[i][2], data[i][3], data[i][4]
                )
            )
            config.new_con.commit()
            counter += 1
            print_message = True
        except:
            config.new_con.commit()
            print_message = False

        if counter / 100000 == int(counter / 100000) and counter > 0 and print_message:
            print(f"{counter} rows inserted...")
    print(f"{counter} rows inserted")


def set_exam(data):
    print("\nInserting Exam...")
    print_message = True
    counter = 0
    for i in range(len(data)):
        try:
            config.new_cur.execute(
                """INSERT INTO Exam VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
                (
                    data[i][0], data[i][1], data[i][2], data[i][3],
                    data[i][4], data[i][5], data[i][6], data[i][7], data[i][8],
                    None if data[i][9] == 'None' or data[i][9] == 'null' else int(float(data[i][9])),
                    None if data[i][10] == 'None' or data[i][10] == 'null' else int(float(data[i][10])),
                    None if data[i][11] == 'None' or data[i][11] == 'null' else int(float(data[i][11])),
                    None if data[i][12] == 'None' or data[i][12] == 'null' else int(float(data[i][12])),
                )
            )
            config.new_con.commit()
            counter += 1
            print_message = True
        except:
            config.new_con.commit()
            print_message = False

        if counter / 100000 == int(counter / 100000) and counter > 0 and print_message:
            print(f"{counter} rows inserted...")
    print(f"{counter} rows inserted")
