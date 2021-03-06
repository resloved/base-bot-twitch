import cfg
import socket

def chat(sock, msg):
    sock.send("PRIVMSG #{} :{}".format(cfg.CHAN, msg))

def ban(sock, user):
    chat(sock, ".ban {}".format(user))

def timeout(sock, user, secs=600):
     chat(sock, ".timeout {}".format(user, secs))

s = socket.socket()
s.connect((HOST, PORT))
s.send("PASS {}\r\n".format(PASS).encode("utf-8"))
s.send("NICK {}\r\n".format(NICK).encode("utf-8"))
s.send("JOIN {}\r\n".format(CHAN).encode("utf-8"))

while True:
    response = s.recv(1024).decode("utf-8")
    if response == "PING :tmi.twitch.tv\r\n":
        s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
    else:
        print(response)
