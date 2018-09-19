#!/bin/python3

import math, os, re, subprocess

def mac():
    mac.mac_input = input('Please enter MAC address:\n')
    while not re.match('^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$', mac.mac_input):
       mac.mac_input = input('Incorrect MAC! Please enter valid MAC address:\n')

def ip():
    ip.ip_input = input('Please enter IP address:\n')
    while not re.match('^(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9])\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[1-9]|0)\.(25[0-5]|2[0-4][0-9]|[0-1]{1}[0-9]{2}|[1-9]{1}[0-9]{1}|[0-9])$', ip.ip_input):
        ip.ip_input = input('Incorrect IP! Please enter valid IP address:\n')

def dept(path):
    fpath = '/root/python/' + path
    while not os.path.isfile(fpath):
        print("Non-existant department. Please enter a valid department.\n")

def addClient(name,mac,ip,dept):
    s = '''host %s {\n        hardware ethernet %s;\n        fixed-address %s;\n}\n''' % (name,mac,ip)
    f = open(dept, "a")
    f.write(s)
    f.close

name = input('Please enter a name:\n')
mac()
ip()

dept_input = input('Please enter a department:\n')
dept(dept_input)

addClient(name,mac.mac_input,ip.ip_input,dept_input)
