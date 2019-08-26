import socket
import os.path as path
import sys
import threading
import json
import requests

def download(url):
  with requests.get(url, stream=True) as r:
    with open('demo.mp4', 'wb') as f:
      for chunk in r.iter_content(chunk_size=8192): 
        if chunk:
          f.write(chunk)

def createSocket():
  host='192.168.10.84'
  port=55555
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    print('Initialzing Connection......')
    s.connect((host, port))
    s.send('100 HELO'.encode('utf-8'))
  except:
    raise ValueError('Connection Error')
  message=s.recv(2048).decode('utf-8')
  print(message)
  urllen=int(message.split(' ')[2])
  s.send('150 {}'.format(urllen).encode('utf-8'))
  info=json.dumps(s.recv[urllen+1].decode('utf-8'))
  # print(info)
  down_thread=threading.Thread(target=download, args=(info['url'],))
  down_thread.start()
  s.shutdown(socket.SHUT_WR)
  data=s.recv(1024).decode('utf-8')
  print(data)
  s.close()


if __name__=='__main__':
  createSocket()
  
  
