"""
IE Titanic utils.

"""

__version__="0.1.0" #semver.org (semantic versioning)

import pandas as pd

print(__name__)

def tokenize(text):
    return text.split()


if __name__ == "__main__":
    print(tokenize("Hello World"))
