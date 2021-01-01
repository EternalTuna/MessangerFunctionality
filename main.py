from flask import session
from flask_socketio import SocketIO
import time
from application import create_app 
from application.database import DataBase
import config 

    # SETUP
app = create_app()
socketio = SocketIO(app) # Communication engine 


    # FUNCTIONS


@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    """
    handles saving messages once received from web server
    and sending message to other clients 
    :parameter json: json
    :param methods: POST | GET
    :return: None
    """
    date = dict(json)
    if "name" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', json)

    # MAIN INSTRUCTIONS

if __name__ == "__main__": # start web server
    socketio.run(app, debug=True, host=str(config.Config.SERVER))