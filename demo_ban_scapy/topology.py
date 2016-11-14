#!/usr/bin/env python
from mininet.net import Mininet, VERSION
from mininet.log import setLogLevel, info, debug
from mininet.cli import CLI
from distutils.version import StrictVersion
from p4_mininet import P4Switch, P4Host
from time import sleep
import sys
from mininet.link import TCLink


SW_PATH='/home/abbie/bmv2/targets/simple_switch/simple_switch'
JSON_PATH='/home/abbie/my_demo/demo_ban_scapy/demo.json'


def main():
    net = Mininet(controller = None, autoSetMacs=True, autoStaticArp=True)

    h1 = net.addHost('h1', cls=P4Host)
    h2 = net.addHost('h2', cls=P4Host)
    h3 = net.addHost('h3', cls=P4Host)
    h4 = net.addHost('h4', cls=P4Host)

    s1 = net.addSwitch('s1', cls = P4Switch, sw_path=SW_PATH, json_path=JSON_PATH, thrift_port=9091)
    s2 = net.addSwitch('s2', cls = P4Switch, sw_path=SW_PATH, json_path=JSON_PATH, thrift_port=9092)
    s3 = net.addSwitch('s3', cls = P4Switch, sw_path=SW_PATH, json_path=JSON_PATH, thrift_port=9093)
    s4 = net.addSwitch('s4', cls = P4Switch, sw_path=SW_PATH, json_path=JSON_PATH, thrift_port=9094)

    net.addLink(s1, h1, port1=0, port2=0)
    net.addLink(s1, h2, port1=1, port2=0)
    net.addLink(s1, s2, port1=2, port2=0)
    net.addLink(s1, s3, port1=3, port2=0)
    net.addLink(s1, h4, port1=4, port2=0)

    net.addLink(s2, s4, port1=1, port2=0)

    net.addLink(s3, s4, port1=1, port2=1)

    net.addLink(s4, h3, port1=2, port2=0)


    net.start()
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('debug')
    main()
