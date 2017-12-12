from flask import Flask, render_template
from flask_socketio import SocketIO
from flask import request
import json

app = Flask(__name__, static_url_path='', static_folder='static',)
app.config['SECRET_KEY'] = 'secret!'
app.config['TEMPLATES_AUTO_RELOAD'] = True
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/_update')
def _update():
	message = request.args.get('message', '')
	socketio.emit('event', message, broadcast=True)
	return '1'

@app.route('/check')
def check():
	return '1'

if __name__ == '__main__':
    socketio.run(app, ssl_context=('cert.pem', 'key.pem'), host='0.0.0.0')
    # app.run(ssl_context='adhoc')

    # print('AAA')