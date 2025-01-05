import os
import time
from colorama import Fore, init, Style
import random
import clear


init(autoreset=True)

RED = Fore.RED
GREEN = Fore.GREEN
PURPLE = Fore.MAGENTA

title = PURPLE + r"""

    ________ __________    _________                          .__                  
    \______ \\______   \  /   _____/____ _____ _______   ____ |  |__   ___________ 
    |    |  \|    |  _/  \_____  \_/ __ \\__  \\_  __ \_/ ___\|  |  \_/ __ \_  __ \
    |    `   \    |   \  /        \  ___/ / __ \|  | \/\  \___|   Y  \  ___/|  | \/
    /_______  /______  / /_______  /\___  >____  /__|    \___  >___|  /\___  >__|     by k4l4shnik0v
            \/       \/          \/     \/     \/            \/     \/     \/       

_______________________________________________________________________________________
        
                        Enter your search or press E to exit    

"""

DB_Folder = "./DB" 
Results_Folder = "./Results"
Founds = []
founs_for_result_file = []

def search(user_search):
    if user_search in ["E", "e", "exit", "Exit", "EXIT"]:
        clear.clear()
        print(PURPLE + "[INFO] Leaving...")
        time.sleep(0.5)
        exit()

    print(PURPLE + "[INFO] Launching the search...")
    try:
        if not os.path.exists(Results_Folder):
            os.makedirs(Results_Folder)

        result_number = 0
        results_file_id = ''.join(random.choices('0123456789', k=4))
        results_file_name = f"results_{results_file_id}.txt"

        for root, dirs, files in os.walk(DB_Folder):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                try:
                    with open(file_path, "r", encoding="utf-8", errors='ignore') as file:
                        if file.name == "Put your DB here.txt":
                            continue
                        print(PURPLE + f"[INFO] Searching in {file.name}...")
                        time.sleep(0.25)
                        content = file.readlines()
                        for row_number, row in enumerate(content, start=1):
                            if user_search in row:
                                result_number += 1
                                result = GREEN + f"[RESULT] RESULT FOUND IN {file_name} - Line {row_number}: " + Style.RESET_ALL + row.strip()
                                result_for_file = f"""___________________________________________________________________________________________________
Found in {file.name} - Line {row_number}
{content}
"""
                                Founds.append(result)
                                founs_for_result_file.append(result_for_file)
                except Exception as e:
                    print(RED + f"[ERROR] Error reading file {file_name}: {e}")
        if result_number != 0:
            with open(f"{Results_Folder}/{results_file_name}", "w", encoding='utf-8') as results_file:
                results_file.write(f"<=========================[SEARCH RESULTS]=========================>\n\nSEARCH: {user_search}\nRESULTS : {result_number}\n\n")
                for result in founs_for_result_file:
                    results_file.write(result)

        print(PURPLE + f"[INFO] Search finished. Total results: {result_number}")

        for result in Founds:
            print(result)
        input(PURPLE + "\n\n[INPUT] Press ENTER to continue...")

    except Exception as e:
        print(RED + f"[ERROR] An error occurred while processing the database folder: {e}")
        input(PURPLE + "\n[INPUT] Press ENTER to continue...")


while True:
    clear.clear()
    print(title)
    user_search = input(PURPLE + "\n\n[INPUT] Enter your search: ").strip()
    search(user_search)
    Founds = []
    founs_for_result_file = []
    clear.clear()
