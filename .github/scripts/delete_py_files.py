import os


def convert_python_files(dir):
    for i in os.listdir(dir):
        if i.startswith(".") or i == "_test":
            continue
        new_dir = os.path.join(dir, i)
        if os.path.isdir(new_dir):
            convert_python_files(new_dir)
        elif i.endswith(".py"):
            os.system(f"rm {new_dir}")


root_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    os.path.join("..", ".."))

convert_python_files(root_dir)
