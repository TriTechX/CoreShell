import subprocess

def kern(args=[]):
    kernCmd = subprocess.run(args, capture_output=True, text=True)
    output = kernCmd.stdout.strip("\n")

    return output

def man(args=[]):
    output = "Runs commands through your system's terminal.\nYou can perform most basic and some advanced actions through here, but some access is restricted by the subprocess module's limitations.\nA good way to get things done that CoreShell can't do."
    return output

