#!/usr/bin/python
import os, sys, re, nmap
from classes import bcolors

#Initialize nmap programm
nm = nmap.PortScanner()

#Add subnet function
def addsub():
        print (bcolors.FAIL +"Exit[x]"+ bcolors.ENDC)
        subnet = raw_input(bcolors.BOLD + "Please choose the network and subnet mask [192.168.0.0/24]: " + bcolors.ENDC)

        if subnet == "":
                print("No subnet added!")
                addsub()
        elif subnet == "x":
                print (bcolors.BOLD + "EXIT" + bcolors.ENDC)
                exit()
        else:

                nm.scan(subnet, arguments = ('-sP -T5'))
                global h
                h = nm.all_hosts()
                global listh
                listh = []

#Search hosts and ports function
def app():

        # output hosts in list
        for hosts in h:
                listh.append(hosts)
                print hosts
        if not listh:
                print("No result!\nMaybe wrong network information.\nPlease try it again or read the help!")
                addsub()

        else:
                host = raw_input(bcolors.BOLD + "Please enter a address: " + bcolors.ENDC)


                for item in listh:

                        m1 = re.search(host, item)
                        if m1:
                                print (bcolors.WARNING + "Custom:[1-65635]\nWell-known ports:[well]\nAll ports:[all]" + bcolors.ENDC)
                                p = raw_input(bcolors.BOLD + "Please select a option: " + bcolors.ENDC)

                                m2 = re.search("all", p)
                                m3 = re.search("well", p)
                                if m2:
                                        s = nm.scan(host, arguments = ('-oN /tmp/info.txt -p-'))
                                        print(open("/tmp/info.txt").read())
                                        break
                                elif m3:
                                        s = nm.scan(host, arguments = ('-oN /tmp/info.txt -p 1-1023'))
                                        print(open("/tmp/info.txt").read())
                                        break

                                elif p > 0:
                                        s = nm.scan(host, arguments = ('-oN /tmp/info.txt -p' + p))
                                        print(open("/tmp/info.txt").read())
                                        break


                else:
                        print (bcolors.FAIL + "No machtes found!" + bcolors.ENDC)


        more = raw_input(bcolors.OKGREEN + "Do you want check more hosts? [y|n]: " + bcolors.ENDC )
        if more == "y":
                app()

        elif more == "n":
                print("EXIT")
                exit()




addsub()
app()
