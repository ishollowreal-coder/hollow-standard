import os
import time
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('clear')

def logo():
    banner = f"""
{Fore.CYAN}    _________ __________  _   ______  ___    ____  ____ 
{Fore.CYAN}   / ___/ __ /_  __/ __ \/ | / / __ \/   |  / __ \/ __ \\
{Fore.WHITE}   \__ \/ /_/ / / / / / / /  |/ / / / / /| | / /_/ / / / /
{Fore.WHITE}  ___/ / __  / / / / /_/ / /|  / /_/ / ___ |/ _, _/ /_/ / 
{Fore.CYAN} /____/_/ |_| /_/  \____/_/ |_/_____/_/  |_/_/ |_/_____/  
    """
    print(banner)
    print(f"{Fore.YELLOW}{'='*60}")
    print(f"{Fore.GREEN} Tier: {Fore.RED}STANDARD (LIMITED) {Fore.GREEN}| Status: Fixed | Dev: Hollow")
    print(f"{Fore.YELLOW}{'='*60}\n")

# Tools Database for Standard Tier
std_db = {
    "1": {"name": "Info Gathering", "locked": False, "tools": [("Nmap", "nmap/nmap"), ("Sherlock", "sherlock-project/sherlock"), ("RedHawk", "Tuhinshubhra/RED_HAWK")]},
    "2": {"name": "Vulnerability Analysis", "locked": False, "tools": [("SQLmap", "sqlmapproject/sqlmap"), ("Nikto", "sullo/nikto"), ("Striker", "s0md3v/Striker")]},
    "3": {"name": "Phishing Tools", "locked": False, "tools": [("Zphisher", "htr-tech/zphisher"), ("PyPhisher", "KasRoudra/PyPhisher"), ("Seeker", "thewhiteh4t/seeker")]},
    "4": {"name": "Password Attacks", "locked": False, "tools": [("Hydra", "vanhauser-thc/thc-hydra"), ("JohnTheRipper", "openwall/john"), ("Cupp", "Mebrouki/Cupp")]},
    "5": {"name": "Termux Styling", "locked": False, "tools": [("T-Header", "htr-tech/t-header"), ("Termux-Style", "adi1090x/termux-style"), ("OhMyTermux", "4678/ohmytermux")]},
    "6": {"name": "Android Hacking (PRO)", "locked": True},
    "7": {"name": "Post Exploitation (PRO)", "locked": True},
    "8": {"name": "DDOS Advanced (PRO)", "locked": True},
}

def install_tool(name, repo):
    clear()
    logo()
    print(f"{Fore.BLUE}[INSTALLING]: {Fore.WHITE}{name}")
    print(f"{Fore.CYAN}{'-'*60}")
    os.system(f"git clone https://github.com/{repo}")
    print(f"\n{Fore.GREEN}[+] Done. Check your folder.")
    input(f"\n{Fore.YELLOW}Press Enter to return...")

def category_menu(cid):
    while True:
        clear()
        logo()
        cat = std_db[cid]
        print(f"{Fore.MAGENTA}CATEGORY >> {cat['name'].upper()}")
        print(f"{Fore.CYAN}{'-'*60}")
        for i, (t_name, t_repo) in enumerate(cat['tools'], 1):
            print(f"{Fore.CYAN}[{i}] {Fore.WHITE}{t_name.ljust(15)} {Fore.BLACK}{Style.BRIGHT}({t_repo})")
        
        print(f"\n{Fore.YELLOW}[B] Back to Menu")
        choice = input(f"\n{Fore.GREEN}hollow@std~# {Fore.WHITE}")
        if choice.lower() == 'b': break
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(cat['tools']):
                install_tool(cat['tools'][idx][0], cat['tools'][idx][1])
        except: pass

def show_locked_msg():
    print(f"\n{Fore.RED}[!] ACCESS DENIED")
    print(f"{Fore.YELLOW}This module is only available in {Fore.CYAN}Hollow Ultra Pro Edition.")
    input(f"\n{Fore.GREEN}Press Enter to go back...")

def main():
    while True:
        clear()
        logo()
        print(f"{Fore.YELLOW}AVAILABLE MODULES")
        print(f"{Fore.CYAN}{'-'*60}")
        for k, v in std_db.items():
            status = f"{Fore.RED}[LOCKED]" if v['locked'] else f"{Fore.GREEN}[OPEN]"
            print(f"{Fore.CYAN}[{k}] {Fore.WHITE}{v['name'].ljust(25)} {status}")
        
        print(f"\n{Fore.RED}[0] EXIT")
        choice = input(f"\n{Fore.GREEN}hollow@std~# {Fore.WHITE}")
        
        if choice == '0': break
        if choice in std_db:
            if std_db[choice]['locked']:
                show_locked_msg()
            else:
                print(f"\n{Fore.GREEN}[*] Opening {std_db[choice]['name']}...")
                time.sleep(0.5)
                category_menu(choice) # Ab ye function actual tools dikhayega
        else:
            time.sleep(0.5)

if __name__ == "__main__":
    main()
  
