from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
port = 8084
# Prepare a server socket
# Fill in start
serverSocket.bind(('', port))
serverSocket.listen(1)
# Fill in end

while True:
    # Establish the connection
    print("Ready to serve...")
    # Fill in start
    connectionSocket, addr = serverSocket.accept()

    print("Server Connected to {}".format(addr))
    # Fill in end

    try:
        # Fill in start
        message = connectionSocket.recv(2048)
        # Fill in end
        if message == "":
            connectionSocket.close()
            continue

        filename = message.split()[1]
        f = open(filename[1:])
        # Fill in start
        outputdata = f.read()
        f.close()
        # Fill in end

        # Send one HTTP header line into socket

        # Fill in start
        respHeader = "HTTP/1.1 200 OK\r\n\r\n"
        connectionSocket.send(respHeader.encode())
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.close()



    except IOError:
        # Send response message for file not found
        # Fill in start
        respHeader = "HTTP/1.1 404 Not Found\r\n\r\n"
        connectionSocket.send(respHeader.encode())

        respMes = "<html><head><title>File Not Found</title></head><body><h1>404 Not Found!</h1></body></html>\r\n"
        connectionSocket.send(respMes.encode())
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end
    print("Connection complete")

serverSocket.close()
