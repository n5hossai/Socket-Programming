Naymul Hossain 
CS 436
20746760

 ***How to compile and run the programs?***

 ~ Firstly log in to username@ubuntu1804-002.student.cs.uwaterloo.ca (I used putty)
 ~ Create a directory for server
 ~ Put the file server.py and cat.txt here
 ~ Similarly, log in to username@ubuntu1804-008.student.cs.uwaterloo.ca
 ~ Create a directory for client
 ~ Put the file client.py and dog.txt here

^^RUNNING the program^^
 ~ in the server directory from username@ubuntu1804-002.student.cs.uwaterloo.ca, tpye:
 python server.py 42080
 ~ Then, in the server directory from username@ubuntu1804-002.student.cs.uwaterloo.ca, tpye:
 python client.py ubuntu1804-002.student.cs.uwaterloo.ca 42080
 ~ Now, input the command GET/PUT, and then filename.txt e.g.:
 GET cat.txt
 or 
 PUT dog.txt 
 ~ If the filename you want to get does not appear in the server side, or 
 the file you want to put does not appear in the client side, then 
 the Enter your command line will appear again.
 Else, "Now creating server socket" line gets on the screen and file transfer updates begin to appear 





 ***Where & Which machines?***

 ~ For server side, username@ubuntu1804-002.student.cs.uwaterloo.ca
 ~ For client side, username@ubuntu1804-008.student.cs.uwaterloo.ca

 (one computer was used during the development and testing of these two files)





 ***What are the executables and parameters?*** 

 ~ executables : 
                -client.py
                -server.py
 ~ parameters :
                - <portnumber> in the example 42080 was used for running server.py
                - <server_address> in the example was used was ubuntu1804-002.student.cs.uwaterloo.ca for running client.py
                - <portnumber> in the example 42080 was used for running client.py


