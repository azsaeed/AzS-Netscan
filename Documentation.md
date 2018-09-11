
# Documentation

These documentation describe how to install and use the AzSa - NetScan.  
It assumes that you are familiar with the operating system which you are using to install.  
Here is used CentOS version 7 and Python version 2.7. 


## Installation
##### Clone or download NetScan:  
`# git clone https://github.com/azsaeed/azsa-netscan.git`

##### Change permission:   
`# chmod 744 run.py`

##### Install python nmap module  
###### auto:  
`# pip install python-nmap`  

###### manual:  
The nmap package is also includes in the source package.  
Or download it: https://xael.org/norman/python/python-nmap/  
`# tar -xf python-nmap.tar`     
`# python setup.py install`   

##### Install nmap package 
`# yum install nmap`     


## Run 
To run the scanner you have to execute the file run.py   
`# .\run.py`   

When the scanner is started you can choose the follow option from the navigation:  
 `# 1.Start -- 2.Help -- 3.Info -- 0.Exit`

To scan you have to choose the option:   
`# Please select [0-3]: 1`  

Next you have to add the subnet with the subnet mask in CIDR format:   
`# Please choose the network and subnet mask [192.168.0.0/24]: 192.168.0.0/24`

After you have added a subnet the scanner will scan all hosts in the subnet and display the result:  
`# 192.168.0.1`  
`# 192.168.0.2`

Choose one of the displayed host and enter it:  
`# Please enter a address: 192.168.0.2`  

Next you can choose one the following options:   
`# Custom:[1-65635]`  
`# Well-known ports:[well]`  
`# All ports:[all]`   

You can enter a custom single port or you can scan for the well-known or all ports by typing well or all.  
`# Please select a option: 22`  


##### Output 
`# Nmap 6.40 scan initiated Tue Sep  4 15:18:07 2018 as: nmap -oX - -oN /tmp/info.txt -p22 192.168.70.87    
Nmap scan report for 192.168.0.2  
Host is up (0.0013s latency).  
PORT   STATE SERVICE  
22/tcp open  ssh  
MAC Address: 00:0C:29:B7:01:B4 (VMware)  
Nmap done at Tue Sep  4 15:18:07 2018 -- 1 IP address (1 host up) scanned in 0.29 seconds #` 

The last output will also concurrently save the in the file /tmp/info.txt.  
After the output the scanner will ask you for check more hosts. There you can choose y or n.   
If you will choose y the scanner display the searched hosts again else it will exit. 



