from socket import *

serverName = 'localhost'
serverPort = 12000
receiverIsReceiving = False
clientSocket = socket(AF_INET, SOCK_STREAM)
ACK = '0'
closingMessage = 'end trans'

def main():
    clientSocket.connect((serverName,serverPort))   # connect
    clientSocket.settimeout(2.0)
    receiverIsReceiving = True
    i = 0
    ACK = '0'
    sentence = raw_input("enter to start")

    while receiverIsReceiving:
        try:
            clientSocket.send(ACK)         #tell the server what we are expecting
            recv = clientSocket.recv(1024)
            sequenceNumber = recv[-1:]
            print recv[:-1]

            if sequenceNumber == ACK:  # if we got the packet we were expecting,
                if ACK == '0':
                    ACK = '1'
                else:
                    ACK = '0' #switch ACK so we are expecting the next packet

                i = i + 1
                if i > 5:
                    receiverIsReceiving = False
                    clientSocket.send(closingMessage)
                    clientSocket.close()

            elif sequenceNumber != ACK:  #if we got the wrong packet, send for the proper one
                clientSocket.send(ACK)
        except timeout:
            print 'timeout notice'
            clientSocket.send(ACK)
            print ACK

if __name__ == '__main__':
    main()
