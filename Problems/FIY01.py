# python script to get username, hostname, and private IP of your machine
#and ti fetch public ip address and your location.

#importing necessary packages.

import json
import socket
import getpass
from urllib.request import urlopen

#get the username of your machine

username = getpass.getuser()
print("username : ", username)

#get the hostname of your machine

hostname = socket.gethostname()
print("hostname :", hostname)

# get the ip address of your machine

machineIP = socket.gethostbyname(hostname)
print("IP Address :", machineIP)

# get the public ip address and the location
# open the url and store the response

url = "http://ipinfo.io/json"
response = urlopen(url)

# converting JSON encoded response into python objects
data = json.load(str(response))

# fecthing and displaying necessary data
print("Public IP :", data["ip"])
print("city :", data["city"])
print("state :", data['region'])
print("country :", data["country"])


