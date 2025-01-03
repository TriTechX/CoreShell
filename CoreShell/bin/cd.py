import os
from bin.cwd import cwd

def cd(args=[]):
    if len(args)>0:
        try:
            os.chdir(args[0])
            output = f"cd: changed directory to '{cwd()}'"
        except:
            if os.path.isfile(args[0]):
                output = f"cd: '{args[0]}' is a file."
            else:
                output = f"cd: no such file or directory '{args([0])}'"
    else:
        output = "cd: no directory was provided."
    return output

def man(args=[]):
    output = "Changes the directory.\nUsage: cd [path]"
    return output
