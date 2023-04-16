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

def Setoolkit():
    os.system("setoolkit")

def Locked_Scanner_TR():
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

    startup_TR()

def Locked_Scanner_EN():
    target = input(str("Hedef IP: "))
    #banner
    print("_" * 50)
    print("Target IP: " + target)
    print("Scanning "+ str(datetime.now())+" Start")
    print("_" * 50)
    #Tarama
    try:
        #Test All Ports
        for port in range(1,65535):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)
            #Açık portları tespit et
            result = s.connect_ex((target,port))
            if result == 0:
                print("[*] Port {} is open".format(port))
                s.close()
    except KeyboardInterrupt:
        print("\n Exiting bye bye :(")
        sys.exit()
    except socket.error:
        print("\n Target not response ?")
        sys.exit()

    startup_EN()




def WifiScan():
    os.system("airmon-ng start wlan0")
    time.sleep(10)
    os.system("airodump-ng wlan0mon")

def Nmap_Scanning_TR():

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
    startup_TR()

def Nmap_Scanning_EN():

    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535
    open_ports = []
    while True:
        ip_add_entered = input("\nEnter Target IP Adress: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} Invalid IP Adress")
            break
    while True:
        print("Scanning Ports: <int>-<int> (ex would be 60-120)")
        port_range = input("Enter Port: ")
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
            print(f"Port is closed {port}.")
    startup_EN()


        
def IP_Scan_TR():
    try:
        ip = "192.168.1.0"
        ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
        while True:
            ip_add_range_entered = "192.168.1.0/24"
            if ip_add_range_pattern.search(ip_add_range_entered):
                print(f"{ip_add_range_entered} geçerli bir ip adresi aralığıdır")
                break

        arp_result = scapy.arping(ip_add_range_entered)
        
    except KeyboardInterrupt:
        print("Çıkış Yapılıyor...")
        startup_TR()


def IP_Scan_EN():
    try:
        ip = "192.168.1.0"
        ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")
        while True:
            ip_add_range_entered = "192.168.1.0/24"
            if ip_add_range_pattern.search(ip_add_range_entered):
                print(f"{ip_add_range_entered} Scanning")
                break

        arp_result = scapy.arping(ip_add_range_entered)
        
    except KeyboardInterrupt:
        print("Exiting...")
        startup_EN()



def Sherlock_Scan_TR():
    try:
        username = input("Kullanıcı Adı Giriniz: ")
        os.system("python3 \Sherlock/sherlock.py --timeout 1 "+username)
    except KeyboardInterrupt:
        print("Exiting...")
        startup_TR()  
    
def Sherlock_Scan_EN():
    try:
        username = input("Enter Username: ")
        os.system("python3 \Sherlock/sherlock.py --timeout 1 "+username)
    except KeyboardInterrupt:
        print("Exiting...")
        startup_EN()


def Torghost_TR():
    try:
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
    except KeyboardInterrupt:
        print("Exiting...")
        startup_TR()
def Torghost_EN():
    try:
        print("_" * 50)
        print("What you want for torghost?")
        print("1-)Create Connection")
        print("2-)Disconnect")
        print("_" * 50)
        selection = int(input("Değer Giriniz: "))
        if selection == 1:
            os.system("python3 ghost.py -s")
        elif selection == 2:
            os.system("python3 ghost.py --stop")    
    except KeyboardInterrupt:
        print("Exiting...")
        startup_EN()

def clear():
    os.system("clear")

def firststartup():
    if os.geteuid() != 0:
        exit("Bu script'in çalışması için root olmanız gerek.\nIf you want to run this script you need to be root.")
        
    print("=" * 50)
    print("What Language You Use?")
    print("=" * 50)
    print("_" * 50)
    print("1-)TR-Türkçe")
    print("2-)EN-English")
    print("_" * 50)
    print("\n")
    option = int(input("Your Selection: "))
    try:
        if option == 1:
                clear()
                Turkish()
                 
        elif option == 2:
                clear()
                English()

    except KeyboardInterrupt:
        print("bye bye :(")

def banner():
    ascii_banner = pyfiglet.figlet_format("LOCKED Multi-Tool")
    print(ascii_banner)
    print("Creator Erdal'Lockedw'Konuk")


def back_TR():
    Turkish()
def back_EN():
    English()

