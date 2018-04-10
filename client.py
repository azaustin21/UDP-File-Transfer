from socket import *

serverName = 'localhost'
serverPort = 12000
receiverIsReceiving = False
clientSocket = socket(AF_INET, SOCK_STREAM)
ACK = '0'
closingMessage = 'end trans'

def main():
    clientSocket.connect((serverName,serverPort))
    receiverIsReceiving = True
    i = 0

    sentence = raw_input("enter to start")

    while receiverIsReceiving:
        clientSocket.send(ACK)
        recv = clientSocket.recv(1024)
        print recv
        i = i + 1
        if i > 11:
            receiverIsReceiving = False
            clientSocket.send(closingMessage)
            clientSocket.close()

if __name__ == '__main__':

    main()