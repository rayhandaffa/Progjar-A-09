#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter08/queuepi.py
# Small application that uses several different message queues

import random, threading, time, zmq, sqlite3, os, sys, hashlib

def randomizer():
    """Express `n` in at least `d` binary digits, with no special prefix."""
    # return bin(random.getrandbits(digits)).lstrip('0b').zfill(digits)
    return str(random.randint(0, 2))

def query(num):
    db = sqlite3.connect("data.db")
    cur = db.cursor()

    total = 0
    value = 0
    # for i in range(1000):
    n1 = random.randint(1, 99000)
    n2 = random.randint(1, 1000)
    mod = "length(FirstNameLastName)"
    sql = "select count(*) from MOCKDATA where (ID>={} AND ID<={}) AND {} % 3 = {};".format(n1, n1+n2, mod, num)
    # print(n1,n2)
    h = hash(sql)
    if h % 2 == 0:
        hasil = "n1 = {}, n2 = {}, num = {}, hasil = nol".format(n1, n2, num)
    else:
        cur.execute(sql)
        value = int(cur.fetchone()[0])
    
    total += value

    hasil = "n1 = {}, n2 = {}, num = {}, hasil = {}".format(n1, n2, num, total)

    db.close()

    return hasil

def generator(zcontext, url):
    """Produce random points in the unit square."""
    zsock = zcontext.socket(zmq.PUB)
    zsock.bind(url)
    while True:
        zsock.send_string(randomizer())
        time.sleep(5)

def executor_0(zcontext, in_url, out_url):
    """Coordinates in the lower-left quadrant are inside the unit circle."""
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    isock.setsockopt(zmq.SUBSCRIBE, b'0')
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    while True:
        hasil_generator=isock.recv_string()
        print(hasil_generator)
        hasil = query(hasil_generator)
        osock.send_string(hasil)

def executor_1(zcontext, in_url, out_url):
    """Coordinates in the lower-left quadrant are inside the unit circle."""
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    isock.setsockopt(zmq.SUBSCRIBE, b'1')
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    while True:
        hasil_generator=isock.recv_string()
        print(hasil_generator)
        hasil = query(hasil_generator)
        osock.send_string(hasil)

def executor_2(zcontext, in_url, out_url):
    """Coordinates in the lower-left quadrant are inside the unit circle."""
    isock = zcontext.socket(zmq.SUB)
    isock.connect(in_url)
    isock.setsockopt(zmq.SUBSCRIBE, b'2')
    osock = zcontext.socket(zmq.PUSH)
    osock.connect(out_url)
    while True:
        hasil_generator=isock.recv_string()
        print(hasil_generator)
        hasil = query(hasil_generator)
        osock.send_string(hasil)

def tally(zcontext, url):
    """Tally how many points fall within the unit circle, and print pi."""
    zsock = zcontext.socket(zmq.PULL)
    zsock.bind(url)
    # p = q = 0
    # while True:
    hasil = zsock.recv_string()
        # q += 1
        # if decision == 'Executor 0 Jalan':
        #     p += 4
        # elif decision == 'Executor 1 Jalan':
        #     p += 2
        # elif decision == 'Executor 2 Jalan':
        #     p += 1
    print(hasil)

def start_thread(function, *args):
    thread = threading.Thread(target=function, args=args)
    thread.daemon = True  # so you can easily Ctrl-C the whole program
    thread.start()

def main(zcontext):
    pubsub = 'tcp://127.0.0.1:6700'
    # reqrep = 'tcp://127.0.0.1:6701'
    pushpull = 'tcp://127.0.0.1:6702'
    # start_thread(bitsource, zcontext, pubsub)
    # start_thread(always_yes, zcontext, pubsub, pushpull)
    # start_thread(judge, zcontext, pubsub, reqrep, pushpull)
    # start_thread(pythagoras, zcontext, reqrep)
    # start_thread(tally, zcontext, pushpull)
    # time.sleep(30)
    # while True:
    start_thread(generator, zcontext, pubsub)
    start_thread(executor_0, zcontext, pubsub, pushpull)
    start_thread(executor_1, zcontext, pubsub, pushpull)
    start_thread(executor_2, zcontext, pubsub, pushpull)
    start_thread(tally, zcontext, pushpull)
    time.sleep(5)

if __name__ == '__main__':
    main(zmq.Context())