#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""


from fabric.api import *
import os

env.host = ["35.237.196.218", "34.224.58.38"]
env.user = "ubuntu"


def do_deploy(archive_path):

    if not os.path.exists(archive_path):
        return False

    results = []
    res = put(archive_path, "/tmp")
    result.append(res.succeeded)
    
    filename = os.path.filename(archive_path)
    if filename[-4:] == ".tgz":
        name = filename[:-4]
    newdir = "/data/web_static/releases/" + name
    run("mkdir -p" + newdir)
    run("tar -xzf /tmp/" + filename + "-C" + newdir)

    run("rm /tmp/" + filename)
    run("mv" + newdir + "/web_static/*" + newdir)
    run("rm -rf" + newdir + "/web_static/")
    run("rm -rf /data/web_static/current")
    run("ln -s" + newdir + "/data/web_static/current")
    return True

    
