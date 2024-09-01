#!/bin/bash
clear
echo -e "\e[34m"
echo "   _____ _____            ______ _______ ____   ____  _      "
echo "  / ____|  __ \     /\   |  ____|__   __/ __ \ / __ \| |     "
echo " | |  __| |__) |   /  \  | |__     | | | |  | | |  | | |     "
echo " | | |_ |  _  /   / /\ \ |  __|    | | | |  | | |  | | |     "
echo " | |__| | | \ \  / ____ \| |       | | | |__| | |__| | |____ "
echo "  \_____|_|  \_\/_/    \_\_|       |_|  \____/ \____/|______|"
echo "                                                             "
echo "                                                             "
echo -e "\e[0m"
echo -e "\e[31m"
echo "  _____ _____    _      ____   _____  _____ ______ _____  "
echo " |_   _|  __ \  | |    / __ \ / ____|/ ____|  ____|  __ \ "
echo "   | | | |__) | | |   | |  | | |  __| |  __| |__  | |__) |"
echo "   | | |  ___/  | |   | |  | | | |_ | | |_ |  __| |  _  / "
echo "  _| |_| |      | |___| |__| | |__| | |__| | |____| | \ \ "
echo " |_____|_|      |______\____/ \_____|\_____|______|_|  \_\\"
echo "                                                          "
echo "                                                          "
echo -e "\e[0m"

# Menü seçenekleri
echo -e "\e[32m[01] Çık\e[0m"
echo -e "\e[32m[02] IP Sorgulatma\e[0m"
read -p "Bir seçenek girin: " secim

if [ "$secim" == "1" ]; then
    exit 0
elif [ "$secim" == "2" ]; then
    clear
    echo -e "\e[37mIP:\e[0m"
    read ip
    if [[ $ip =~ ^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
        curl -s "https://ipinfo.io/$ip" | grep -E '"ip"|"city"|"region"|"country"|"org"'
    else
        echo "Geçerli bir IP adresi girmediniz."
    fi
else
    echo "Geçerli bir seçenek girin."
fi
