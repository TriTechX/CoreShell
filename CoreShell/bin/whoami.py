import os
import getpass

def whoami(args=[]):
    user = getpass.getuser()

    return user

def man(args=[]):
    output = "Provides you with your username in the host OS. This command has no positional arguments. Providing them will have no effect."
    return output