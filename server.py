from flask import Flask, render_template, session, url_for, redirect
from flask_socketio import SocketIO, emit, send
import eventlet
import uuid

eventlet.monkey_patch()
async_mode = 'eventlet'

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard password'
socketio = SocketIO(app, async_mode=async_mode)



@app.route('/')
def index():
    return render_template('game.html')


@socketio.on('create user')
def create_user():
    session['username'] = str(uuid.uuid4())
    emit('new user', session['username'])

@socketio.on('message')
def message(message):
    emit('message', message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
