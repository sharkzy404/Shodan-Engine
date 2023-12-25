import requests as re
import json as js
import os as os
import sys as sys
import time as tm
from bs4 import BeautifulSoup
from colorama import Fore as F
from os import system as sm

sm("clear")

name = """

               sharkk-OPEN SOURCE INTELLIGENCE[OSINT]-Shark
                        POWERED BY SHODAN.IO
"""
def run_name():
    print(F.YELLOW+name)


def shodan_menu():
    tm.sleep(1)
    text = """
          Input an option::

[01].Get host ip
[02].Get host count
[03].Host search
[04].Host search tokens
[05].Ports

[06].Dns lookup
[07].Dns reverse
[08].Honeyscore
[09].Shodan profile
[10].My ip

[11].Httpheader
[12].Api info
[13].Exploit author
[14].Exploit cve
[15].Exploit msb

[16].Exploit bid
[17].Exploit ovsdb
[18].Exploit title
[19].Exploit description
[20].Exploit date

[21].Exploit code
[22].Exploit platform
[23].Exploit port
[00].Exit program

"""
    print (F.GREEN+text)

def check_api_key():
    api = input(F.BLUE+"[∆]--Enter Valid API KEY--> "+F.WHITE)
    return api


def host_search(): #111111
    host_ip = input("Enter host ip: ")
    url = "https://api.shodan.io/shodan/host/"+host_ip+"?keys="+check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())


def get_host_count(): #222222
    host_search = input("Enter host search: ")
    url = "https://api.shodan.io/shodan/host/count?key="+check_api_key()+"&query="+host_search
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def get_host_search_count(): #333333
    host_count = input("Enter host search: ")
    url = "https://api.shodan.io/shodan/host/search?key="+ check_api_key()+"&query="+host_count
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())


def host_search_tokens(): #44444
    host_token = input("Enter token: ")
    url = "https://api.shodan.io/shodan/host/tokens?key="+check_api_key()+"&uery="+host_token
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())


def shodan_ports(): #5555
    url = "https://api.shodan.io/shodan/ports?key=" +check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_dns_lookup(): #6666
    hostnames = input("DNS Lookup : ")
    url = "https://api.shodan.io/dns/resolve?hostnames="+ hostnames +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_dns_reverse(): #7777
    ips = input("DNS Reverse : ")
    url = "https://api.shodan.io/dns/reverse?ips="+ ips +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_honeyscore(): #88888
    honeypot = input("DNS Reverse : ")
    url = "https://api.shodan.io/labs/honeyscore/"+honeypot +"&key="+check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_profile(): #9999
    url = "https://api.shodan.io/account/profile?key=" +check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_myip(): #10 10 10 10
    url = "https://api.shodan.io/tools/myip?key=" +check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_httpheaders(): #11 11 11
    url = "https://api.shodan.io/tools/httpheaders?key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_api_info(): #12 12 12
    url = "https://api.shodan.io/api-info?key=" +check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_author(): #13 13 13
    exploit_author = input("Exploit Author : ")
    url = "https://exploits.shodan.io/api/search?query= author: "+ exploit_author +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_cve(): #14 14 14
    exploit_cve = input("Exploit CVE : ")
    url = "https://exploits.shodan.io/api/search?query= cve:" + exploit_cve +"&key=" + shodan_api
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_msb(): #15 15 15
    exploit_msb = input("Exploit Microsoft Security Bulletin ID : ")
    url = "https://exploits.shodan.io/api/search?query= msb:" + exploit_msb +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_bid(): #16 16 16
    exploit_bid = input("Exploit Bugtraq ID : ")
    url = "https://exploits.shodan.io/api/search?query= bid:" + exploit_bid +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_osvdb(): #17 17 17
    exploit_osvdb = input("Exploit Open Source Vulnerability Database ID : ")
    url = "https://exploits.shodan.io/api/search?query= osvdb:" + exploit_osvdb +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_title(): #18 18 18
    exploit_title = input("Exploit Title : ")
    url = "https://exploits.shodan.io/api/search?query= title:" + exploit_title +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_description(): #19 19 19
    exploit_description = input("Exploit Description : ")
    url = "https://exploits.shodan.io/api/search?query= description:" + exploit_description +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_date(): #20 20 20
    exploit_date = input("Exploit Date : ")
    url = "https://exploits.shodan.io/api/search?query= description:" + exploit_date +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_code(): #21 21 21
    exploit_code = input("Exploit Code : ")
    url = "https://exploits.shodan.io/api/search?query= code:" + exploit_code +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_platform(): #22 22 22
    exploit_platform = input("Exploit Platform : ")
    url = "https://exploits.shodan.io/api/search?query= platform:" + exploit_platform +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodan_exploit_port(): #23 23 23
    exploit_platform = input("Exploit Port : ")
    url = "https://exploits.shodan.io/api/search?query= port:" + exploit_platform +"&key=" + check_api_key()
    request = re.get(url)
    txt = request.text
    soup = BeautifulSoup(txt, 'html.parser')
    for data in soup.find_all("body"):
       print (F.YELLOW+data.get_text())

def shodansploit_exit(): #24 24 24
    quit(0)


while True:
    run_name()
    shodan_menu()
    try:
        choice = int(input(F.CYAN+"[*]Enter option: "+F.WHITE))
        if choice == 1:
            host_search()
        elif choice == 2:
            get_host_count()
        elif choice == 3:
            get_host_search_count()
        elif choice == 4:
            host_search_tokens()
        elif choice == 5:
            shodan_ports()
        elif choice == 6:
            shodan_dns_lookup()
        elif choice == 7:
            shodan_dns_reverse()
        elif choice == 8:
            shodan_honeyscore()
        elif choice == 9:
            shodan_profile()
        elif choice == 10:
            shodan_myip()
        elif choice == 11:
            shodan_httpheaders()
        elif choice == 12:
            shodan_api_info()
        elif choice == 13:
             shodan_exploit_author()
        elif choice == 14:
            shodan_exploit_cve()
        elif choice == 15:
            shodan_exploit_msb()
        elif choice == 16:
            shodan_exploit_bid()
        elif choice == 17:
            shodan_exploit_osvdb()
        elif choice == 18:
            shodan_exploit_title()
        elif choice == 19:
            shodan_exploit_description()
        elif choice == 20:
            shodan_exploit_date()
        elif choice == 21:
            shodan_exploit_code()
        elif choice == 22:
            shodan_exploit_platform()
        elif choice == 23:
            shodan_exploit_port()
        elif choice == 00:
            shodansploit_exit()
        else:
            print ("error")
    except:
        print(F.RED+"[x] An Error Occured")
        tm.sleep(2)
        sm('clear')
