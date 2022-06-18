import os
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def find_python_files(dir, subdir=None):
    out = []
    for i in os.listdir(dir):
        if i.startswith(".") or i.startswith("_"):
            continue
        new_dir = os.path.join(dir, i)
        if subdir is None:
            new_subdir = i
        else:
            new_subdir = os.path.join(subdir, i)
        if os.path.isdir(new_dir):
            out += find_python_files(new_dir, new_subdir)
        elif i.endswith(".ipynb"):
            out.append(new_subdir)
    return out


tutorial_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..")
tutorials = find_python_files(tutorial_dir)


@pytest.mark.parametrize("notebook", tutorials)
def test_tutorial(notebook):
    with open(os.path.join(tutorial_dir, notebook)) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600)

    ep.preprocess(nb, {"metadata": {"path": path}})
