from socket import *

# sys is being imported for command line arguments
import sys
import random

while True:
#server_address and n_port are given in order. so it is referred
#accordingly from the array sys.argv
#try / except is used for exception handling if the user forgets to
#input the command line arguments
    try:
        server_address = sys.argv[1]
        n_port = int(sys.argv[2])#indexes from the array sys.argv and
                                 #converts that to an integer
        print("Successfully read server_address and n_port ")
    except:
        print("Please input the <server_address> and <n_port> in the correct order ")

    clientSocket = socket(AF_INET, SOCK_STREAM) #creates a TCP socket using <server_address>
                                                                                                      #as the server address and <n_port> as the
                                                                                                      #negotiation port number (where the server is listening)
    clientSocket.connect((server_address, n_port))
    sentence = raw_input('Enter your command: ') #user is asked to input command GET or PUT then <filename>
    clientSocket.send(sentence.encode()) #client sends the request with command and filename
    #waits for the server to send ok
    recvd_sentence = clientSocket.recv(1024)
    if (recvd_sentence == "NOT OK"): # this break occurs when the request had some problems
        continue
    # print ("everything good until transaction socket") #debugging statement
    if(recvd_sentence == "OK"):
        print("Now creating server socket") #to indicate request was valid and 
                                           #server socket will now be created
    

    transSocket = socket(AF_INET, SOCK_STREAM) # transaction socket is being made
    transSocket.bind(('', 0)) # the transSocet is bound with a random port number and local host
    transSocket.listen(1) # starts listening for incoming requests
    

    addressPort = transSocket.getsockname() #retrieves the port number and address tuple
    client_address = gethostname() #retrieves the hostname of here
    sendAddressPort = (client_address)+ " " +str(addressPort[1]) # string is being processed before sending
    clientSocket.send(sendAddressPort.encode()) # client_address and port is being sent
    #print("yo3")
    #print(addressPort[0])
    transClConnectionSocket, addr = transSocket.accept() #accepts the connection 
    #print("yo4")

    #Stage 2:
    sentence_split = sentence.split() # splitting the string to form an array 
    command = sentence_split[0] #referring the exact command
    filename = sentence_split[1] # referring the exact filename

    if command == "GET":
        with open(filename, 'w') as f: #opening the file 
            while True:
                print('Receiving file now ~~~')
                data = transClConnectionSocket.recv(1024) # data is being transferred at 1024 bytes
                if not data: #when all the data have been read, the while loop breaks
                    break
                f.write(data)
        f.close() #closes the file, and 'w' automatically has the functionality to save the file in 
                  #the current directory
        print("File is received successfully.")
        transClConnectionSocket.close() #the transaction socket is being closed here

    elif command=="PUT":
        #the following part for sending file was referred from
        # https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
        f=open(filename, 'r') #file is being opened to be read into f
        li = f.read(1024) # f reads 1024 bytes at a time
        while(li):
            print("File is transferring ~~~")
            transClConnectionSocket.send(li)
            li = f.read(1024) #sends the portions of the file in 1024 bytes
        f.close() #file is closed to prevent data loss from the source
        print("File is transferred successfully.")
        transClConnectionSocket.close()#the transaction socket is being closed here



    
    







