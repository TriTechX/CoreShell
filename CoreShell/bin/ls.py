import os
from bin.sz import sz
import colours

def ls(args=[]):
    validArgs = ["--pretty","--bare"]
    dirCont = os.listdir()
    #args --pretty, --bare, --sep - [SEP]
    if len(args) == 0:
        response=""
        for item in dirCont:
            if item != dirCont[-1]:
                if os.path.isfile(item):
                    response+=item+"\n"
                else:
                    response+="\x1B[1m"+item+colours.reset()+"\n"
            else:
                response+=item
        dirCont = response
    
    if len(args) > 0:
        if "--pretty" in args:
            response = ""
            response+="------\n"
            
            for item in dirCont:
                if os.path.isfile(item):
                    response += "🗎  - " + item + " " + str(sz([item,"--unit"])) + "\n"
                else:
                    response += "🗀  - \x1B[1m" + item + colours.reset() + " " + str(sz([item,"--unit"])) + "\n"
            
            response+="------"
            dirCont = response
        elif "--bare" in args:
            pass
        elif args[0] not in validArgs:
            dirCont = "ls: invalid positional arguments were given."
        elif len(args) > 1:
            dirCont = "ls: too many positional arguments were provided."
        
        
    
    return dirCont

def man(args=[]):
    output = "Lists all of the files and directories in the current working directory.\nUse arguments such as --pretty to print the list in a more human readable format, or --bare to print the list in a more managable format for piping."
    return output
    