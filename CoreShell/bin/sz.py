import os

def sz(args=[]):
    sizeByte = 0

    if len(args) > 0:
        if os.path.isfile(args[0]):
            sizeByte = os.path.getsize(args[0])
        else:
            for path, dirs, files in os.walk(args[0]):
                try:
                    for f in files:
                        fp = os.path.join(path, f)
                        sizeByte += os.path.getsize(fp)
                except:
                    pass
    
        if "--unit" in args:
            if sizeByte < 1000:
                size = str(sizeByte) + "B"
            elif sizeByte >= 1000 and sizeByte < 1000000:
                size = str(round(sizeByte / 1000, 2)) + "KB"
            elif sizeByte >= 1000000 and sizeByte < 1000000000:
                size = str(round(sizeByte / 1000000, 2)) + "MB"
            elif sizeByte >= 1000000000 and sizeByte < 1000000000000:
                size = str(round(sizeByte / 1000000000, 2)) + "GB"
            elif sizeByte >= 1000000000000 and sizeByte < 1000000000000000:
                size = str(round(sizeByte / 1000000000000, 2)) + "TB"
    
            sizeFormat = size
        else:
            sizeFormat = sizeByte
    else:
        sizeFormat = "sz: no such file or directory was given."

    if sizeFormat == 0 or sizeFormat == "0" or sizeFormat == "0B":
        if os.path.exists(args[0]):
            if "--unit" in args:
                sizeFormat = "0B"
            else:
                sizeFormat = 0
        else:
            sizeFormat = f"sz: '{args[0]}' - the file or directory does not exist."

    return sizeFormat

def man(args=[]):
    output = "Provides you with the size of a given file/directory.\nTakes positional arguments:\n--unit: prints the size in a more human readable fashion with the unit.\nBy default this command provides you the size of the file in bytes."
    return output
