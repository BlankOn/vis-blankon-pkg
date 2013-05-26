
ARCHS = ['i386', 'amd64', 'armel', 'armhf']

SECTIONS = ('main', 'extras', 'extras-restricted', 'restricted')

DISTS = [
    'ombilin', 'pattimura', 'rote', 'suroboyo' 
]

REPOS = {
    'ombilin': 'old',
    'pattimura': 'old',
    'rote': 'current',
    'suroboyo': 'current',
}

BASE_URLS = {
    'current': 'http://arsip.blankonlinux.or.id/blankon',
    'old': 'http://arsip.blankonlinux.or.id/blankon-legacy'
}

