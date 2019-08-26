import socket
import os
import sys

def Main():
  host='192.168.10.84'
  port=55555

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind((host,port))
  print("server Started")
  s.listen(1)
  while True:
      size=0
      c, addr = s.accept()
      print("Connection from: " + str(addr))
      info=c.recv(1024).decode('utf-8').split('-')
      print(info)
      filename = open('demo{}'.format(info[1]), "wb")
      data=c.recv(1024)
      size+=len(data)
      while data:
        filename.write(data)
        data = c.recv(1024)
        print('Receiving...')
        size+=len(data)
      print('Received Size: ',size)
      filename.close()
      # if size!=int(info[2]):
        # raise ValueError('Unable to receive full file')
      c.send('Received {} bytes'.format(size).encode('utf-8'))
      c.close()

if __name__ == '__main__':
    Main()