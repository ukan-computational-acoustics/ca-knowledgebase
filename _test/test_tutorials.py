import os
import pytest


def find_python_files(dir, subdir=None):
    out = []
    for i in os.listdir(dir):
        print(i)
        new_dir = os.path.join(dir, i)
        if subdir is None:
            new_subdir = i
        else:
            new_subdir = os.path.join(subdir, i)
        if os.path.isdir(new_dir):
            out += find_python_files(new_dir, new_subdir)
        elif i.endswith(".py"):
            out.append(new_subdir)
    return out


tutorial_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    os.path.join("..", "tutorials"))
tutorials = find_python_files(tutorial_dir)


@pytest.mark.parametrize("tutorial", tutorials)
def test_tutorial(tutorial):
    assert os.system(f"python3 {os.path.join(tutorial_dir, tutorial)}") == 0
