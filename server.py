from socket import *
import  os.path
# sys is being imported for command line arguments
import sys

#n_port is referred from array sys.argv
#try / except is used for exception handling if the user forgets to
#input the command line argument
try:
    n_port = int(sys.argv[1])  #indexes from the array sys.argv and
                               #converts that to an integer
    print("Successfully read n_port ")
except:
    print("Please input the <n_port> ")


#creating  a socket on the local port number
serverSocket= socket(AF_INET, SOCK_STREAM) #a server welcoming socket is created
                                                                                                      #with IPv4 TCP connection
serverSocket.bind(('', n_port)) #server socket is running using the local address
serverSocket.listen(1) #server begins listening for incoming TCP requests

while True:
    connectionSocket, addr=serverSocket.accept() #accepting the connection
    sentence = connectionSocket.recv(1024).decode() #receiving the sentence from client
    sentence_split = sentence.split() # splitting the string to form an array 
    command = sentence_split[0] #referring the exact command
    filename = sentence_split[1] # referring the exact filename
    flag =os.path.exists(filename) #checking if the file exists
    if (flag and command=="GET") or (not(flag) and command=="PUT"):
        connectionSocket.send("OK")
        print("ok")  #debugging statment
    else:
        connectionSocket.send("NOT OK") 
        print("not ok") #debugging statement
        continue
    
    recvAddressPort = connectionSocket.recv(1024).decode()
    client_address = (recvAddressPort.split())[0]
    r_port = int((recvAddressPort.split())[1])

    #Stage 2:
    #print(client_address)
    #print(r_port)
    transServerSocket = socket(AF_INET, SOCK_STREAM)
    #print("yo1")
    transServerSocket.connect((client_address, r_port))
    #print("yo2")
    #tried here

    if command=="GET":
        #the following part for sending was referred from
        # https://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
        f=open(filename, 'r')#file is being opened to be read into f
        li = f.read(1024)# f reads 1024 bytes at a time
        while(li):
            print("File is transferring ~~~")
            #transConnectionSocket, addr = transServerSocket.accept() #also tried here
            transServerSocket.send(li)
            li = f.read(1024)#sends the portions of the file in 1024 bytes
        f.close()#file is closed to prevent data loss from the source
        print("File is transferred successfully.")
        transServerSocket.close()#the transaction socket is being closed here

    elif command == "PUT":
        with open(filename, 'w') as f:#opening the file
            while True:
                print('Receiving file now ~~~')
                data = transServerSocket.recv(1024)# data is being transferred at 1024 bytes
                if not data:
                    break
                f.write(data)
        f.close()#closes the file, and 'w' automatically has the functionality to save the file in 
                  #the current directory
        print("File is received successfully.")
        transServerSocket.close()#the transaction socket is being closed here






        
        
        


    
    