from socket import socket
import time
import threading
import random

sock = socket()


def connect():
    sock.connect(('irc.chat.twitch.tv', 6667))  # connects to twitch.


def sendRaw(data):
    print("sending raw " + data)
    sock.send(bytes(data + '\r\n', 'utf-8')) # enables you to communicate to the irc server

def information():
    channel = "yourusername"
    sendRaw('PASS oauth:')  # oauth https://twitchapps.com/tmi/
    sendRaw('NICK ' + channel)  # nickname
    # requests more information
    sendRaw('CAP REQ :twitch.tv/commands')
    sendRaw('CAP REQ :twitch.tv/tags')

pleb_colours = "Blue", "BlueViolet", "CadetBlue", "Chocolate", "Coral", "DodgerBlue", "Firebrick", "GoldenRod", "Green", "HotPink", "OrangeRed", "Red", "SeaGreen", "SpringGreen", "YellowGreen"
prime = True # set this to True if you have prime or turbo, if not set it to False or anything else

def GACHI_PRIDE():
    if prime:
            time.sleep(10)  # time delay in seconds # (keep within twitch ratelimits or you will be global banned for about 30mins)
            random_number = random.randint(0, 16777215)
            hex_number = str(hex(random_number))
            sendRaw('PRIVMSG #turtoise :/color  #' + hex_number[2:])
    else:
            time.sleep(10)  # time delay in seconds # (keep within twitch ratelimits or you will be global banned for about 30mins)
            sendRaw('PRIVMSG #' + channel + ' :/color ' + random.choice(pleb_colours))



timerone = threading.Thread(target=GACHI_PRIDE)
timerone.start()  # runs the timer on a separate thread so it doesnt block data


def commands():
    while True:  # continuously getting the data
        chat = sock.recv(1024).decode('utf -8', errors='replace')  # socket data (chat)
        print(chat)

        if "PING" in chat:
            sendRaw("PONG")  # This keeps the bot alive  when  twitch sends PING a bot needs to send PONG back.

def run_bot():
    connect()
    information()
    commands()

run_bot()
