import os

def cwd(args=[]):
    cwd = os.getcwd()
    return cwd

def man(args=[]):
    output = "Prints the current working directory to the screen. This command supports no positional arguments. Providing them will have no effect."
    return output