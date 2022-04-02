import logging
import socket

from emoji import demojize

username = "davi21xxi"
server = "irc.chat.twitch.tv"
port = 6667
token = "oauth:kpz9iq7hk78g6ck8bycx5r3clg9vf9"
channel = "#jomaoppa"

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s — %(message)s',
                    datefmt='%Y-%m-%d_%H:%M:%S',
                    handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

if __name__ == "__main__":

    sock = socket.socket()

    sock.connect((server, port))

    sock.send(f"PASS {token}\n".encode('utf-8'))
    sock.send(f"NICK {username}\n".encode('utf-8'))
    sock.send(f"JOIN {channel}\n".encode('utf-8'))

    while True:
        resp = sock.recv(2048).decode("utf-8", "ignore ")

        if resp.startswith("PING"):
            sock.send("PONG\n".encode('utf-8'))

        elif len(resp) > 0:
            print(resp)
