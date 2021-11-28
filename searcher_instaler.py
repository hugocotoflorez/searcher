import os
from subprocess import Popen
os.remove(os.getcwd()+"\searcher.py")
os.chdir("\".join(os.getcwd().split("\")[:-1]))
Popen(['git','clone','https://github.com/hugoocf/searcher.git'])
