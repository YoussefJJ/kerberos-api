import json
import sqlite3
from flask import Flask, Response, request
from User import User
app = Flask(__name__)

@app.route('/signup', methods=['POST', 'GET'])
def signup():

    user = dict(request.get_json())
    user = add_user(user)
    return Response(status=201)


@app.route('/login', methods=['POST', 'GET'])
def login():
    user = dict(request.get_json())
    response, user = find_user(user)
    response = app.response_class(
        response=json.dumps(user),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/check_email', methods=['POST', 'GET'])
def check_email():
    data = dict(request.get_json())
    print(data)
    email = data["email"]
    response = check(email)
    return response


def add_user(user_to_insert):
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='USER';")
    if (not cursor.fetchall()):
        cursor.execute("CREATE TABLE USER(first_name VARCHAR2, last_name VARCHAR2, email VARCHAR2, pwd VARCHAR2)")
    sql_query = 'INSERT INTO user VALUES(?,?,?,?);'
    user = User()
    print(user_to_insert)
    user.setEmail(user_to_insert["email"])
    user.setFirstName(user_to_insert["firstname"])
    user.setLastName(user_to_insert["lastname"])
    user.setHashedPasswd(user_to_insert["hashedpwd"])
    cursor.execute(sql_query, (user.firstname, user.lastname, user.email, user.hashedpwd))
    connection.commit()
    connection.close()
    return user

def find_user(credentials):
    sql_query = 'SELECT * FROM user WHERE email=? and pwd=?;'
    connection = sqlite3.connect("test_db.db")
    cursor = connection.cursor()
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
    response = Response(409 if cursor.fetchall() != [] else 200)
    connection.close()
    return response


if __name__ == '__main__':
    app.run(debug=True)