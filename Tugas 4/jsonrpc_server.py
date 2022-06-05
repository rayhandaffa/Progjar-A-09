#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/jsonrpc_server.py
# JSON-RPC server needing "pip install jsonrpclib-pelix"

import glob
import shutil
from time import sleep
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer

def ls(*args):
    List=""
    results=[]
    msgSplit=args[0].split()
    if(len(msgSplit)== 1):
        listFile=glob.glob("./*")
    else:
        msgL = "".join(msgSplit[1:])
        listFile = glob.glob(msgL)
    for i in listFile:
        List += i +"\n"
    results = List
    return results

def count(*args):
    results=[]
    msgSplit=args[0].split()
    msgL = "".join(msgSplit[1:])
    listFile=glob.glob(msgL)
    results = len(listFile)
    return results

def get(*args):
    results = []
    msgSplit=args[0].split()
    pesan = " ".join(msgSplit[1:-1])
    pesanGet = pesan + '/' + msgSplit[-1]

    f = open(pesanGet, "rb")
    b = f.read()
    f.close()
    shutil.copy(pesanGet, r'client')
    results = "fetch: {} size: {} lokal: {}".format(pesan, len(b), msgSplit[-1])
    return results

def put(*args):
    results = []
    msgSplit=args[0].split()
    namaFile = msgSplit[1]
    namaTujuan = msgSplit[2]
    shutil.copy(namaFile, namaTujuan)
    return "successed put {} to {}".format(namaFile, namaTujuan)

def quit(*args):
    print("Quitting Client")
    return "Client shutting down"

def main():
    server = SimpleJSONRPCServer(('localhost', 7002))
    server.register_function(quit)
    server.register_function(get)
    server.register_function(ls)
    server.register_function(put)
    server.register_function(count)
    print("Starting server")
    server.serve_forever()

if __name__ == '__main__':
    main()