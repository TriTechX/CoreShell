import os

def echo(args=[]):
    combined = ""
    for item in args:
        combined += item

    output = combined

    return combined

def man(args=[]):
    output = "Returns any text typed where positional arguments would usually be present as raw text.\nSometimes useful for piping."
    return output