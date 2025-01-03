import os
#Returns the type of operating system shell is being run within.
def mode(args=[]):
    if str(os.name).lower() in ["nt","dos"]:
        mode = "dos"
    elif str(os.name).lower() in ["posix","linux"]:
        mode = "linux"
    else:
        mode = "name"
    
    return mode

def man(args=[]):
    output = "Provides you with the name of your host OS. This command supports no positional arguments. Providing them will have no effect."
    return output