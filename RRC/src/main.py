import requests, ctypes, os, random
from colorama import init, Fore
from discord_webhook import DiscordWebhook, DiscordEmbed
init()
temp = f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\11011001 10000100 11011000 10100111 00100000 11011000 10101010 11011000 10101010 11011001 10000101 11011001 10000100 11011001 10000010 11011001 10000001'
u = "Available.txt"
im = "https://i.postimg.cc/SQgdwb20/image.png"
ic = "https://i.postimg.cc/pVGC3Jws/icon.png"
letters = "abcdefghijklmnoqrstuvwxyz0123456789-_."
if os.path.exists(temp):
    try:
        os.remove(temp)
    except Exception:
        pass
ctypes.windll.kernel32.SetConsoleTitleW("RecRoom Checker  >  https://github.com/Q8G")
print(Fore.YELLOW + r"""
      
      
      
      
      
      
                           ___          ___                    _______           __          
                          / _ \___ ____/ _ \___  ___  __ _    / ___/ /  ___ ____/ /_____ ____
                         / , _/ -_) __/ , _/ _ \/ _ \/  ' \  / /__/ _ \/ -_) __/  '_/ -_) __/
                        /_/|_|\__/\__/_/|_|\___/\___/_/_/_/  \___/_//_/\__/\__/_/\_\\__/_/   
                        
                        
""")
while True:
    Q1 = input(Fore.YELLOW + "                       [?] How length is the username?: " + Fore.RESET)
    if not Q1:
        print(Fore.RED + "                       [-] Enter a choice" + Fore.RESET)
    elif not Q1.isdigit():
        print(Fore.RED + "                       [-] You must enter a number" + Fore.RESET) 
    else:
        break
while True:
    Q2 = input(Fore.YELLOW + "                       [?] Do you want to send your available username to Discord Webhook? (Y/n): " + Fore.RESET)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         #https://github.com/Q8G
    if not Q2:
        print(Fore.RED + "                       [-] Enter a choice" + Fore.RESET)
    elif Q2.lower() in ["y", "yes"]:
        while True:
            Q4 = input(Fore.YELLOW + "                       [?] Enter the webhook url: " + Fore.RESET)
            if not Q4:
                print(Fore.RED + "                       [-] Enter a url" + Fore.RESET)
            elif not Q4.startswith("https://discord.com/api/webhooks/"):
                print(Fore.RED + f"                       [-] This is not a Webhook URL" + Fore.RESET)
            else:
                try:
                    response = requests.head(Q4, timeout=5)
                    if response.status_code == 200:
                        with open(temp, "w") as f:
                            f.write(" ")
                        while True:
                            Q2 = input(Fore.YELLOW + "                       [?] Do you want to send test? (Y/n): " + Fore.RESET)
                            if not Q2:
                                print(Fore.RED + "                       [-] Enter a choice" + Fore.RESET)
                            elif Q2.lower() in ["y", "yes"]:
                                try:
                                    webhook = DiscordWebhook(url=Q4, username="RecRoom Checker", avatar_url=im, content="Hello")
                                    webhook.execute()
                                    print(Fore.LIGHTGREEN_EX + f"                       [+] Tested")
                                    break
                                except requests.exceptions.RequestException as e:
                                    print(Fore.RED + f"                       [-] Error: {e}" + Fore.RESET)
                                except Exception:
                                    print(Fore.RED + f"                       [-] Something Went Worng" + Fore.RESET)
                            elif Q2.lower() in ["n", "no"]:
                                break
                            else:
                                print(Fore.RED + "                       [-] Unexpected answer" + Fore.RESET)
                        break
                    else:
                        print(Fore.RED + f"                       [-] invalid url" + Fore.RESET)
                except requests.exceptions.RequestException as e:
                    print(Fore.RED + f"                       [-] Error: {e}" + Fore.RESET)
                except Exception:
                    print(Fore.RED + f"                       [-] Something Went Worng" + Fore.RESET)
        break
    elif Q2.lower() in ["n", "no"]:
        break
    else:
        print(Fore.RED + "                       [-] Unexpected answer" + Fore.RESET)
while True:
    Q3 = input(Fore.YELLOW + "                       [?] Do you want to print only the available username? (Y/n): " + Fore.RESET)
    if not Q3:
        print(Fore.RED + "                       [-] Enter a choice" + Fore.RESET)
    elif Q3.lower() in ["y", "yes"]:
        break
    elif Q3.lower() in ["n", "no"]:
        break
    else:
        print(Fore.RED + "                       [-] Unexpected answer" + Fore.RESET)
while True:
    Q5 = input(Fore.YELLOW + "                       [?] Do you want to save the available username in a file? (Y/n): " + Fore.RESET)
    if not Q5:
        print(Fore.RED + "                       [-] Enter a choice" + Fore.RESET)
    elif Q5.lower() in ["y", "yes"]:
        break
    elif Q5.lower() in ["n", "no"]:
        break
    else:
        print(Fore.RED + "                       [-] Unexpected answer" + Fore.RESET)
Q1A = int(Q1)
while True:
    ra = ''.join(random.choice(letters) for _ in range(Q1A))
    url = f"https://apim.rec.net/accounts/account?username={ra}"
    response = requests.get(url)
    if response.status_code == 200:
        if Q3.lower() in ["n", "no"]:
            print(Fore.RED + f"                       [-] {ra} is unavailable")
    elif response.status_code == 404:
        print(Fore.LIGHTGREEN_EX + f"                       [+] {ra} is available")
        if Q5.lower() in ["y", "yes"]:
            if os.path.exists(u):
                with open(u, "a") as f:
                    f.write(f"{ra}\n")
            else:
                with open(u, "w") as f:
                    f.write(f"{ra}\n")
        if os.path.exists(temp):
            webhook = DiscordWebhook(url=Q4, username="RecRoom Checker", avatar_url=im)
            embed = DiscordEmbed(title=f"**Username Available**", color="ffffff")
            embed.set_author(name="Checker Username", icon_url=im)
            embed.add_embed_field(name=f"> **@{ra}**", value=f"")
            embed.set_footer(text="https://github.com/Q8G | RWSHNY GROUP ", color="ff0000")
            embed.set_thumbnail(url=ic)
            embed.set_timestamp()
            webhook.add_embed(embed)
            webhook.execute()
    else:
        print(Fore.RED + f"                       [-] Something Went Worng" + Fore.RESET)