import socket
import os.path as path
import sys

if __name__=='__main__':
  print('Relative file location:',end=' ')
  file_path=input()
  curr_path=path.abspath(path.dirname(__file__))
  req_file=path.join(curr_path,file_path)
  if not path.exists(req_file):
    raise ValueError('Unable to locate file')
  file_name, file_ext = path.splitext(req_file)
  file_name=file_name.split('/')[-1]
  print('Receiver IP:',end=' ')
  host=input()
  port=55555
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    s.connect((host, port))
    s.send('{}-{}-{}'.format(file_name,file_ext,path.getsize(req_file)).encode('utf-8'))
  except:
    raise ValueError('Receiver unable to accept connection')
  print('Connected to server')
  size=0
  with open(req_file,'rb') as file:
    data=''
    for line_in in file:
      size+=len(line_in)
      s.send(line_in)
      print('Sending...')
    print('Transmit Size ',size)
  s.shutdown(socket.SHUT_WR)
  data=s.recv(1024).decode('utf-8')
  print(data)
  s.close()