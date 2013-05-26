#!/usr/bin/python

import os
import urllib2

import config

def get_url(dist, section, arch):
    repo = config.REPOS[dist]
    return '%(base)s/dists/%(dist)s/%(section)s/binary-%(arch)s/Packages.bz2' % \
        dict(base=config.BASE_URLS[repo],
             dist=dist,
             section=section,
             arch=arch)

def get_target(dist, section, arch):
    return os.path.join(config.DOWNLOAD_DIR, dist, section, 'binary-%s' % arch)

def download(dist, section, arch):
    url = get_url(dist, section, arch)
    target = get_target(dist, section, arch)
    path = os.path.join(target, 'Packages.bz2')

    if not os.path.exists(target):
        os.makedirs(target)

    try:
        fin = urllib2.urlopen(url)
        fout = open(path, 'wb')
        fout.write(fin.read())
        fout.close()
        fin.close()

        return True
    except urllib2.HTTPError:
        return False

def main():
    total = len(config.DISTS) * len(config.SECTIONS) * len(config.ARCHS)
    count = 0

    for dist in config.DISTS:
        for section in config.SECTIONS:
            for arch in config.ARCHS:
                status = download(dist, section, arch)
                status = status and 'OK' or 'FAIL'

                count += 1
                print '%s of %s: %s %s %s -> %s' % \
                      (count, total, dist, section, arch, status)

if __name__ == '__main__':
    main()

