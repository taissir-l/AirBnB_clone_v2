#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.19.204', '54.157.159.85']


def do_clean(number=0):
    """out-of-date archives delete

    Args:
        number (int): number of archives to keep.

    number is 0 or 1then  keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives...
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
