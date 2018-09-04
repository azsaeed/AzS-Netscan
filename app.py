#!/usr/bin/python
import os, sys, re, nmap
from classes import bcolors

def app ():


        nm = nmap.PortScanner()

        subnet = raw_input(bcolors.BOLD + "Please choose the network and subnet mask [192.168.0.0/24]: " + bcolors.ENDC)


        if subnet == 0:
                exit()
        else:
        # scan subnet
                nm.scan(subnet, arguments = ('-sP'))

#       set a default network and netmask
#       nm.scan('192.168.70.0/24', arguments = ('-sP'))

                h = nm.all_hosts()

        # add a list
                listh = []

        # output hosts in list
                for hosts in h:
                        listh.append(hosts)
                        print hosts


                host = raw_input(bcolors.BOLD + "Please enter a address: " + bcolors.ENDC)

                for item in listh:
                        m1 = re.search(host, item)

                        if m1:
                                p = str((input( bcolors.BOLD + "Please select a port: " + bcolors.ENDC)))
                                s = nm.scan(host, arguments = ('-oN /tmp/info.txt -p' + p))
                                print(open("/tmp/info.txt").read())
                                break

                else:
                        print (bcolors.FAIL + "No machtes found!" + bcolors.ENDC)

app()
