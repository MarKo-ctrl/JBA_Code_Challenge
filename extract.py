import os.path
import sys

try:
    import pyperclip
except ModuleNotFoundError:
    pass


def get_path():
	"""
    When the program starts, this function:
    - Checks if a valid file path is given as an argument
    - Checks if a valid file path is copied to the clipboard (pyperclip is
    required)
    - As last option, the function asks the user for a valid file path
    """

    if len(sys.argv) == 2 and os.path.isfile(sys.argv[1]):
        path = sys.argv[1]
    elif os.path.isfile(pyperclip.paste()):
        path = pyperclip.paste()
    else:
        path = input("Please enter filepath:\n")
    return path


def load(path):
	"""
    Loads data from user provided file path.
    Returns a list of strings; each strings correspoonds to one line in
    text file. Also returns a list containing the header of the text file.
    """
    with open(path, "r", encoding="utf-8") as d:
        header = [d.readline() for _ in range(5)]
        lines = d.readlines()
    return lines, header
