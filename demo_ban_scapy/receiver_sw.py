#!/usr/bin/env python
import sys
import struct
from scapy.all import *
from subprocess import call
import time

to_hex = lambda x:" ".join([hex(ord(c)) for c in x])
cnt = 0
start = 0
end = 0
elapsed = 0

def handle_pkt(pkt):
    
    pkt = str(pkt)
    if(len(pkt) > 40): return  # filter unexpect packet

    msg = pkt[4:]
    
    global cnt
    global start
    global end
    global elapsed

    cnt+=1
    end = time.time()
    elapsed = end - start
    print "Time taken: ", elapsed, "seconds." , "packet rate: " , (cnt/elapsed)
    print "Msg:%s , cnt:%d \n" % (msg,cnt)
    hexdump(pkt)
    '''
    if cnt==3:
        cmd="echo table_add bad_lookup _drop 1 =\> >> test1_cmd.txt"
        call(cmd,shell=True)
    '''
    sys.stdout.flush()

def main():
    from sys import argv
    if len(argv) < 2:
        print "Usage receiver.py [host number]"
        return

    iface = "s%s-eth%s" % (argv[1],argv[2] )
    print "Listen on %s" % (iface, )

    global start
    start = time.time()
    sniff(iface = iface, prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
