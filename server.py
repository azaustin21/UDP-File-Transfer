from socket import *

serverPort = 12000
sequenceNumber = 0
nextPacketToSend = 0
closingMessage = 'end trans'
receivng = False

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('',serverPort))
    serverSocket.listen(1)
    print 'READY TO WORK'

    while True:
        connectionSocket, addr = serverSocket.accept()
        receiving = True
        while receiving == True:

            connectionSocket, addr = serverSocket.accept()
            recv = connectionSocket.recv( 1024 )
            connectionSocket.send( recv + ' got it' )

            if recv == closingMessage:
                connectionSocket.close()
                receiving = False

if __name__ == '__main__':

    main()