import socket
import os
import sys
import json

def InitializeConnection(c, url):
  sendMessage=json.dumps({"url":url})
  c.send('200 OK {}'.format(len(sendMessage)).encode('utf-8'))
  print('Size', c.recv(100).decode('utf-8'))
  c.send(sendMessage.encode('utf-8'))
  message=c.recv(1024).decode('utf-8').split(' ')
  if message[0]==110:
    return 0
  else:
    InitializeConnection(c,url)


def Main():
  host='192.168.10.84'
  port=55555
  url=input('Download URL: ')
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host,port))
  print("Server started")
  s.listen(1)
  c, addr = s.accept()
  print("Connection from: " + str(addr))
  loopCounter=0 #replace later
  while loopCounter<10:
    message=c.recv(1024).decode('utf-8').split(' ')
    if message[0]=='100' and message[1]=='HELO':
      print('Client {} connected'.format(addr[0]))
      InitializeConnection(c, url)
      loopCounter+=1
    else:
      raise Exception('Client Error')
  c.close()
  s.close()

if __name__ == '__main__':
    Main()
