# 5. Write a script that  system information like distro info, memory(total, used, free), CPU info (model, core numbers, speed), current user, system load average, and IP address. Use arguments for specifying resources. (For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address).


import argparse
import psutil
import subprocess
import getpass
import socket
import platform

parser = argparse.ArgumentParser()

parser.add_argument("-d", action="store_true",
   help="show distribution")
parser.add_argument("-m", action="store_true",
   help="show memory info")
parser.add_argument("-c", action="store_true",
   help="show cpu info")
parser.add_argument("-u", action="store_true",
   help="show user info")
parser.add_argument("-l", action="store_true",
   help="show load average")
parser.add_argument("-i", action="store_true",
   help="show IP adress")
args = parser.parse_args()

if args.d:
    release = subprocess.run(['grep', '-E', '^(VERSION|NAME)=', '/etc/os-release'], 
                             capture_output=True, text=True)
    print(release.stdout)

if args.m:
    mem = psutil.virtual_memory()
    print("MEMORY - TOTAL: ", mem.total/1024/1024) # in MB
    print("MEMORY - USED: ", mem.used/1024/1024)
    print("MEMORY - FREE: ", mem.free/1024/1024)
if args.c:
    # cpu_cores - czy logiczne czy fizyczne
    print("CPU CORES:" , psutil.cpu_count(logical=False))
    print("CPU FREQ: ", psutil.cpu_freq())
if args.u:
    print("USER: ", getpass.getuser())
if args.l:
    print("LOAD AVERAGE: ", psutil.getloadavg())
if args.i:
    print("IP: ", socket.gethostbyname(socket.gethostname()))



