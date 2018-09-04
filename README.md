# AzS - NetScan v1.0 

# About

The AzS - NetScan v1.0 is an open source application to scan network state of selected hosts.
Currently you can scan which hosts are online or which ports are open or closed.

The Application use the python nmap module to scan the network. 
The application is constantly under development.

Developed by Azhar Saeed Bhatti, Duesseldorf - Germany

Version: 1.0
Relase: 2018-09-04

# Licensing
AzS - NetScan v1.0 is licensed under the terms of the GNU General Public License Version 3, you will find a copy of this license in the LICENSE file included in the source package.


# Documentation

### Installation

### Set default Network for scan

To set a default network you have to add and delete the following lines:  
--       subnet = raw_input(bcolors.BOLD + "Please choose the network and subnet mask [192.168.0.0/24]: " + bcolors.ENDC)
--       nm.scan(subnet, arguments = ('-sP'))
++       nm.scan('192.168.70.0/24', arguments = ('-sP'))
