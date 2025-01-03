from bin.mode import mode
import os

def cl(args=[]):
    osName = mode()
    
    if osName == "dos":
        clear = os.system("cls")
    else:
        clear = os.system("clear")

    return clear

def man(args=[]):
    output = "Clears the screen. Has no positional arguments, providing them will have no effect."
    return output
        