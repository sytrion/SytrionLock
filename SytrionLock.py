import requests
import time
import sys
import os
import random
from colorama import init, Fore, Style
from pyfiglet import Figlet

f = Figlet(font='starwars')

init(autoreset=True)

SKULL = "💀"
SPIDER = "🕷️"

def slow_text(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    print(f.renderText('Sytrion'))
    print(Fore.RED + SKULL + "𓆝 𓆟 𓆞 𓆝" * 10 + SKULL)
    
    slow_text(f"{Fore.RED}Made by sytrion {SPIDER}", 0.05)
    print(f"{Fore.RED}For communication with me Discord : @sytrion")
    print(f"{Fore.RED}For More Tools Visit My GitHub: https://github.com/sytrion ")
    print(f"{Fore.LIGHTBLACK_EX}This tool is open source; you can use it however you like. Have fun!\n")

# ====================== CHECK FUNCTIONS ======================

def check_platform(username, platform_name, url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
        }
        r = requests.get(url, headers=headers, timeout=15)
        
        if platform_name == "Instagram":
            content = r.text.lower()
            if "sorry, this page isn't available" in content or "page not found" in content:
                print(f"{Fore.RED}[-] {platform_name} → Not Found!")
                return False
            else:
                print(f"{Fore.GREEN}[+] {platform_name} → FOUND! {url}")
                return True
                
        if r.status_code == 200:
            print(f"{Fore.GREEN}[+] {platform_name} → FOUND! {url}")
            return True
        else:
            print(f"{Fore.RED}[-] {platform_name} → Not Found!")
            return False
            
    except:
        print(f"{Fore.RED}[!] {platform_name} → Error during check!")
        return False

def check_tiktok(username): return check_platform(username, "TikTok", f"https://www.tiktok.com/@{username}")
def check_instagram(username): return check_platform(username, "Instagram", f"https://www.instagram.com/{username}/")
def check_twitter(username): return check_platform(username, "X (Twitter)", f"https://twitter.com/{username}")
def check_youtube(username): return check_platform(username, "YouTube", f"https://www.youtube.com/@{username}")
def check_facebook(username): return check_platform(username, "Facebook", f"https://www.facebook.com/{username}")
def check_telegram(username): return check_platform(username, "Telegram", f"https://t.me/{username}")
def check_snapchat(username): return check_platform(username, "Snapchat", f"https://www.snapchat.com/add/{username}")
def check_spotify(username): return check_platform(username, "Spotify", f"https://open.spotify.com/user/{username}")
def check_reddit(username): return check_platform(username, "Reddit", f"https://www.reddit.com/user/{username}")
def check_twitch(username): return check_platform(username, "Twitch", f"https://www.twitch.tv/{username}")
def check_pinterest(username): return check_platform(username, "Pinterest", f"https://www.pinterest.com/{username}/")
def check_linkedin(username): return check_platform(username, "LinkedIn", f"https://www.linkedin.com/in/{username}")
def check_roblox(username): return check_platform(username, "Roblox", f"https://www.roblox.com/users/search?keyword={username}")

def check_whatsapp(username):
    print(f"{Fore.YELLOW}[~] WhatsApp does not support public username checking.")
    return False

def check_netflix(username):
    print(f"{Fore.YELLOW}[~] Netflix username checking is not reliable publicly.")
    return False

def check_discord(username):
    print(f"{Fore.YELLOW}[~] Discord is hard to check without API.")
    return False

def check_messenger(username):
    print(f"{Fore.YELLOW}[~] Messenger → Checking via Facebook...")
    return check_facebook(username)

def check_capcut(username):
    print(f"{Fore.YELLOW}[~] CapCut username check is limited.")
    return False

def check_zoom(username):
    print(f"{Fore.YELLOW}[~] Zoom does not support public username lookup.")
    return False

def check_gmail(username):
    print(f"{Fore.YELLOW}[~] Gmail is email based. Try {username}@gmail.com")
    return False

# ====================== SUGGESTIONS ======================

GENERAL_EXAMPLES = {
    "Instagram": ["cristiano", "mrbeast", "kyliejenner"],
    "TikTok": ["khaby.lame", "charlidamelio"],
    "X (Twitter)": ["elonmusk", "Cristiano"],
    "YouTube": ["MrBeast", "PewDiePie"],
    "Facebook": ["zuck", "Cristiano"],
    "Telegram": ["durov"],
    "Snapchat": ["snapchat"],
    "Spotify": ["theweeknd"],
    "Reddit": ["spez"],
    "Twitch": ["ninja"],
}

def get_random_suggestions(username):
    if not username:
        return ""
    suffixes = ["official", "real", "yt", "tv", "hd", "69", "x"]
    prefixes = ["the", "real", "mr"]
    suggestions = []
    for _ in range(4):
        if random.random() > 0.5:
            suggestions.append(username + random.choice(suffixes))
        else:
            suggestions.append(random.choice(prefixes) + username)
    return f"{Fore.LIGHTCYAN_EX}Similar suggestions: {Fore.WHITE}{', '.join(suggestions)}"

# ====================== MENU ======================

def show_menu():
    print(f"{Fore.CYAN}=== Username Checker Menu ==={Style.RESET_ALL}")
    print(f"""{Fore.LIGHTCYAN_EX}   🔥 Most Popular 10 Apps 🔥{Style.RESET_ALL}
{Fore.YELLOW}[1] {Fore.WHITE}Instagram     {Fore.YELLOW}[6] {Fore.WHITE}Snapchat
{Fore.YELLOW}[2] {Fore.WHITE}TikTok        {Fore.YELLOW}[7] {Fore.WHITE}Facebook
{Fore.YELLOW}[3] {Fore.WHITE}X (Twitter)   {Fore.YELLOW}[8] {Fore.WHITE}Roblox
{Fore.YELLOW}[4] {Fore.WHITE}YouTube       {Fore.YELLOW}[9] {Fore.WHITE}Twitch
{Fore.YELLOW}[5] {Fore.WHITE}Telegram      {Fore.YELLOW}[10]{Fore.WHITE} Reddit

{Fore.LIGHTBLACK_EX}────── Other Platforms ──────
{Fore.YELLOW}[11] {Fore.WHITE}Spotify       {Fore.YELLOW}[12] {Fore.WHITE}Pinterest
{Fore.YELLOW}[13] {Fore.WHITE}LinkedIn      {Fore.YELLOW}[14] {Fore.WHITE}Messenger
{Fore.YELLOW}[15] {Fore.WHITE}Discord       {Fore.YELLOW}[16] {Fore.WHITE}Netflix
{Fore.YELLOW}[17] {Fore.WHITE}CapCut        {Fore.YELLOW}[18] {Fore.WHITE}Zoom
{Fore.YELLOW}[19] {Fore.WHITE}WhatsApp      {Fore.YELLOW}[20] {Fore.WHITE}Gmail
    """)
    print(f"{Fore.YELLOW}[0]  {Fore.WHITE}Exit")
    print()

# ====================== MAIN ======================

def main():
    while True:
        print_banner()
        show_menu()
        
        choice = input(f"{Fore.WHITE}Enter your choice: {Fore.YELLOW}").strip()
        
        if choice == "0":
            print(f"\n{Fore.MAGENTA}Goodbye! {SKULL}{SPIDER}")
            sys.exit(0)
        
        platform_map = {
            "1": ("Instagram", check_instagram),
            "2": ("TikTok", check_tiktok),
            "3": ("X (Twitter)", check_twitter),
            "4": ("YouTube", check_youtube),
            "5": ("Telegram", check_telegram),
            "6": ("Snapchat", check_snapchat),
            "7": ("Facebook", check_facebook),
            "8": ("Roblox", check_roblox),
            "9": ("Twitch", check_twitch),
            "10": ("Reddit", check_reddit),
            "11": ("Spotify", check_spotify),
            "12": ("Pinterest", check_pinterest),
            "13": ("LinkedIn", check_linkedin),
            "14": ("Messenger", check_messenger),
            "15": ("Discord", check_discord),
            "16": ("Netflix", check_netflix),
            "17": ("CapCut", check_capcut),
            "18": ("Zoom", check_zoom),
            "19": ("WhatsApp", check_whatsapp),
            "20": ("Gmail", check_gmail),
        }
        
        if choice in platform_map:
            platform_name, check_func = platform_map[choice]
            
            clear_screen()
            print_banner()
            
            examples = GENERAL_EXAMPLES.get(platform_name, ["No examples"])
            random_examples = random.sample(examples, min(3, len(examples)))
            print(f"{Fore.LIGHTCYAN_EX}Popular accounts: {Fore.WHITE}{', '.join(random_examples)}")
            
            username = input(f"\n{Fore.LIGHTBLACK_EX}Enter username for {Fore.WHITE}{platform_name}{Fore.LIGHTBLACK_EX}: {Fore.YELLOW}").strip()
            
            if not username:
                print(f"{Fore.RED}[!] Username cannot be empty!")
                input(f"\n{Fore.LIGHTBLACK_EX}Press Enter to return to menu...")
                continue
            
            print(get_random_suggestions(username))
            
            print(f"\n{Fore.CYAN}[*] Checking {platform_name} @{username}...\n")
            check_func(username)
            
            input(f"\n{Fore.LIGHTBLACK_EX}Press Enter to return to menu...")
        else:
            print(f"{Fore.RED}[!] Invalid choice!")
            time.sleep(1.2)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Program terminated by user. {SKULL}")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[!] Unexpected error: {e}")