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
    directory = "{}/versions/".format(cwd)
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "{}web_static_{}.tgz".format(directory, now)
    archive = "tar -cvzf {} web_static/"

    if not os.path.isdir(directory):
        os.mkdir(directory)
    local(archive.format(path))

    if os.path.exists(path):
        return path


def do_deploy(archive_path):
    """Distributes an archive to web server"""
    fname = Path(archive_path).stem
    static = "/data/web_static/releases/"
    link = "/data/web_static/current"

    if not os.path.exists(archive_path):
        return False

    put(archive_path, '/tmp/')
    run('mkdir -p {}{}/'.format(static, fname))
    run('tar -xzf /tmp/{}.tgz -C {}{}/'.format(fname, static, fname))
    run('rm /tmp/{}.tgz'.format(fname))
    run('mv {}{}/web_static/* {}{}/'.format(static, fname, static, fname))
    run('rm -rf {}{}/web_static/'.format(static, fname))
    run('rm -rf {}'.format(link))
    run('ln -s {}{} {}'.format(static, fname, link))

    return True


def deploy():
    """Creates and distributes archives"""
    path = do_pack()
    if not path:
        return False
    return do_deploy(path)
