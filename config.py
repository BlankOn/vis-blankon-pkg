
<<<<<<< HEAD
DOWNLOAD_DIR = 'data'

ARCHS = ['i386', 'amd64', 'armel', 'armhf']
=======
ARCHS = ['i386', 'amd64']
>>>>>>> fajran/master

SECTIONS = ('main', 'extras', 'extras-restricted', 'restricted')

DISTS = [
    'rote', 'suroboyo' 
]

REPOS = {
    'rote': 'current',
    'suroboyo': 'current',
}

BASE_URLS = {
    'current': 'http://arsip.blankonlinux.or.id/blankon',
    'old': 'http://arsip.blankonlinux.or.id/blankon-legacy'
}

