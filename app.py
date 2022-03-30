import json
import json
from flask import Flask, Response, request
from flask_kerberos import init_kerberos
from flask_kerberos import requires_authentication
from services.user_service import *

app = Flask(__name__)

@app.route('/signup', methods=['POST', 'GET'])
@requires_authentication
def signup(user):

    signup_user = dict(request.get_json())
    signup_user = add_user(signup_user)
    return Response(status=201)


@app.route('/login', methods=['POST', 'GET'])
@requires_authentication
def login(user):
    login_user = dict(request.get_json())
    response, login_user = find_user(login_user)
    response = app.response_class(
        response=json.dumps(login_user),
        status=200,
        mimetype='application/json'
    )
    return response


@app.route('/check_email', methods=['POST', 'GET'])
@requires_authentication
def check_email(user):
    data = dict(request.get_json())
    print(data)
    email = data["email"]
    response = check(email)
    return response



if __name__ == '__main__':
    init_kerberos(app,service='host', hostname="service1.insat.tn")
    app.run(host='0.0.0.0', port=9998, debug=True)