#!/usr/bin/python
from scapy.all import *
from time import sleep
from random import randint
import time


start = 0
end = 0
elapsed = 0

def main():

    from sys import argv
    if len(argv) < 2:
        print "Usage sender.py [host number] [sleep time]"
        return

    count = 1
    iface = "h%s-eth0" % (argv[1], )
    dst = 3
    
    while(1):
        # p1 = "\x00" + chr(int(argv[1])) + "\x00" + chr(dst) + "Hello from h%s -> %d" % (argv[1],count, )
        p = Ether(dst="00:00:00:00:00:03",src="00:00:00:00:00:01") / IP() / TCP() / "aaaaaaaaaaaaaaaaaaa"
        
        '''does't work
        ether = "\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x01\x08\x00"
        ip = "\x04\x05\x00\x00\x3B\x00\x01\x00\x00\x40\x06\x7C\xBA\x7F\x00\x00\x01\x7F\x00\x00\x01"
        # p2 = ether + ip + "Hello!!! from h%s -> %d" % (argv[1],count, )     
        '''
        global start
        global end
        global elapsed

        ether = "\x00\x03\x00\x01\x08\x00"
        ip = "\x06\x7F\x00\x00\x01\x7F\x00\x00\x01"
        payload = "a"*1400
        print payload,"~~",len(payload)
        # ip = "\x45\x00\x06\x7F\x00\x00\x01\x7F\x00\x00\x01"
        p2 = ether + ip + payload +"Hello!!! from h%s -> %d" % (argv[1],count, )
        # hexdump(p)
        # hexdump(p2)
        print p2
        print "Send 1 Packet to h%d -> %d " % (dst,count, )
        count += 1

        start = time.time()
        sendp(p2, iface = iface, verbose=0)
        #sendpfast(p, pps=1000,iface = iface)
        
        
        sleep(float(argv[2]))
        end = time.time()
        elapsed = end - start
        print "Time taken: ", elapsed, "seconds."

if __name__ == '__main__':
    main()
