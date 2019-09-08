#!/usr/bin/env python3
# Sender
#Bret Boyer
import os.path
import socket
import random
from random import shuffle
import time
import sys


BUFFER = 4096
HOST = ''
PORT = 8888
def main():


    print('This is the UDP Client')
    print('This program is designed to run on a local machine')
    while True:
        HOST = str(input('Please enter the IP address to send to: '))
        if HOST == '' or HOST == '127.0.0.1' or HOST == 'localhost':
            break


        else:
            print('Try again... ')




    # Set up our sending socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#DGRAM means UDP
    clientsocket.bind((HOST, PORT)) #sending from this port


    #files that will be sent
    files = [
        'file0.txt','file1.txt','file2.txt','file3.txt',
        'file4.txt','file5.txt','file6.txt','file7.txt',
        'file8.txt','file9.txt',
        ]




    fNum = {} #^^^files will be added to this
    j = 0
    #dictionary has number of lines in file that have been sent
    for j in range(len(files)):
        fNum[files[j]] = 0


    #Get the amount of lines that are to be sent per file
    linesToSend = 0
    for num in range(len(files)):
        l = fileLines(files[num])
        linesToSend = linesToSend + l




    #randomize files to send
    shuffleFiles = files
    shuffle(shuffleFiles)




    for f in range(len(shuffleFiles)):


        if shuffleFiles[f] in files and '.txt' in shuffleFiles[f] :
            print(shuffleFiles[f])
            linesToRead = numOfLines()#how many lines should we send
            fNum[shuffleFiles[f]] = linesToRead


            with open(shuffleFiles[f], 'r') as textFile:#open textfile
                fn = str(shuffleFiles[f]) #file name sent


                for line in range(linesToRead):
                    data = textFile.readline() #line to read from file
                    print(data, end = '')
                    clientsocket.sendto(fn.encode('UTF-8'),('localhost', 7777))#sends filename


                    print(fn, end = '')
                    clientsocket.sendto(data.encode('UTF-8'),('localhost', 7777)) #sending to this port


                #if fNum[shuffleFiles[f]] == 3:
                    #shuffleFiles[f] = 'fileSent'#replace file that has been completely sent
                    #print(shuffleFiles)
        time.sleep(.1)
    #first wave of data sent


    #Send all data that wasn't sent before
    for sendAll in range(len(shuffleFiles)):
        lineSent = fNum[shuffleFiles[sendAll]]


        with open(shuffleFiles[sendAll]) as sendData:
            allLines = sendData.readlines()
            while True:
                try:
                    sendFN = str(shuffleFiles[sendAll])
                    data = allLines[lineSent]
                    if data == '': #end of file go back
                        break
                    print(sendFN)
                    print(data, end='')
                    clientsocket.sendto(sendFN.encode('UTF-8'), ('localhost', 7777))
                    clientsocket.sendto(data.encode('UTF-8'), ('localhost', 7777))
                    lineSent = lineSent + 1
                except IndexError: #incase line sent goes higher than lines available
                    break
    stop = 'quit'#I've sent everything
    clientsocket.sendto(stop.encode('UTF-8'), ('localhost', 7777)) #Kill send process
    clientsocket.sendto(stop.encode('UTF-8'), ('localhost', 7777)) #Kill send process


    #receiving all files
    data = ''
    with open('allFiles.txt', 'w') as allFiles:
        while data != 'quit':
            data, address = clientsocket.recvfrom(BUFFER)
            data = data.decode('UTF-8')
            if data == 'quit':
                continue
            allFiles.write(data)
            print(data, end = '')




#lines in a file
def fileLines(fn):
    with open(fn) as f:
        for i, line in enumerate(f):
            pass
    return i+1




def numOfLines():
    num = (random.randint(1,3))
    return num


if __name__ == '__main__':
    main()