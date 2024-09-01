import os
import time
import requests
from colorama import Fore, init

init(autoreset=True)

# Kullanıcı işlemlerini takip etmek için bir liste
user_activity_log = []

# IP sorgulama log dosyası
LOG_FILE = 'sorgulananip.txt'

def clear_screen():
    os.system('clear')

def print_menu():
    clear_screen()
    print(Fore.BLUE + """
   ____ ____      _    _____ _____ ___   ___  _     
  / ___|  _ \    / \  |  ___|_   _/ _ \ / _ \| |    
 | |  _| |_) |  / _ \ | |_    | || | | | | | | |    
 | |_| |  _ <  / ___ \|  _|   | || |_| | |_| | |___ 
  \____|_| \_\/_/   \_\_|     |_| \___/ \___/|_____|
                                                    
""")
    print(Fore.RED + """
  _____ _____    _      ____   _____  _____ ______ _____  
 |_   _|  __ \  | |    / __ \ / ____|/ ____|  ____|  __ \ 
   | | | |__) | | |   | |  | | |  __| |  __| |__  | |__) |
   | | |  ___/  | |   | |  | | | |_ | | |_ |  __| |  _  / 
  _| |_| |      | |___| |__| | |__| | |__| | |____| | \ \ 
 |_____|_|      |______\____/ \_____|\_____|______|_|  \_\
                                                          
""")                                                      
    print(Fore.YELLOW + "Developer: carbans2717")
    print(Fore.GREEN + "[01] Çıkış")
    print(Fore.GREEN + "[02] IP Adresi Sorgulama")
    print(Fore.GREEN + "[03] Admin Panel")

def log_ip_info(ip_address, data):
    with open(LOG_FILE, 'a') as file:
        file.write(f"IP Adresi: {ip_address}\n")
        file.write(f"Ülke: {data['country']}\n")
        file.write(f"Bölge: {data['regionName']}\n")
        file.write(f"Şehir: {data['city']}\n")
        file.write(f"ISP: {data['isp']}\n")
        file.write(f"Organizasyon: {data['org']}\n")
        file.write(f"AS: {data['as']}\n")
        file.write(f"Posta Kodu: {data['zip']}\n")
        file.write(f"Enlem: {data['lat']}\n")
        file.write(f"Boylam: {data['lon']}\n")
        file.write("\n")

def get_ip_info(ip_address):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip_address}")
        data = response.json()

        if data['status'] == 'fail':
            print(Fore.RED + "Hatalı IP adresi girdiniz.")
            return

        print(Fore.GREEN + f"IP Adresi: {data['query']}")
        print(Fore.GREEN + f"Ülke: {data['country']}")
        print(Fore.GREEN + f"Bölge: {data['regionName']}")
        print(Fore.GREEN + f"Şehir: {data['city']}")
        print(Fore.GREEN + f"ISP: {data['isp']}")
        print(Fore.GREEN + f"Organizasyon: {data['org']}")
        print(Fore.GREEN + f"AS: {data['as']}")
        print(Fore.GREEN + f"Posta Kodu: {data['zip']}")
        print(Fore.GREEN + f"Enlem: {data['lat']}")
        print(Fore.GREEN + f"Boylam: {data['lon']}")

        # Kullanıcı işlemi kaydediliyor
        user_activity_log.append(f"IP sorgulandı: {ip_address} - {data['country']}, {data['city']}, {data['isp']}")

        # IP bilgilerini log dosyasına kaydet
        log_ip_info(ip_address, data)
    except requests.RequestException as e:
        print(Fore.RED + "Bir hata oluştu:", e)

def admin_panel():
    clear_screen()
    print(Fore.RED + "Admin Password:")
    password = input()
    if password == "graftooladminkey":
        clear_screen()
        print(Fore.GREEN + "Admin terminaline hoş geldiniz!")
        print(Fore.GREEN + "Kullanıcı aktiviteleri:")
        for activity in user_activity_log:
            print(Fore.GREEN + activity)
        
        # Admin log dosyasının içeriğini göster
        print(Fore.GREEN + "\nSorgulanan IP bilgileri:")
        if os.path.exists(LOG_FILE):
            with open(LOG_FILE, 'r') as file:
                print(file.read())
        else:
            print(Fore.RED + "Log dosyası bulunamadı.")
            
        input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
    else:
        print(Fore.RED + "Yanlış şifre. Geri dönülüyor...")
        time.sleep(1)

def main():
    while True:
        print_menu()
        choice = input(Fore.GREEN + "Seçiminizi yapın (1, 2 veya 3): ")

        if choice == '1':
            clear_screen()
            print(Fore.GREEN + "Çıkış yapılıyor...")
            time.sleep(1)
            break
        elif choice == '2':
            clear_screen()
            print(Fore.WHITE + "IP Adresi:")
            ip_address = input()
            clear_screen()
            print(Fore.GREEN + f"{ip_address} adresi sorgulanıyor...")
            get_ip_info(ip_address)
            input(Fore.GREEN + "Devam etmek için bir tuşa basın...")
        elif choice == '3':
            admin_panel()
        else:
            clear_screen()
            print(Fore.RED + "Geçersiz seçim. Lütfen tekrar deneyin.")
            time.sleep(1)

if __name__ == "__main__":
    main()
