#!/usr/bin/python3
"""Deployment process: Stage 1"""
import time
from fabric.api import local


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
