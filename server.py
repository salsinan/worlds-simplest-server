from http import server
from socket import *

def createServer():
    # create endpoint
    serversocket = socket(AF_INET, SOCK_STREAM)
    try:
        # only one app can communicate with this server at this port at any time
        serversocket.bind(('localhost', 9000))
        # tells the OS that if port is busy, queue the next 4 incoming requests 
        serversocket.listen(5)
        while(1):
            # .accept() is blocking -- it waits until server goes down or is otherwise stopped
            (clientsocket, address) = serversocket.accept()

            # this line only executes when a "phone call" is received (when a socket connection is established)
            # .decode() converts utf-8 into unicode
            rd = clientsocket.recv(5000).decode()
            pieces = rd.split("\n")
            # we only get the first line
            if ( len(pieces) > 0 ): print(pieces[0])

            # construct a response
            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            # \r\n --> network's version of newline
            data += "\r\n"
            data += "<html><body>Hello, Server</body></html>\r\n\r\n"
            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as exec:
        print("Error:\n")
        print(exec)
    
    serversocket.close()

print('Access http://localhost:9000')
createServer()
