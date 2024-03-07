#!/usr/bin/python3
""" Fabric script that deletes out-of-date archives """
from fabric.api import *

env.hosts = ['18.204.9.11', '18.233.66.83']
env.user = "ubuntu"


def do_clean(number=0):
    """ Deletes out-of-date archives """

    number = max(1, int(number))

    # Delete local archives except the most recent 'number' ones
    local('ls -t versions | tail -n +{} | xargs rm -rf'.format(number + 1))

    # Delete remote archives except the most recent 'number' ones
    run('ls -t /data/web_static/releases | tail -n +{} | xargs rm -rf'.
        format(number + 1))
