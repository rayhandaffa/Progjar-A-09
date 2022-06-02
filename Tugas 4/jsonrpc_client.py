#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_client.py
# JSON-RPC client needing "pip install jsonrpclib-pelix"

import sys
from jsonrpclib import Server

def main():
    proxy = Server('http://localhost:7002')
    while True:
        msg = input(">  ")
        msgSplit=msg.split()
        if(msgSplit[0]=="ls"):
            print(proxy.ls(msg))

        elif(msgSplit[0]=="get"):
            print(proxy.get(msg))
        elif(msgSplit[0]=="count"):
            print(proxy.count(msg))
        elif(msgSplit[0]=="quit"):
            proxy.quit()
            proxy('close')()
            return
        
    # print(proxy.lengths((1,2,3), 27, {'Sirius': -1.46, 'Rigel': 0.12}))

if __name__ == '__main__':
    main()