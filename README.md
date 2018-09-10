# AzSa - NetScan v1.0 

# About

The AzSa - NetScan v1.0 is an open source application to scan network state of selected hosts.
Currently you can check which hosts are online or which ports are open or closed.

The Application use the python nmap module to scan the network.
The application is constantly under development.

AzSa - NetScan v1.0 is licensed under the terms of the GNU General Public License Version 3,
you will find a copy of this license in the LICENSE file included in the source package.

Developed by Azhar Saeed Bhatti, Duesseldorf - Germany  

Version: 1.0  
Relase: 2018-09-19  


# Licensing
AzSa - NetScan v1.0 is licensed under the terms of the GNU General Public License Version 3, you will find a copy of this license in the LICENSE file included in the source package.


# Documentation

### Installation
Clone or download:  
git clone https://github.com/azsaeed/azsa-netscan.git 

change permission: # chmod 744 run.py   
Install python nmap module  
auto:  
yum -y install python-pip   
pip install python-nmap  

manual:  
download: https://xael.org/norman/python/python-nmap/  
tar -xf python-nmap.tar   
python setup.py install  


#### Run the scanner 
.\run.py 

Navigation:
1.Start -- 2.Help -- 3.Info -- 0.Exit

  Please select [0-3]: 1  
  Please choose the network and subnet mask [192.168.0.0/24]: 192.168.0.0/24  
  Please enter a address: 192.168.0.0  
  Please select a port: 22   

Nmap 6.40 scan initiated Tue Sep  4 15:18:07 2018 as: nmap -oX - -oN /tmp/info.txt -p22 192.168.70.87  
Nmap scan report for 192.168.70.87  
Host is up (0.0013s latency).  
PORT   STATE SERVICE  
22/tcp open  ssh  
MAC Address: 00:0C:29:B7:01:B4 (VMware)  
Nmap done at Tue Sep  4 15:18:07 2018 -- 1 IP address (1 host up) scanned in 0.29 seconds  

