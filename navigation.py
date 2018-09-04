#!/usr/bin/python

from classes import bcolors

def navi():

        print bcolors.WARNING + "Navigation:" + bcolors.ENDC
        print bcolors.BOLD + "1.Start -- 2.Help -- 3.Info -- 0.Exit\n" + bcolors.ENDC
        try:
                number = input("Please select [0-3]: ")
        except SyntaxError:
                number = None

        if number == 1:
                import app

        elif number == 2:
                print "-----------------------------------------------------------------"
                print bcolors.WARNING + "Help" + bcolors.ENDC
                print "-----------------------------------------------------------------\n"

                print "First you have to select 1.Start in the navaigation to start the scaner.\nAfter the app is started, next you have to add a subnet with the subnetmask in CIDR format:\n192.168.0.0/24.\n"
                print "Next the scanner will search and dispay all online hosts in the selected network.\nThen You can choose one of the host with the ip address and port to get the more details.\n"
                print "Concurrently the sniffer save the last output in the file /tmp/info.txt\n"

                print "For more help and information please visit: xxxx \n"

                b = raw_input(bcolors.WARNING + "<<< Back - Please press *Enter* " + bcolors.ENDC)
                print "Enter"
                if b == "":
                        navi()

        elif number == 3:
                print "-----------------------------------------------------------------"
                print bcolors.WARNING + "Info" + bcolors.ENDC
                print "-----------------------------------------------------------------\n"
                print "The AzS - NetScan v1.0 is an open source application to scan network state of selected hosts.\nCurrently you can scan which hosts are online or which ports are open or closed.\n"
                print "The Application use the python nmap module to scan the network.\nThe application is constantly under development.\n"

                print "AzS - NetScan v1.0 is licensed under the terms of the GNU General Public License Version 2,\nyou will find a copy of this license in the COPYING file included in the source package.\n"

                print "Developed by Azhar Saeed Bhatti, Duesseldorf - Germany\n"
                print "GitHub: xxx"
                print "Version: 1.0\nRelase: 2018-09-19\n"

                print "For more help and information please visit: xxxx \n"

                b1 = raw_input(bcolors.WARNING + "<<< Back - Please press *Enter* " + bcolors.ENDC)
                if b1 == "":
                        navi()
        elif number == 0:
                print  bcolors.BOLD + "EXIT" + bcolors.ENDC
                exit()


        else:
                print bcolors.FAIL + "No matches available!\n" + bcolors.ENDC
                navi()
navi()
