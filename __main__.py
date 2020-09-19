import os
import sys
from _thread import start_new_thread as thread
from time import sleep
browser = "firefox" #Browser with has to be used
r = 5 #Per run number of Views
extra_time = 4 #time that is need by opening a website in secounds


def window(url):
    os.system(command + " --new-tab --url "+url)
if len(sys.argv) < 4:
    print("Usage: <URL> <clicks> <time in secounds> <proxy>")
    print("   Not given")
    sys.exit()
if sys.argv[4] == "yes":
    command = "proxychains "+browser
    thread(os.system,("tor",))
else:
    command = browser
time_p = int(sys.argv[3]) + extra_time 

for m in range(int(int(sys.argv[2])/r)):
    for i in range(r):
        t = thread(window, (sys.argv[1],))
        sleep(1.5)
    sleep(int(time_p))
    os.system("pkill "+browser)
    sleep(5)
    os.system("clear")
    print("---------------------------")
    print("Clicks: ",str(r*(m+1)))
    print("---------------------------")

os.system("pkill tor") #close tor
os.system("clear")
print("---------------------------------")
print("URL:",sys.argv[1])
print("Clicks:",sys.argv[2])
print("Finished")
print("---------------------------------")
   
