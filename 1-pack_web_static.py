#!/usr/bin/python3
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Will generate a .tgz archive form contents of web_static
    folder of my repo (this one)
    """

    date_t = datetime.today()
    tod = date_t.strftime('%Y%m%d%H%M%S')

    local("mkdir -p versions")
    local("tar -czvf versions/web_static{}.tgz web_static".format(tod))
