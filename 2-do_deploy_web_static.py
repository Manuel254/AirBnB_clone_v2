#!/usr/bin/python3
from fabric.api import *
import os
from pathlib import Path
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['100.25.138.30', '34.224.1.8']


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


def do_deploy(archive_path):
    """Distributes an archive to web server"""
    fname = Path(archive_path).stem
    static = "/data/web_static/releases/"
    link = "/data/web_static/current"

    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/')
    fname = Path(archive_path).stem
    run('mkdir -p {}{}'.format(static, fname))
    run('tar -xzf /tmp/{}.tgz -C {}{}/'.format(fname, static, fname))
    run('rm /tmp/{}.tgz'.format(fname))
    run('rm -rf {}'.format(link))
    run('ln -s {}/{} {}'.format(static, fname, link))

    return True
