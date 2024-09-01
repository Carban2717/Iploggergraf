import os
import requests

# Renkli metinler için escape kodları
BLUE = '\033[94m'
RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[97m'
RESET = '\033[0m'

# Admin şifresi
ADMIN_PASSWORD = "graftooladminkey"

# Admin log dosyası
LOG_FILE = "admin_log.txt"

def clear_screen():
    os.system('clear')  # Terminal ekranını temizler

def display_menu():
    clear_screen()
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
    print(f"{GREEN}[03] Admin Girişi{RESET}")

def ip_sorgulatma():
    clear_screen()
    print(f"{WHITE}IP:{RESET}")
    ip = input()
    if ip.count('.') == 3 and all(part.isdigit() for part in ip.split('.')):  # Basit IP adresi doğrulama
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            print(f"{WHITE}IP: {data.get('ip', 'N/A')}{RESET}")
            print(f"{WHITE}City: {data.get('city', 'N/A')}{RESET}")
            print(f"{WHITE}Region: {data.get('region', 'N/A')}{RESET}")
            print(f"{WHITE}Country: {data.get('country', 'N/A')}{RESET}")
            print(f"{WHITE}Org: {data.get('org', 'N/A')}{RESET}")
            with open(LOG_FILE, 'a') as log_file:
                log_file.write(f"IP sorgulandı: {ip}\n")
                log_file.write(f"IP bilgileri: {response.text}\n")
        else:
            print(f"{RED}API hatası.{RESET}")
    else:
        print(f"{RED}Geçerli bir IP adresi girmediniz.{RESET}")

def admin_girisi():
    clear_screen()
    print(f"{RED}Admin Password:{RESET}")
    password = input()
    if password == ADMIN_PASSWORD:
        print(f"{GREEN}Admin girişi başarılı.{RESET}")
        while True:
            clear_screen()
            with open(LOG_FILE, 'r') as log_file:
                print(log_file.read())
            input("\nDevam etmek için bir tuşa basın...")
    else:
        print(f"{RED}Yanlış şifre. Menüye dönülüyor.{RESET}")

if __name__ == "__main__":
    while True:
        display_menu()
        secim = input("Bir seçenek girin: ")

        if secim == "1":
            exit()
        elif secim == "2":
            ip_sorgulatma()
        elif secim == "3":
            admin_girisi()
        else:
            print(f"{RED}Geçerli bir seçenek girin.{RESET}")
