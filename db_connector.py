from datetime import datetime
import pymysql

schema_name = "freedb_db123123"

#The function makes a connection to the database
#host_test (str), port_test (int), user_test (str), passwd_test(str)
def db_connector(host_test, port_test, user_test, passwd_test):
    connection = pymysql.connect(host=host_test, port=port_test, user=user_test, passwd=passwd_test, db=schema_name)
    connection.autocommit(True)
    cursor = connection.cursor()
    return connection,cursor

#The function disconnects from the database
def db_close_connector(cursor,connection):
    cursor.close()
    connection.close()

#The function adds data to the database
#user_id(int), user_name (str)
def add_user(user_id, user_name):
    connection, cursor = db_connector('sql.freedb.tech', 3306, 'freedb_hadar', 'm@h6HrEMZYxvBx#')
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(f"INSERT into {schema_name}.users (user_id, user_name, creation_date) VALUES ('{user_id}', '{user_name}', '{time_now}' )")
    db_close_connector(connection,cursor)

#The function provides data from the database
#user_id(int), user_name (str)
def get_user(user_id):
    connection, cursor = db_connector('sql.freedb.tech', 3306, 'freedb_hadar', 'm@h6HrEMZYxvBx#')
    cursor.execute(f"SELECT * FROM {schema_name}.users where user_id= '{user_id}';")
    for row in cursor:
        user_name = row[1]
    db_close_connector(connection,cursor)
    return user_name

#The function updates data in the database
#user_id(int), user_name (str)
def update_user(user_id, user_name):
    connection, cursor = db_connector('sql.freedb.tech', 3306, 'freedb_hadar', 'm@h6HrEMZYxvBx#')
    cursor.execute(f"UPDATE {schema_name}.users SET user_name = '{user_name}' WHERE user_id = '{user_id}'")
    db_close_connector(connection,cursor)

#The function deletes data from the database
#user_id(int)
def delete_user(user_id):
    connection, cursor = db_connector('sql.freedb.tech', 3306, 'freedb_hadar', 'm@h6HrEMZYxvBx#')
    cursor.execute(f"DELETE FROM {schema_name}.users WHERE user_id = '{user_id}'")
    db_close_connector(connection,cursor)