def startup_TR():
    print("*" * 50)
    cont = str(input("Devam Etmek istiyor musunuz? E/h: "))
    if cont.lower() == "e":
        os.system("clear")
        firststartup()
        Turkish()
    elif cont == "":
        os.system("clear")
        Turkish()
        cont = str(input("Seçtiğiniz Değer: "))
    elif cont.lower() == "h":
        sys.exit()


def startup_EN():
    print("*" * 50)
    cont = str(input("Do you want to continue? E/h: "))
    if cont.lower() == "e":
        os.system("clear")
        firststartup()
        English()
    elif cont == "":
        os.system("clear")
        English()
        cont = str(input("Your Selection: "))
    elif cont.lower() == "h":
        sys.exit()


def Turkish():
        try:
            clear()
            banner()
            print("_" * 50)
            print("1-)Tarama Saldırıları")
            print("2-)Sosyal Mühendislik Saldırıları")
            print("3-)Gizlen")
            print("_" * 50)
            option = int(input("Seçtiğiniz Değer: "))
            if option == 1:
                clear()
                banner()
                print("1-)Port Taraması(Lockedw)")
                print("2-)Port Taraması(NMAP)")
                print("3-)IP Taraması")
                print("4-)WıFı Taraması(WiFi Kartı Gerekli)")
                print("5-)Geri)")
                option = int(input("Seçtiğiniz Değer: "))
                if option == 1:
                    Locked_Scanner_TR()
                    startup_TR()
                elif option == 2:
                    Nmap_Scanning_TR()
                    startup_TR()
                elif option == 3:
                    IP_Scan_TR()
                    startup_TR()
                elif option == 4:
                    WifiScan()
                    startup_TR()
                elif option == 5:
                    clear()
                    back_TR()
            elif option == 2:
                clear()
                banner()
                print("1-)Kullanıcı Adı Taraması(Sherlock)")
                print("2-)Sosyal Mühendislik tool-kit")
                print("3-)Geri")
                option = int(input("Seçtiğiniz Değer: "))
                if option == 1:
                    Sherlock_Scan_TR()
                    startup_TR()
                elif option == 2:
                    Setoolkit()
                    startup_TR()
                elif option == 3:
                    clear()
                    back_TR()
            elif option == 3:
                clear()
                banner()
                print("1-)Gizlenmek İçin Torghost Kullan")
                print("2-)Geri")
                option = int(input("Seçtiğiniz Değer: "))
                if option == 1:
                    Torghost_TR()
                    startup_TR()
                elif option == 2:
                    clear()
                    back_TR()

        except KeyboardInterrupt:
            clear()
            print("Bye bye :(")
            sys.exit()

def English():
        try:
            clear()
            banner()
            print("_" * 50)
            print("1-)Scan attacks")
            print("2-)Social Engineering Attacks")
            print("3-)Be Hidden")
            print("_" * 50)
            option = int(input("Your Selection: "))
            if option == 1:
                clear()
                banner()
                print("1-)Port Scanning(Lockedw)")
                print("2-)Port Scanning(NMAP)")
                print("3-)IP Scanning")
                print("4-)WıFı Scanning(Its need wifi card)")
                print("5-)Back")
                option = int(input("Your Selection: "))
                if option == 1:
                    Locked_Scanner_EN()
                    startup_EN()
                elif option == 2:
                    Nmap_Scanning_EN()
                    startup_EN()
                elif option == 3:
                    IP_Scan_EN()
                    startup_EN()
                elif option == 4:
                    WifiScan()
                    startup_EN()
                elif option == 5:
                    clear()
                    back_EN()
            elif option == 2:
                clear()
                banner()
                print("1-)Username Reverse Search Attack(Sherlock)")
                print("2-)Social Engineering ToolKit")
                print("3-)Back")
                option = int(input("Your Selection: "))
                if option == 1:
                    Sherlock_Scan_EN()
                    startup_EN()
                elif option == 2:
                    Setoolkit()
                    startup_EN()
                elif option == 3:
                    clear()
                    back_EN()
            elif option == 3:
                clear()
                banner()
                print("1-)Use Torghost For Hidden")
                print("2-)Back")
                if option == 1:
                    Torghost_EN()
                    startup_EN()
                elif option == 2:
                    clear()
                    back_EN()

        except KeyboardInterrupt:
            clear()
            print("Bye bye :(")
            sys.exit()



clear()
banner()
firststartup()


