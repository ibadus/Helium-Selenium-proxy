
# HELIUM
from helium import *
# SELENIUM
from selenium import webdriver
# PROXY
from utility.chrome_proxy_driver_setup import ChromeProxySetup as CPS
from utility.extension_clean_up import cleanUp
# OS
import os
# TIME
import time

# VAR FOR THE PROXY PARTS
proxies = []
ip = []
port = []
username = []
psw = []

# PATH TO THE PROXIES.TXT FILE
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
proxies_file = os.path.join(THIS_FOLDER, 'proxies.txt')
#OPEN THE PROXIES.TXT AND READ LINE BY LINE TO GET THE INFOS
file = open(str(proxies_file), "r")
for line in file:
    prox = line.rstrip("\n")
    prox = prox.split(":")
    ip.append(prox[0])
    port.append(prox[1])
    username.append(prox[2])
    psw.append(prox[3])
    proxies.append(line.rstrip("\n"))
file.close()

# LOAD PROXY
proxy_1 = CPS(ip[0],port[0],username[0],psw[0])
# START SELENIUM BROWSER WITH PROXY
driver = proxy_1.set_proxy()
# CHANGE SELENIUM TO HELIUM 
set_driver(driver)
# GO TO AN URL
go_to('https://www.google.fr/')
# TRY TO CLICK (SEE IF HELIUM IS WORKING)
click("J'ai de la chance")
time.sleep(5)
# CLEAN THE BROWSER
cleanUp(True).clean_extensions()