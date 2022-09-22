#!/usr/bin/python3
"""Deployment process: Stage 3"""
import time
from os.path import exists
from fabric.api import run, put, local, env

env.hosts = ['34.203.35.182', '54.91.166.190']


def do_pack():
    """Returns the file path if has been correctly generated.
    Otherwise, returns none"""
    timest = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timest))
        return ("versions/web_static_{:s}.tgz".format(timest))
    except Exception:
        return None


def do_deploy(archive_path):
    """Recieves an archive pack and deploys it to the web server"""
    if exists(archive_path) is False:
        return False

    try:
        file_n = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_n, path, no_ext))
        run('rm /tmp/{}'.format(file_n))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception as e:
        print(e)
        return False


def deploy():
    """Deploy function with do_pack and do_deploy"""
    archive_path = do_pack()
    if archive_path is None:
        return False

    return (do_deploy(archive_path))
