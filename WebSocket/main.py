from flask import Flask, render_template, session, request, copy_current_request_context
from flask_socketio import SocketIO, emit, disconnect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=None)


@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.event
def connect_event(message):
    emit("log_event", {'data': message['data']})

@socketio.event
def comment_event(message):
    emit("log_event", {'data': message['data']}, broadcast=True)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected', request.sid)

@socketio.event
def volume_event(message):
    # print(message['volume'])
    emit("volume_update", {'volume': message['volume']}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
