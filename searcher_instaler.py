import shutil;
import os;
from subprocess import Popen;os.chdir("\\".join(os.getcwd().split("\\")[:-1]));shutil.rmtree(os.getcwd()+"\\searcher",ignore_errors=1);Popen(["git","clone","https://github.com/hugoocf/searcher.git"])
