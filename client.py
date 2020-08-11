import socket


HEADER = 64
PORT = 5050 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!EXIT"
SERVER = "10.0.0.8" #ip
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)