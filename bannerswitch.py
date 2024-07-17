import os
import json
import time
import pyautogui
import psutil

    
# Function to update master JSON file
def update_master(master_file, folder_path, json_files):
    current_json = json_files.pop(0)
    json_files.append(current_json)

    with open(os.path.join(folder_path, current_json), 'r') as file:
        data = json.load(file)
    
    with open(master_file, 'w') as master:
        json.dump(data, master, indent=4)
        

# Folder containing JSON files
folder_path = r"C:\Users\ibesh\AppData\Roaming\cultivation\grasscutter\bannersData"
# Master JSON file
master_file = r"C:\Users\ibesh\AppData\Roaming\cultivation\grasscutter\data\Banners.json"

# List of JSON files in the folder
json_files = [filename for filename in os.listdir(folder_path) if filename.endswith('.json')]

try:
    while True:
        update_master(master_file, folder_path, json_files)
        print("Master JSON updated.")
        time.sleep(300)  # 5 minutes
except KeyboardInterrupt:
    print("Process interrupted.")
