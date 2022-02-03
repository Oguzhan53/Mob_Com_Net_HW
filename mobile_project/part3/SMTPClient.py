from socket import *
from base64 import *
import ssl

senderMail = "enter_sender_email" 
password = "sender_password"
receiverMail = "enter_receiver_email"
subject = "SMTP Mail Test"

msg = "\r\n I love computer networks!\r\n(This is test email!!!)"
endmsg = "\r\n.\r\n"

# Choose a mail server (e.g. Googlemailserver) and call it mailserver
# Fill in start
port = 587
mailserver = ("smtp.gmail.com", port)
# Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver

# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)
# Fill in end

recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != b'220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024)
print(recv1)
if recv1[:3] != b'250':
    print('250 reply not received from server.')

TLSCommand = "STARTTLS\r\n"
clientSocket.send(TLSCommand.encode())
recv2 = clientSocket.recv(1024)
print(recv2)
if recv2[:3] != b'220':
    print('220 reply not received from server.')

# Send sender email and password information for authentication
clientSocket = ssl.wrap_socket(clientSocket)

clientSocket.send("AUTH LOGIN\r\n".encode())
recv3 = clientSocket.recv(1024)
print(recv3)
if recv3[:3] != b'334':
    print('334 reply not received from server.')

clientSocket.send(b64encode(senderMail.encode()) + "\r\n".encode())
recv4 = clientSocket.recv(1024)
print(recv4)
if recv4[:3] != b'334':
    print('334 reply not received from server.')

clientSocket.send(b64encode(password.encode()) + "\r\n".encode())
recv5 = clientSocket.recv(1024)
print(recv5)
if recv5[:3] != b'235':
    print('235 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <" + senderMail + ">\r\n"
clientSocket.send(mailFrom.encode())
recv6 = clientSocket.recv(1024)
print(recv6)
if recv6[:3] != b'250':
    print('250 reply not received from server.')
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
rcptTo = "RCPT TO: <" + receiverMail + ">\r\n"
clientSocket.send(rcptTo.encode())
recv7 = clientSocket.recv(1024)
print(recv7)
if recv7[:3] != b'250':
    print('250 reply not received from server.')
# Fill in end


# Send DATA command and print server response.
# Fill in start
data = "DATA\r\n"
clientSocket.send(data.encode())
recv8 = clientSocket.recv(1024)
print(recv8)
if recv8[:3] != b'354':
    print('354 reply not received from server.')
# Fill in end


# Send message data.
# Fill in start
message = "SUBJECT: " + subject + "\r\n" + msg + endmsg
clientSocket.send(message.encode())
recv9 = clientSocket.recv(1024)
print(recv9)
if recv9[:3] != b'250':
    print('250 reply not received from server.')
# Fill in end

# Send QUIT command and get server response.
Quit = "QUIT\r\n"
clientSocket.send(Quit.encode())
recv10 = clientSocket.recv(1024)
print(recv10)
if recv10[:3] != b'221':
    print('221 reply not received from server.')

clientSocket.close()
