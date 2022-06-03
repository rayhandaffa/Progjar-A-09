#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter18/rpyc_server.py
# RPyC server

import rpyc
import os, glob, shutil

def main():
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port = 18861)
    t.start()

class MyService(rpyc.Service):
    def exposed_line_counter(self, fileobj, function):
        print('Client has invoked exposed_line_counter()')
        for linenum, line in enumerate(fileobj.readlines()):
            function(line)
        return linenum + 1

    def exposed_ls(self, path):
        print('Client has invoked exposed_ls()')
        if len(path) == 1:
            return os.listdir('.')
        else:
            return os.listdir(path[1])

    def exposed_get(self, path):
        print('Client has invoked exposed_get()')
        pesan = " ".join(path[1:-1])
        pesanGet = pesan + '/' + path[-1]

        f = open(pesanGet, "rb")
        b = f.read()
        #print(len(b))
        f.close()
        shutil.copy(pesanGet, r'client')

        results = "fetch: {} size: {} lokal: {}".format(pesan, len(b), path[-1])
        return results
    
    def exposed_count(self, path):
        print('Client has invoked exposed_count()')
        listFile=glob.glob(path[1])
        results = len(listFile)
        return results
    
    def exposed_put(self, data, path):
        print('Client has invoked exposed_put()')
        shutil.copy(data, path)
        return "successed put {} to {}".format(data, path)

    def exposed_quit(self):
        print('Client has invoked exposed_quit()')
        
        return "Hati-hati Di Jalan"


if __name__ == '__main__':
    main()