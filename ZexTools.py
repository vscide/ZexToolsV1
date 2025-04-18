import os
import subprocess
from colorama import init, Fore, Style

init(autoreset=True)

def banner():
    print(Fore.CYAN + Style.BRIGHT + """
███╗   ███╗███████╗██╗  ██╗████████╗ ██████╗  ██████╗ ██╗     ███████╗
████╗ ████║██╔════╝██║  ██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██╔████╔██║█████╗  ███████║   ██║   ██║   ██║██║   ██║██║     █████╗  
██║╚██╔╝██║██╔══╝  ██╔══██║   ██║   ██║   ██║██║   ██║██║     ██╔══╝  
██║ ╚═╝ ██║███████╗██║  ██║   ██║   ╚██████╔╝╚██████╔╝███████╗███████╗
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
""" + Fore.MAGENTA + Style.BRIGHT + "                            [ Ethical Hacking Toolset by Cr4ck3r ]")

def clone_tool(name, url):
    print(Fore.YELLOW + f"\n[+] {name} indiriliyor...")
    subprocess.run(["git", "clone", url])
    print(Fore.GREEN + f"[✓] {name} başarıyla indirildi!\n")

def show_menu():
    banner()
    print(Fore.BLUE + "\n[ MENÜ ]")
    print("1. Bilgi Toplama Araçları")
    print("2. Zafiyet Taraması")
    print("3. Web Exploit")
    print("4. Sosyal Mühendislik")
    print("5. Kablosuz Saldırı")
    print("0. Çıkış")

    choice = input(Fore.CYAN + "\nSeçiminiz: ")
    if choice == "1":
        bilgi_toplama()
    elif choice == "2":
        zafiyet()
    elif choice == "3":
        web()
    elif choice == "4":
        sosyal()
    elif choice == "5":
        wifi()
    elif choice == "0":
        print(Fore.RED + "Çıkılıyor...")
        exit()
    else:
        print(Fore.RED + "Geçersiz seçim!")
        show_menu()

def bilgi_toplama():
    clone_tool("Nmap", "https://github.com/nmap/nmap")
    clone_tool("Infoga", "https://github.com/m4ll0k/Infoga")
    show_menu()

def zafiyet():
    clone_tool("Nmap-Vulners", "https://github.com/vulnersCom/nmap-vulners")
    clone_tool("Nuclei", "https://github.com/projectdiscovery/nuclei")
    show_menu()

def web():
    clone_tool("SQLMap", "https://github.com/sqlmapproject/sqlmap")
    clone_tool("OWASP ZAP", "https://github.com/zaproxy/zaproxy")
    show_menu()

def sosyal():
    clone_tool("SET", "https://github.com/trustedsec/social-engineer-toolkit")
    clone_tool("HiddenEye", "https://github.com/DarkSecDevelopers/HiddenEye")
    show_menu()

def wifi():
    clone_tool("Wifite2", "https://github.com/derv82/wifite2")
    clone_tool("Aircrack-ng", "https://github.com/aircrack-ng/aircrack-ng")
    show_menu()

if __name__ == "__main__":
    show_menu()
