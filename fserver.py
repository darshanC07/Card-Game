from flask import Flask, render_template,request
from flask_socketio import SocketIO, send,join_room,leave_room
from cards import cards
from random import randint
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

cards = cards

# room = None
connectedUsers = set()

@app.route('/')
def index():
    userCardDeck = []
    for i in range(5):
        index = randint(0,len(cards)-1)
        userCardDeck.append(cards[index])
        
    return render_template("index.html",cardDeck=userCardDeck)

@socketio.on('message')
def handle_message(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)
@socketio.on('connect')
def handle_connect(user):
    print('Client connected')
    # print(user)
    # print(request)

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    
@socketio.on('join_room')
def on_join_room(data):
    global room
    username = data['userName']
    room = data['room']
    print(room)
    join_room(room)
    socketio.emit("playerJoined",f"{username} has joined room",to=room,include_self=False)

@socketio.on('leave_room')
def on_leave_room(data):
    socketio.emit("playerLeft",data,to=room,include_self=False)
    
@socketio.on('messageSentToRoom')    
def onMessageSentToRoom(data):
    socketio.emit("newMessage",data,to=room)

@socketio.on('cardPlayed')
def cardPlayerd(card):
    global room
    print(card)
    socketio.emit("otherPlayersCard",card,to=room,include_self=False)
if __name__ == '__main__':
    socketio.run(app, debug=True)