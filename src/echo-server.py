#!/usr/bin/env python
import os
import sys
import ssl

from socket import socket, AF_INET, SOCK_STREAM

KEYFILE = 'resources/key.pem'
CERTFILE = 'resources/cert.pem'

def echo_client(s):
  while True:
    data = s.recv(8192)
    if data == b'': # Character stream ends
      break
    s.send(data)
  s.close()
  print('Connection closed.')

def echo_server(address):
  s = socket(AF_INET, SOCK_STREAM)
  s.bind(address)
  s.listen(1)

  # Server on SSL
  s_ssl = ssl.wrap_socket(s, keyfile=KEYFILE, certfile=CERTFILE, server_side=True)

  # Wait for connections
  while True:
    try:
      c,a = s_ssl.accept()
      echo_client(c)
    except Exception as e:
      print('{}: {}'.format(e.__class__.__name__, e))


def main():
  print('Starting echo server...')
  echo_server(('',20000))

if __name__ == '__main__':
  main()

