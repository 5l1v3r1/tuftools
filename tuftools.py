import sys
import argparse
import os
import httplib
import subprocess
import re
import urllib2
import socket
import urllib
import sys
import json
import telnetlib
import glob
import random
import Queue
import threading
import base64
import time
import ConfigParser
from sys import argv
from commands import *
from getpass import getpass
from xml.dom import minidom
from urlparse import urlparse
from optparse import OptionParser
from time import gmtime, strftime, sleep



# Color
W = '\033[1m'
R = '\033[31m'
N = '\033[0m'
G = '\033[32m'
B = '\033[34m'
Y = '\033[33m'

os.system('clear')


print R+"""                         

                                                                                @!@!@!@!@    
@@@@@@@@@@@                @@@@@@@@@  @@@@@@@@@@@                              @@@@@@@@@@@    
@@@@@@@@@@@  @@@      @@@  @@@@@@@@@  @@@@@@@@@@@                             !@!  
    @!@      @!@      @!@  @!@            @!@      @@@@@@     @@@@@@    @@@   !@!  
    !@!      !@!      !@!  !@!            !@!     @@@@@@@@   @@@@@@@@   @@@   !@!
    !!@      !!@      @!!  !!@!!@         !!@    !!@    @!! !!@    @!!  @!!      !!@!!@!!
    !!!      !!!      !!!  !!!!!!         !!!    !!!    !!! !!!    !!!  !!!              !!!
    !:!      !:!      !:!  !:!            !:!    !:!    !:! !:!    !:!  !:!              !:!
    ::!      ::!::::::!::  ::!            ::!    !::::::::! !::    ::!  !::::::: ::::::::!::     
    :::         ::::::     :::            :::       ::::       ::::     :::::::: ::::::::  
"""

print G+"""

(0) : exit tuftools

(1) : tufhammer (Dos attack)

(2) : tufscanner (Port scanners)

(3) : webattack (web url or ip info gather)

(4) : tufdos (A free Dos attack that u can execute right now)

"""

choice = raw_input('Choose a tool : ')
os.system('clear')
if choice == "1": os.system('git clone https://github.com/unkn0wnh4ckr/tufhammer')

if choice == "2": os.system('git clone https://github.com/unkn0wnh4ckr/tufscanner')

if choice == "3": os.system('git clone https://github.com/unkn0wnh4ckr/webattack')

if choice == "0": sys.exit()  
  
if choice == "4": os.system('cd ..')
os.system('python tufdos.py')

