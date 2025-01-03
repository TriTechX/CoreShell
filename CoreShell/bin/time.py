from datetime import datetime

def time(args=[]):
    currentTime = datetime.now()
    #args: --date, --bare, --pretty, --12
    validArgs = ["--date","--dateus","--bare","--pretty"]
    if len(args) == 1:
        if "--date" in args:
            output = currentTime.strftime("%d/%m/%y")
        if "--dateus" in args:
            output = currentTime.strftime("%x")
        if "--bare" in args:
            output = currentTime
        if "--pretty" in args:
            output = currentTime.strftime("%H:%M:%S, %d %b %Y")
    elif len(args) > 1:
        output = "time: too many positional arguments were provided."
    else:
        output = currentTime.strftime("%H:%M:%S")

    if len(args) > 0 and args[0] not in validArgs:
        output = f"time: positional argument '{args[0]}' not recognised."

    return output

def man(args=[]):
    output = "Prints the time/date to the screen.\nSupports positional arguments:\n--date: provides the date.\n--dateus: provides the date in US format.\n--bare: provides the date in the standard way that datetime provides the data.\n--pretty: prints the time and the date at the same time in a human readable format."
    return output
    