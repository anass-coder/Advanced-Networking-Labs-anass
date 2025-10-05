#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller
from mininet.cli import CLI
from mininet.log import setLogLevel, info

def build_net():
    net = Mininet(controller=Controller)

    info('*** Adding controller\n')
    net.addController('c0')

    info('*** Adding hosts\n')
    PC1 = net.addHost('PC1')          # no IP here (set later)
    PC2 = net.addHost('PC2')
    PC3 = net.addHost('PC3')
    PC4 = net.addHost('PC4')

    info('*** Adding switches\n')
    s14 = net.addSwitch('s14')
    s24 = net.addSwitch('s24')
    s34 = net.addSwitch('s34')

    info('*** Creating links\n')
    # Order of links defines interface numbering (eth0, eth1, ...)
    net.addLink(PC1, s14)   # PC1-eth0
    net.addLink(PC4, s14)   # PC4-eth0

    net.addLink(PC2, s24)   # PC2-eth0
    net.addLink(PC4, s24)   # PC4-eth1

    net.addLink(PC3, s34)   # PC3-eth0
    net.addLink(PC4, s34)   # PC4-eth2

    info('*** Starting network\n')
    net.start()

    # Optional: open xterms for each PC
    info('*** Opening xterms\n')
    PC1.cmd('xterm -T PC1 &')
    PC2.cmd('xterm -T PC2 &')
    PC3.cmd('xterm -T PC3 &')
    PC4.cmd('xterm -T PC4 &')

    info('*** Drop into CLI\n')
    CLI(net)

    info('*** Closing xterms\n')
    for h in (PC1, PC2, PC3, PC4):
        h.cmd('killall xterm')

    info('*** Stopping network\n')
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    build_net()
