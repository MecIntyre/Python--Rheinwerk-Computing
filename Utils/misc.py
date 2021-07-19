import os
import sys

def printEnvironment():
    for variable, value in os.environ.items():
        print(variable, '=', value)
    print()

    print("PYTHONPATH = ", os.environ.get('PYTHONPATH', '<existiert nicht>'))

    for p in sys.path:
        print(p)