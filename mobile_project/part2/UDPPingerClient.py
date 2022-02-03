from socket import *
import time


def current_micro_time():
    return round(time.time() * 1000000)


clientSocket = socket(AF_INET, SOCK_DGRAM)
serverAddr = ('localhost', 12000)
clientSocket.settimeout(1)

i = 0
while i <= 10:

    try:
        reqTime = current_micro_time()
        message = "Ping " + str(i) + " " + str(reqTime)
        clientSocket.sendto(message.encode(), serverAddr)
        print("Ping Message : " + message)

        data, server = clientSocket.recvfrom(1024)
        print("Response Message: " + data.decode())
        respTime = current_micro_time()

        passTime = respTime - reqTime
        print("RTT: {} microseconds".format(passTime))
        print("--------------------------------------------------")

    except timeout:
        print("Request-{} timed out".format(i))
        print("--------------------------------------------------")

    i += 1

clientSocket.close()
