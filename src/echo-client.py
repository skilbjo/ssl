#!/usr/bin/env python
import os
import sys
import ssl
import argparse

from socket import socket, AF_INET, SOCK_STREAM

CERTFILE = 'resources/cert.pem'

def echo_request(text_payload):
  s = socket(AF_INET, SOCK_STREAM)
  s_ssl = ssl.wrap_socket(s, cert_reqs=ssl.CERT_REQUIRED, ca_certs=CERTFILE)
  s_ssl.connect(('localhost', 20000))
  # s_ssl.send(b'Hello?')
  s_ssl.send(text_payload.encode('utf-8'))
  print(s_ssl.recv(8192))
  # s.close()
  # print('Connection closed.')

def main(text_payload):
  print('Client here, Sending a ping to the server.')
  echo_request(text_payload)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='echo client')
  parser.add_argument('-d','--data', help='what do you want to echo?', required=True)

  args = parser.parse_args()

  main(args.data)
