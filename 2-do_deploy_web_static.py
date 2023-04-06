#!/usr/bin/python3
from fabric.api import put, run, local, env
from os import path


env.hosts = ["54.160.101.122", "54.237.51.149"]


def do_deploy(archive_path):
    """
    Will distribute an archve to my web servers
    """

    if path.exists(archive_path):
        archive = archive_path.split('/')[1]
        a_path = "/tmp/{}".format(archive)
        folder = archive.split('.')[0]
        fold_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, a_path)
        run("mkdir -p {}".format(fold_path))
        run("tar -xzf {} -C {}".format(a_path, fold_path))
        run("rm {}".format(a_path))
        run("mv -f {}web_static/* {}".format(fold_path, fold_path))
        run("rm -rf {}web_static".format(fold_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(fold_path))

        return True
    return False
