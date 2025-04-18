#!/bin/bash
clear
echo -e "\033[1;32m[*] ZexTool Kurulumu Başlatılıyor...\033[0m"
sleep 1
echo -e "\033[1;34m[+] Gerekli paketler kuruluyor...\033[0m"
pkg update -y && pkg upgrade -y
pkg install python git openssl curl wget -y
echo -e "\033[1;34m[+] Python modülleri kuruluyor...\033[0m"
pip install colorama
chmod +x ZexTool.py
echo -e "\033[1;32m[✓] Kurulum tamamlandı! ZexTool’u başlatmak için:\033[0m"
echo -e "\033[1;33mpython ZexTool.py\033[0m"
