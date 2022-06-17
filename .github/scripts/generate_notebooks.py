import os
import pytest


def convert_python_files(dir):
    for i in os.listdir(dir):
        if i.startswith("."):
            continue
        new_dir = os.path.join(dir, i)
        if os.path.isdir(new_dir):
            out += find_python_files(new_dir)
        elif i.endswith(".py"):
            os.system(f"jupytest --to ipynb {dir}")


root_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..")

convert_python_files(root_dir)
