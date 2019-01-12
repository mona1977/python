import psycopg2 as pg


def get_connection():
    conn = pg.connect(
        database='company',
        user='surendra',
        password='!test32',
        host='test.om',
        port=5432)
    return conn


def create_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute('''CREATE TABLE LOGS
        (USERID       TEXT    UNIQUE    NOT Null,
         NAME           TEXT    NOT NULL,
         EMAIL            TEXT     NOT NULL,
         PASSWORD        TEXT);''')
        print "Table created successfully"
        cursor.execute('''CREATE TABLE company
         (USERID       TEXT   REFERENCES LOGS(USERID)  NOT Null,
            name           TEXT     NOT NULL,
             phone         TEXT     NOT NULL,
            address        TEXT);''')
        connection.commit()
        connection.close()
    except Exception as error:
        return error


def insert_catagories(USER, name, phone, address):
    connection = get_connection()
    cursor = connection.cursor()
    print "cur is created"
    query = """INSERT INTO LOGSS(USERID,name,phone,address) VALUES('%s', '%s', %s, '%s');"""
    query = query % (
        USER, name, phone, address)
    print query
    cursor.execute(query)
    connection.commit()
    print "Records created successfully"
    connection.close()


def catagory_alreadyexits(USER, name,phone, address):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT USERID from LOGSS where name='%s';"""
    query = query % (name, )
    cursor.execute(query)
    rows = cursor.fetchall()
    print rows
    try:
        if (len(rows) == 0):
            insert_catagories(USER, name, phone, address)
        else:
            return 1
    except Exception as error:
        return error


def filter_user_chart(USER):
    connection = get_connection()
    cursor = connection.cursor()
    fetch_db = """select name,phone from logss where userid='%s' group by name"""
    fetch_db = fetch_db % (USER)
    cursor.execute(fetch_db)
    rows = cursor.fetchall()
    for row in rows:
        print "name", row[0], type(row[0])
        print "phone = ", row[1]
    print "Operation done successfully"
    cursor.close()
    return rows


def filter_user_data(USER):
    connection = get_connection()
    cursor = connection.cursor()
    fetch_db = """SELECT USERID, name, phone, address  from LOGSS where USERID='%s'"""
    fetch_db = fetch_db % (USER)
    cursor.execute(fetch_db)
    rows = cursor.fetchall()
    for row in rows:
        print "User ID = ", row[0]
        print "Your Name = ", row[1]
        print "Registered Name = ", row[2]
        print "Password = ", row[3], "\n"
    print "Operation done successfully"
    cursor.close()
    return rows


def insert_db(USER, NAME, EMAIL, PASSWORDV):
    connection = get_connection()
    cursor = connection.cursor()
    print "cur is created"
    query = """INSERT INTO LOGS(USERID,NAME,EMAIL,PASSWORD) VALUES('%s', '%s', '%s', '%s');"""
    query = query % (
        USER, NAME, EMAIL, PASSWORDV)
    print query
    cursor.execute(query)
    connection.commit()
    print "Records created successfully"
    connection.close()


def user_alreadyexits(USER, NAME, EMAIL, PASSWORDV):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT USERID from LOGS where USERID='%s';"""
    query = query % (USER, )
    cursor.execute(query)
    rows = cursor.fetchall()
    print rows
    try:
        if (len(rows) == 0):
            insert_db(USER, NAME, EMAIL, PASSWORDV)
        else:
            return 1
    except Exception as error:
        return error
    connection.close()


def authenticate(username, password):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT USERID, PASSWORD from LOGS where USERID='%s' and PASSWORD='%s';"""
    query = query % (username, password)
    cursor.execute(query)
    rows = cursor.fetchall()
    print rows
    try:
        if (rows[0][0] == username) and (rows[0][1] == password):
            return 1
        else:
            return 0
    except Exception as error:
        return error
    connection.close()
