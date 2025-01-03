import os
import importlib

#This file ensures that all files from the bin folder are correctly identified by main.
__all__ = []
current_dir = os.path.dirname(__file__)

for filename in os.listdir(current_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = filename[:-3]
        __all__.append(module_name)
        module = importlib.import_module(f"bin.{module_name}")
        globals().update(vars(module))