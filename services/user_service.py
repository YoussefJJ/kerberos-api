import sqlite3

from flask import Response

from models.User import User

     
def add_user(user_to_insert):
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USER';")
    if (not cursor.fetchall()):
        cursor.execute("CREATE TABLE USER(first_name VARCHAR2, last_name VARCHAR2, email VARCHAR2, pwd VARCHAR2)")
    sql_query = 'INSERT INTO user VALUES(?,?,?,?);'
    user = User()
    user.setEmail(user_to_insert["email"])
    user.setFirstName(user_to_insert["firstname"])
    user.setLastName(user_to_insert["lastname"])
    user.setHashedPasswd(user_to_insert["hashedpwd"])
    cursor.execute(sql_query, (user.firstname, user.lastname, user.email, user.hashedpwd))
    connection.commit()
    connection.close()
    return user

def find_user(credentials):
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
    sql_query = 'SELECT * FROM user WHERE email=? and pwd=?;'
    user_to_find = (
        credentials['email'],
        credentials['hashedpwd']
    )
    cursor.execute(sql_query, user_to_find)
    if (cursor.fetchall() == []):
        print("Invalid credentials.")
        return Response(status=401), None
    cursor.execute(sql_query, user_to_find)
    user = {}    
    user_found = cursor.fetchone()
    user["firstname"] = user_found[0]
    user["lastname"] = user_found[1]
    return Response(status=200), user

def check(email):
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM user WHERE email=?',(email,))
    response = Response(status=409 if cursor.fetchall() != [] else 200)
    connection.close()
    return response
