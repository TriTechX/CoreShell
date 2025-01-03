import os
import importlib
from bin import *
import colours

home = os.getcwd()

validCmds = []

def execute_command(cmd, args):
    try:
        command_func = globals().get(cmd) or importlib.import_module(f"bin.{cmd}")
        output = command_func(args)
        return output
    except Exception as e:
        return f"Error: {e}"

while True:
    wd=""
    cmd=""
    base=""
    args="" 
    
    wd = os.getcwd()
    cmd = input(wd + colours.magenta() + " ~ € " + colours.reset())
    base = cmd.split(" ")[0]
    args = cmd.split(" ")[1:]
    if base not in globals() and not hasattr(importlib.import_module('bin'), base):
        print("Command not found.")
    else:
        output = execute_command(base, args)
        if output not in [0, None]:
            print(output)
