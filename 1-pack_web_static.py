#!/usr/bin/python3
"""This generates a .tgz archive from the contents of the web_static
   folder of your AirBnB Clone repo."""
from fabric.api import local
from datetime import date
from time import strftime


def do_pack():
    """
    This generates a .tgz archive form contents of web_static
    folder of my repo (this one)
    """

    filename = strftime('%Y%m%d%H%M%S')
    try:
        local("mkdir -p versions")

        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)
    except Exception as e:
        return None
