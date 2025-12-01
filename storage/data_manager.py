import json
import os
from historique.list import CommandLinkedList

DATA_FILE = "storage/data.json"

def save_data(user_histories):
    data_to_save = {}
    
    for user_id, linked_list in user_histories.items():
        commands = []
        current = linked_list.head
        while current:
            commands.append(current.data)
            current = current.next
        data_to_save[str(user_id)] = commands

    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data_to_save, f, indent=4)

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data_loaded = json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}

    restored_histories = {}
    
    for user_id_str, commands_list in data_loaded.items():
        user_id = int(user_id_str)
        new_linked_list = CommandLinkedList()
        for cmd in reversed(commands_list):
            new_linked_list.add(cmd)
            
        restored_histories[user_id] = new_linked_list

    return restored_histories