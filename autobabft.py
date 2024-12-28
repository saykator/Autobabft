import tkinter as tk
import pyautogui as pyag
import time as t
import random

main = tk.Tk()
main.title("Auto Babft v1.1")
main.geometry("384x64")
main.resizable(False, False)
main.configure(bg="black")

def randomPos():
    global randomX, randomY
    randomX = random.randint(-768, -100)
    randomY = random.randint(-768, -100)

randomPos()

isClicking = False

def clicking():
    global isClicking
    if not isClicking:
        isClicking = True
        print("started")
        mainButton.config(
            text="Stop",
            command=stopClicking,
            state="disabled"
        )

        t.sleep(0.5)
        mainButton.config(
            state="normal"
        )
        autoClick()

def autoClick():
    if isClicking:
        print("auto clicking")
        pyag.click(button="left")
        main.after(500, autoClick)

def stopClicking():
    global isClicking
    randomPos()
    isClicking = False
    print("stopped")
    mainButton.config(
        text="Start",
        command=clicking
    )

mainButton = tk.Button(
    main,
    text="Start",
    command=clicking,
    width=10,
    height=2,
    bg="black",
    fg="blue",
    activebackground="black",
    activeforeground="light blue",
    font=("Arial", 20, "bold"),
    cursor="hand2"
)

mainButton.pack(pady=10)

main.mainloop()