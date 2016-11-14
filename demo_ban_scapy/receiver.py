#!/usr/bin/env python
import sys
import struct
from scapy.all import sniff
from subprocess import call
import time
import os


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
    
    if cnt>10:
        '''
        if os.stat("test1_cmd.txt").st_size == 0 :
            cmd="echo table_add bad_lookup _drop 8 =\> >> test1_cmd.txt"
        else:
            cmd= "cat test1_cmd.txt | sed '0a table_add bad_lookup _drop 1 =\>' > test1_cmd.txt"
        '''

        # cmd="echo table_add bad_lookup _drop 1 =\> >> test1_cmd.txt"
        f = open('test1_cmd.txt', 'w')
        f.seek(0,0)
        f.write("table_add bad_lookup action_bad_lookup 1 => 4")
        f.close()
        # call(cmd,shell=True)
    
    sys.stdout.flush()

def main():
    from sys import argv
    if len(argv) < 2:
        print "Usage receiver.py [host number]"
        return
    
    iface = "h%s-eth0" % (argv[1], )
    print "Listen on %s" % (iface, )
    
    global start
    start = time.time()
    sniff(iface = iface, prn = lambda x: handle_pkt(x))


if __name__ == '__main__':
    main()



