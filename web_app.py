import os
import signal
from flask import Flask
from db_connector import get_user

app = Flask(__name__)

@app.route('/users/get_user_data/<user_id>')
#The server accepts to display a user from the database
#user_id (int)
def get_user_name(user_id):
    try:
        user_name = get_user(user_id)
        return "<H1 id='user_name'>""The user name is: " + user_name + "</H1>"
    except Exception:
        return "<H1 id='error'>" "No such user for Id: " + user_id + "</H1>"

# Automatic termination to rest api
@app.route('/stop_server')
def stop_server():
    try:
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
        return 'Server stopped'
    except Exception:
        return 'Server is not responding'

app.run(host='127.0.0.1', debug=True, port=5001)
