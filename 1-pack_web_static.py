#!/usr/bin/python3
from fabric.api import *
import os
from datetime import datetime


def do_pack():
    """This function generates a .tgz archive from
    the contents of the web_static folder
    """
    cwd = os.getcwd()
    ver_dir = "{}/versions/".format(cwd)
    web_static = "web_static"
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    hour = datetime.now().hour
    mins = datetime.now().minute
    sec = datetime.now().second
    comp = "tar -cvzf {}web_static_{}{:02d}{:02d}{:02d}{:02d}{:02d}.tgz {}"

    if not os.path.isdir(ver_dir):
        os.mkdir(ver_dir)
    local(comp.format(ver_dir, year, month, day, hour, mins, sec, web_static))
