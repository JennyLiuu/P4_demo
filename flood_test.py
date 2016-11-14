#!/usr/bin/python
import sys
from scapy.all import *
print "Field Values of packet sent"
p=IP(dst="10.0.0.1",id=1111,ttl=99)/TCP(sport=RandShort(),dport=3636,seq=12345,ack=1000,window=1000,flags="S")
print "Sending Packets in 0.3 second intervals for timeout of 4 sec"
ans,unans=srloop(p,inter=0.3,retry=2,timeout=4)
print "Summary of answered & unanswered packets"
ans.summary()
unans.summary()