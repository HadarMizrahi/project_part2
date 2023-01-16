import requests

#The function stops the backend server
def stop_backend_server():
    try:
        requests.get('http://127.0.0.1:5000/stop_server')
        return 'Backend server stopped'
    except Exception:
        return 'Backend server is not responding'

#The function stops the frontend server
def stop_frontend_server():
    try:
        requests.get('http://127.0.0.1:5001/stop_server')
        return 'Backend server stopped'
    except Exception:
        return 'Backend server is not responding'


stop_backend_server()
stop_frontend_server()
