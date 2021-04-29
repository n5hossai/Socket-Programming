# Implementation of TCP socket programming in a client-server enivormnet

### How to compile and run the programs?

 1. Firstly log in to one of your accessed servers **Host1**, wiht your credentials (I used putty)
 2. Create a directory for server
 3. Put the file server.py and cat.txt here
 4. Similarly, log in to another server with a different host id, say **Host2**, so as to demonstrate the socket programming
 5. Create a directory for client
 6. Put the file client.py and dog.txt here

### RUNNING the program
 1. in the server directory from **Host1**, tpye:
 python server.py 42080  (basically any port number greater than 1023)
 2. Then, in the server directory , tpye:
 python client.py  **Host1** 42080
 3. Now, input the command GET/PUT, and then filename.txt e.g.:
 GET cat.txt
 or 
 PUT dog.txt 
 4. If the filename you want to get does not appear in the server side, or 
 the file you want to put does not appear in the client side, then 
 the Enter your command line will appear again.
 Else, "Now creating server socket" line gets on the screen and file transfer updates begin to appear 




 ### What are the executables and parameters?

 + executables : 
                - client.py
                - server.py
 + parameters :
                - <portnumber> in the example 42080 was used for running server.py
                - <server_address> in the example my institution's server was used for running client.py
                - <portnumber> in the example 42080 was used for running client.py


Please email me at nnaymul2@gmail.com if to ask more questions or make it better. Thank you

