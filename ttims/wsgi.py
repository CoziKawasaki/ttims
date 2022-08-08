import os
from sys import path
from pathlib import Path

path.insert(0, Path(__file__).parents[1])
os.chdir(Path(__file__).parents[1])

from run import app as application
