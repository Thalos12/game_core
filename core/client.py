# client
import socket


# noinspection PyPep8Naming,PyUnboundLocalVariable
def client(host, string_to_send):
    HOST = host
    PORT = 50007
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        connected = "Connected to server at " + str(host) + ", sending..."
        print connected
        s.sendall(string_to_send)
        print "Data sent."
        data = s.recv(1024)
        print data
    finally:
        s.close()
