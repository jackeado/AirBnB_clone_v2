#!/usr/bin/python3
"""
A Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack
"""


from fabric.api import local
import datetime


def do_pack():
    local("mkdir -p versions")
    date = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    temp = "web_static_" + date + ".tgz"
    res = local("tar -cvzf versions/{} web_static".format(temp))
    path = "versions/" + temp
    if res.succeeded:
        return(path)
    else:
        return(None)
