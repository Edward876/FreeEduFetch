from colorama import init, Fore, Back, Style

init(autoreset=True)

# Colors for the hacker theme
fc = Fore.CYAN  # Cyan
fy = Fore.YELLOW  # Yellow
fm = Fore.MAGENTA  # Magenta
sb = Style.BRIGHT  # Bright style
fr = Fore.RED  # Red
fb = Fore.BLUE  # Blue

def banner():
    banner_text = f'''
{fr}{sb}
  _______            ______    _       ______   _       _    
 |  ____|           |  ____|  | |     |  ____| | |     | |    
 | |__ _ __ ___  ___| |__   __| |_   _| |__ ___| |_ ___| |__  
 |  __| '__/ _ \/ _ \  __| / _` | | | |  __/ _ \ __/ __| '_ \ 
 | |  | | |  __/  __/ |___| (_| | |_| | | |  __/ || (__| | | |
 |_|  |_|  \___|\___|______\__,_|\__,_|_|  \___|\__\___|_| |_|
                                                              
                                                              
{Style.RESET_ALL}
'''
    print(banner_text)

def msg():
    msg_text = f'''
{fc}{fr}[{fy}*{fc}{fr}] {fb}Please be patient, It may take some time to Get Courses for you!{fb} {fr}[{fy}*{fc}{fr}]
'''
    print(msg_text)

def info():
    info_text = f'''
{fc}{fr}[{fy}*{fc}{fr}] {fb}Coded By:{fb} {fr}Shilly Joestar{fr}
'''
    print(info_text)

def end_msg():
    end_msg_text = f''' 
{fc}{fr}[{fy}*{fc}{fr}] {fb}Thank you for your patience!{fb}
{fc}{fr}[{fy}*{fc}{fr}] {fb}All Paid Courses for free to enroll are saved in getbenefits.txt{fb}
{fc}{fr}[{fy}*{fc}{fr}] {fb}Hope to see you again ❤!!{fb}
'''
    print(end_msg_text)

if __name__ == "__main__":
    banner()
    msg()
    info()
    end_msg()
