#!/bin/bash

# Admin şifresi
ADMIN_PASSWORD="graftooladminkey"

# Admin terminali için log dosyası
LOG_FILE="admin_log.txt"

# Renkler
BLUE='\033[94m'
RED='\033[91m'
GREEN='\033[92m'
WHITE='\033[97m'
RESET='\033[0m'

# Menü fonksiyonu
display_menu() {
    clear
    echo -e "${BLUE}   _____ _____            ______ _______ ____   ____  _      ${RESET}"
    echo -e "${BLUE}  / ____|  __ \     /\   |  ____|__   __/ __ \ / __ \| |     ${RESET}"
    echo -e "${BLUE} | |  __| |__) |   /  \  | |__     | | | |  | | |  | | |     ${RESET}"
    echo -e "${BLUE} | | |_ |  _  /   / /\ \ |  __|    | | | |  | | |  | | |     ${RESET}"
    echo -e "${BLUE} | |__| | | \ \  / ____ \| |       | | | |__| | |__| | |____ ${RESET}"
    echo -e "${BLUE}  \_____|_|  \_\/_/    \_\_|       |_|  \____/ \____/|______|${RESET}"
    echo -e "${RED}  _____ _____    _      ____   _____  _____ ______ _____  ${RESET}"
    echo -e "${RED} |_   _|  __ \  | |    / __ \ / ____|/ ____|  ____|  __ \ ${RESET}"
    echo -e "${RED}   | | | |__) | | |   | |  | | |  __| |  __| |__  | |__) |${RESET}"
    echo -e "${RED}   | | |  ___/  | |   | |  | | | |_ | | |_ |  __| |  _  / ${RESET}"
    echo -e "${RED}  _| |_| |      | |___| |__| | |__| | |__| | |____| | \ \ ${RESET}"
    echo -e "${RED} |_____|_|      |______\____/ \_____|\_____|______|_|  \_\\${RESET}"
    echo -e "${GREEN}[01] Çık${RESET}"
    echo -e "${GREEN}[02] IP Sorgulatma${RESET}"
    echo -e "${GREEN}[03] Admin Girişi${RESET}"
}

# IP sorgulama fonksiyonu
ip_sorgulatma() {
    clear
    echo -e "${WHITE}IP:${RESET}"
    read ip
    if [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        response=$(curl -s "https://ipinfo.io/$ip")
        if [ $? -eq 0 ]; then
            echo "$response" | grep -E '"ip"|"city"|"region"|"country"|"org"'
            echo "IP sorgulandı: $ip" >> "$LOG_FILE"
            echo "IP bilgileri: $response" >> "$LOG_FILE"
        else
            echo -e "${RED}API hatası.${RESET}"
        fi
    else
        echo -e "${RED}Geçerli bir IP adresi girmediniz.${RESET}"
    fi
}

# Admin girişi fonksiyonu
admin_girisi() {
    clear
    echo -e "${RED}Admin Password:${RESET}"
    read -s password
    if [ "$password" == "$ADMIN_PASSWORD" ]; then
        echo -e "${GREEN}Admin girişi başarılı.${RESET}"
        tail -f "$LOG_FILE"
    else
        echo -e "${RED}Yanlış şifre. Menüye dönülüyor.${RESET}"
    fi
}

# Ana döngü
while true; do
    display_menu
    read -p "Bir seçenek girin: " secim

    case $secim in
        1)
            exit 0
            ;;
        2)
            ip_sorgulatma
            ;;
        3)
            admin_girisi
            ;;
        *)
            echo -e "${RED}Geçerli bir seçenek girin.${RESET}"
            ;;
    esac
done
