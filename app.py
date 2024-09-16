from app import create_app, db
from flask_socketio import SocketIO, emit
from app.services import get_openai_response

app = create_app()
socketio = SocketIO(app)


@SocketIO.on('message')
def handle_message(msg):
    response = get_openai_response(msg['data'])
    emit('response', {'data': response})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    socketio.run(app, debug=True)
