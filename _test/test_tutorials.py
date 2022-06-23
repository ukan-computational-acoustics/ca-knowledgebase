import os
import pytest
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def find_notebooks(dir):
    out = []
    for i in os.listdir(dir):
        if i.startswith(".") or i.startswith("_"):
            continue
        if os.path.isdir(os.path.join(dir, i)):
            out += find_notebooks(os.path.join(dir, i))
        elif i.endswith(".ipynb"):
            out.append((dir, i))
    return out


tutorial_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    "..")
tutorials = find_notebooks(tutorial_dir)


@pytest.mark.parametrize("path, notebook", tutorials)
def test_tutorial(path, notebook):
    with open(os.path.join(path, notebook)) as f:
        nb = nbformat.read(f, as_version=4)

    ep = ExecutePreprocessor(timeout=600)

    ep.preprocess(nb, {"metadata": {"path": path}})
