import os
import requests

# Renkli metinler için escape kodları
BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[97m'
RESET = '\033[0m'

def display_menu():
    os.system('clear')
    print(f"{BLUE}   _____ _____            ______ _______ ____   ____  _      {RESET}")
    print(f"{BLUE}  / ____|  __ \     /\   |  ____|__   __/ __ \ / __ \| |     {RESET}")
    print(f"{BLUE} | |  __| |__) |   /  \  | |__     | | | |  | | |  | | |     {RESET}")
    print(f"{BLUE} | | |_ |  _  /   / /\ \ |  __|    | | | |  | | |  | | |     {RESET}")
    print(f"{BLUE} | |__| | | \ \  / ____ \| |       | | | |__| | |__| | |____ {RESET}")
    print(f"{BLUE}  \_____|_|  \_\/_/    \_\_|       |_|  \____/ \____/|______|{RESET}")
    print(f"{RED}  _____ _____    _      ____   _____  _____ ______ _____  {RESET}")
    print(f"{RED} |_   _|  __ \  | |    / __ \ / ____|/ ____|  ____|  __ \ {RESET}")
    print(f"{RED}   | | | |__) | | |   | |  | | |  __| |  __| |__  | |__) |{RESET}")
    print(f"{RED}   | | |  ___/  | |   | |  | | | |_ | | |_ |  __| |  _  / {RESET}")
    print(f"{RED}  _| |_| |      | |___| |__| | |__| | |__| | |____| | \ \ {RESET}")
    print(f"{RED} |_____|_|      |______\____/ \_____|\_____|______|_|  \_\\{RESET}")
    print(f"{GREEN}[01] Çık{RESET}")
    print(f"{GREEN}[02] IP Sorgulatma{RESET}")

def ip_sorgulatma(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json")
    if response.status_code == 200:
        data = response.json()
        print(f"{WHITE}IP: {data.get('ip', 'N/A')}{RESET}")
        print(f"{WHITE}City: {data.get('city', 'N/A')}{RESET}")
        print(f"{WHITE}Region: {data.get('region', 'N/A')}{RESET}")
        print(f"{WHITE}Country: {data.get('country', 'N/A')}{RESET}")
        print(f"{WHITE}Org: {data.get('org', 'N/A')}{RESET}")
    else:
        print(f"{RED}Geçersiz IP adresi veya API hatası.{RESET}")

if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Bir seçenek girin: ")
        if choice == "1":
            exit()
        elif choice == "2":
            os.system('clear')
            ip = input(f"{WHITE}IP: {RESET}")
            ip_sorgulatma(ip)
            input("\nDevam etmek için bir tuşa basın...")
        else:
            print(f"{RED}Geçerli bir seçenek girin.{RESET}")
