import os
import signal
from flask import Flask, request
from db_connector import add_user, get_user, update_user, delete_user

app = Flask(__name__)

@app.route('/users/<user_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def user(user_id):
    #The server receives a POST request to add a user to the database
    if request.method == 'POST':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            add_user(user_id, user_name)
            return {'status':'ok', 'user_added': user_name}, 200 # status code
        except Exception:
            return {'status':'error', 'reason': 'id already exists'}, 500 # status code

    #The server receives a GET request to get a user from the database
    elif request.method == 'GET':
        try:
            user_name = get_user(user_id)
            return {'status':'ok', 'user_name': user_name}, 200 # status code
        except Exception:
            return {'status': 'error', 'reason': 'no such id'}, 500

    #The server accepts a PUT request to update user data in the database
    elif request.method == 'PUT':
        try:
            request_data = request.json
            user_name = request_data.get('user_name')
            update_user(user_id, user_name)
            return {'status':'ok', 'user_updated': user_name}, 200 # status code
        except Exception:
            return {'status': 'error', 'reason': 'no such id'}, 500

    #The server receives a DELETE request to delete a user from the database
    else:
        try:
            delete_user(user_id)
            return {'status': 'ok', 'user_deleted': user_id}, 200  # status code
        except Exception:
            return {'status': 'error', 'reason': 'no such id'}, 500

#Automatic termination to rest api
@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
        return 'Server stopped'
    except Exception:
        return 'Server is not responding'

app.run(host='127.0.0.1', debug=True, port=5000)
