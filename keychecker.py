from pynput import keyboard
import subprocess
import pyautogui



def cmd(command):
    subprocess.Popen(command, shell=True)
        
        

def log(cmd):
    if cmd == "reset":
        eve = open('keylog','w',encoding="utf-8_sig")
        eve.write("")
        eve.close()
    elif cmd == "read":
        eve = open('keylog','r',encoding="utf-8_sig")
        logdata = eve.read()
        eve.close()
        return logdata
    else:
        eve = open('keylog','a',encoding="utf-8_sig")
        eve.write(cmd)
        eve.close()

def on_press(key):
    try:
        print(key)
        if(str(key).count("'") > 0 ):
            stkey = str(key).split("'")[1]
            log(stkey+",")
        else:
            stkey = str(key)
            log(stkey+",")
        
    except AttributeError:
        if(str(key).count("'") > 0 ):
            stkey = str(key).split("'")[1]
        else:
            stkey = str(key)
            


def on_release(key):
    sc = open('keysc.ini','r',encoding="utf-8_sig")
    scdata = sc.read()
    sc.close()
    scsep = scdata.split("\n")

    defsc = open('defaultkey','r',encoding="utf-8_sig")
    defscdata = defsc.read()
    defsc.close()
    defscsep = defscdata.split("\n")   

    data = log("read")
    log("reset")

    i = 0
    
    for d in scsep:
        if d.count("=") > 0:
            if data.count(d.split("=")[0]) > 0:
                for k in defscsep:
                    if k.count("=") > 0:
                        if d.split("=")[1] == k.split("==")[0]:
                            exec(k.split("==")[1])
                            i = 1
                            break
                if i != 1:        
                    cmd(d.split("=")[1])
                    log("reset")
                    break
                else:
                    log("reset")
                    break
            

with keyboard.Listener(on_press = on_press,on_release = on_release) as listener:
    listener.join()
            
