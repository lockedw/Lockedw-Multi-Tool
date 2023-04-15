import subprocess
import scapy.all as scapy
import pyfiglet 
import socket
import sys
from datetime import datetime 
import nmap
import re
import os
import time

def Normal_Tarama():
    target = input(str("Hedef IP: "))
    #banner
    print("_" * 50)
    print("Taranan Hedef: " + target)
    print("Tarama "+ str(datetime.now())+"'da Başladı...")
    print("_" * 50)
    #Tarama
    try:
        #Tüm portları tes et
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            #Açık portları tespit et
            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] Port {} is open".format(port))
                s.close()
    except KeyboardInterrupt:
        print("\n Çıkış Yapılıyor bye bye :(")
        sys.exit()
    except socket.error:
        print("\n Kaynak Cevap Vermiyor ?")
        sys.exit()

    startup()

def WifiScan():
    os.system("airmon-ng start wlan0")
    time.sleep(10)
    os.system("airodump-ng wlan0mon")

def Nmap_Tarama():

    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535
    open_ports = []
    while True:
        ip_add_entered = input("\nTaramak istediğiniz ip adresini giriniz: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} Geçersiz ip adress")
            break
    while True:
        print("Taramak istediğiniz port aralığı: <int>-<int> (ex would be 60-120)")
        port_range = input("Port Aralığı Giriniz: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
        nm = nmap.PortScanner()
    for port in range(port_min, port_max + 1):
        try:       
            result = nm.scan(ip_add_entered, str(port))      
            port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
            print(f"Port {port} is {port_status}")
        except:
            print(f"Tarama Yapılamıyor port kapalı {port}.")
    startup()
        
def WIFI_SCAN():
    ip = "192.168.1.0"
    ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
    while True:
        ip_add_range_entered = "192.168.1.0/24"
        if ip_add_range_pattern.search(ip_add_range_entered):
            print(f"{ip_add_range_entered} geçerli bir ip adresi aralığıdır")
            break

    arp_result = scapy.arping(ip_add_range_entered)
    startup()

def Sherlock():
    username = input("Kullanıcı Adı Giriniz: ")
    os.system("python3 \Sherlock/sherlock.py --timeout 1 "+username)
    startup()


def torghost():
    print("_" * 50)
    print("Torghost ile ne yapmak istersiniz?")
    print("1-)Bağlantı Kur")
    print("2-)Bağlantı Kes")
    print("_" * 50)
    selection = int(input("Değer Giriniz: "))
    if selection == 1:
        os.system("python3 ghost.py -s")
    elif selection == 2:
        os.system("python3 ghost.py --stop")
    
    startup()

def firststartup():
    if os.geteuid() != 0:
        exit("Bu script'in çalışması için root olmanız gerek.\nLütfen bu sefer 'sudo' kullanarak tekrar deneyin.")
    print("=" * 50)
    print("Ne yapmak istiyorsunuz?")
    print("=" * 50)
    print("\n")
    print("_" * 50)
    print("1-)Port Taraması(Normal)")
    print("2-)Port Taraması(NMAP)")
    print("3-)IP Taraması")
    print("4-)Username Taraması(Sherlock)")
    print("5-)TOR Protokolü kullanarak ip değiştir")
    print("6-)Wifi Taraması")
    print("_" * 50)
    print("\n")
    option = int(input("Seçtiğiniz Değer: "))

    if option ==1:
        Normal_Tarama()
    elif option ==2:
        Nmap_Tarama()
    elif option ==3:
        WIFI_SCAN()
    elif option == 4:
        Sherlock()
    elif option == 5:
        torghost()
    elif option == KeyboardInterrupt:
        print("good bye")
    elif option == 6:
        WifiScan()

def banner():
    ascii_banner = pyfiglet.figlet_format("LOCKED SCANNER")
    print(ascii_banner)
    print("Creator Erdal'Lockedw'Konuk")

def startup():
    print("^" * 50)
    print("Sonuçlar") 
    cont = input("Programa Devam Etmek İstiyor Musunuz? E/h: ")
    if cont.lower() == "e":
        os.system("clear")
        firststartup()
        option = int(input("Seçtiğiniz Değer: "))
    elif cont == "":
        os.system("clear")
        firststartup()
        option = int(input("Seçtiğiniz Değer: "))
    elif cont.lower() == "h":
        sys.exit()

banner()
firststartup()


