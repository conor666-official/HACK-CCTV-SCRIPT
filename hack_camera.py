#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, re, requests, signal, sys, colorama

colorama.init()

# ========== HEADER ==========
print('Checking Update...')
os.system('git pull')
os.system('clear')

# Colors
red="\033[0;31m"
green="\033[0;32m"
blue="\033[0;34m"
cyan="\033[0;36m"
yellow="\033[0;33m"
purple="\033[0;35m"
white="\033[0;37m"

# Banner
print(green+'''
⠀⠀⢀⣤⣤⣠⣤⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣿⣿⡿⠟⠿⠿⢿⣿⣷⣶⣤⣶⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣿⣿⣿⠀⠀⠀⠀⠀⠙⠛⢻⣿⣿⣿⣿⣿⣦⣀⡀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠙⢿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⢿⣿⣿⣦⣤⣤⣄⡀⠀⢀⣄⠉⠙⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠛⢿⣿⣿⣿⣿⣿⣿⣧⣤⡟⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣩⣿⣿⣿⣿⣿⣿⣿⣿⣾⣏⢀⡤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠋⣙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣰⡿⣷⣶⣦⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠋⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡿⠀⣿⣿⣿⣿⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⠋⢉⣿⣿⣿⣿⣿⣿⣿⣿⡿⢿⠀⠘⣿⣿⣿⣿⣷⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢉⣬⡿⢿⣿⣿⠛⢿⠗⠀⠀⠀⠈⢿⣿⣿⣿⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠟⠉⠀⠀⠈⠙⠁⠀⠀⠀⠀⠀⠀⠀⠙⠻⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠓⠀⠀⠀⠀⠀⠀⠀⠀⠀
''')

print(green+'%37s' % '   |Developed By : Conor 666')
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
print(blue+'Youtube Channel:kunal_yt10')
print(blue+'Telegram Group : https://t.me/+qP6jaApocvEzZTU1')
print(red+'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

# ========= PRINT COUNTRY MENU =========
print(green+'1) United States            47) Singapore')
print('2) Japan                    48) Iceland')
print('3) Italy                    49) Malaysia')
print('4) Korea                    50) Colombia')
print('5) France                   51) Tunisia')
print('6) Germany                  52) Estonia')
print('7) Taiwan                   53) Dominican Republic')
print(cyan+'8) Russian Federation       54) Slovenia')
print('9) United Kingdom           55) Ecuador')
print('10) Netherlands             56) Lithuania')
print('11) Czech Republic          57) Palestinian')
print('12) Turkey                  58) New Zealand')
print('13) Austria                 59) Bangladesh')
print('14) Switzerland             60) Panama')
print(red+'15) Spain                   61) Moldova')
print('16) Canada                  62) Nicaragua')
print('17) Sweden                  63) Malta')
print('18) Israel                  64) Trinidad And Tobago')
print('19) Iran                    65) Saudi Arabia')
print('20) Poland                  66) Croatia')
print('21) India                   67) Cyprus')
print('22) Norway                  68) Pakistan')
print('25) Belgium                 69) United Arab Emirates')
print('26) Brazil                  70) Kazakhstan')
print('27) Bulgaria                71) Kuwait')
print('28) Indonesia               72) Venezuela')
print(yellow+'29) Denmark                 73) Georgia')
print('30) Argentina               74) Montenegro')
print('31) Mexico                  75) El Salvador')
print('32) Finland                 76) Luxembourg')
print('33) China                   77) Curacao')
print('34) South Africa            78) Puerto Rico')
print('35) Slovakia                79) Costa Rica')
print('36) Hungary                 80) Belarus')
print('37) Ireland                 81) Albania')
print(purple+'38) Egypt                   82) Philippines')
print('39) Thailand                83) Nepal')
print('40) Ukraine                 84) Peru')
print('41) Serbia                  85) Uruguay\n')

# ========= COUNTRY CODE LIST =========
countries = ["US","JP","IT","KR","FR","DE","TW","RU","GB","NL",
             "CZ","TR","AT","CH","ES","CA","SE","IL","PL","IR",
             "NO","IN","BE","BR","BG","ID","DK","AR","MX","FI",
             "CN","ZA","SK","HU","IE","EG","TH","UA","RS","HK",
             "GR","PT","LV","SG","IS","MY","CO","TN","EE","DO",
             "SI","EC","LT","PS","NZ","BD","PA","MD","NI","MT",
             "TT","SA","HR","CY","PK","AE","KZ","KW","VE","GE",
             "ME","SV","LU","CW","PR","CR","BY","AL","LI","BA",
             "PY","PH","NP","PE","UY"]

headers = {"User-Agent":"Mozilla/5.0"}

# ========= GLOBAL VAR =========
collected_ips = []
country_code = "Unknown"

# ========= SIGNAL HANDLER =========
def save_and_exit(sig, frame):
    if collected_ips:
        filename = f"{country_code}.txt"
        with open(filename, "w") as f:
            for ip in collected_ips:
                f.write(ip + "\n")
        print(f"\n{green}[✔] Saved {len(collected_ips)} IPs to {filename}{white}")
    else:
        print(f"\n{red}[!] No IPs collected, nothing saved.{white}")
    sys.exit(0)

signal.signal(signal.SIGINT, save_and_exit)

# ========= MAIN =========
try:
    num = int(input("\nOPTIONS : "))
    if num not in range(1, len(countries)+1):
        raise IndexError

    country_code = countries[num-1]
    res = requests.get(f"http://www.insecam.org/en/bycountry/{country_code}", headers=headers)
    last_page = re.findall(r'pagenavigator\("\?page=", (\d+)', res.text)[0]

    for page in range(int(last_page)):
        res = requests.get(f"http://www.insecam.org/en/bycountry/{country_code}/?page={page}", headers=headers)
        find_ip = re.findall(r"http://\d+\.\d+\.\d+\.\d+:\d+", res.text)
        for ip in find_ip:
            if ip not in collected_ips:
                collected_ips.append(ip)
                print(red, ip)

except Exception as e:
    print(red, f"[!] Error: {e}", white)
finally:
    save_and_exit(None, None)
