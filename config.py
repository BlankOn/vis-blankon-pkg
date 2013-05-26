
ARCHS = ['i386', 'amd64', 'armel', 'armhf']

SECTIONS = ('main', 'extras', 'extras-restricted', 'restricted')

DISTS = [
    'konde', 'lontara', 'meuligoe', 'nanggar', 'ombilin', 'pattimura', 'rote', 'suroboyo' 
]

REPOS = {
    'konde': 'old',
    'lontara': 'old',
    'meuligoe': 'old',
    'nanggar': 'old',
    'ombilin': 'old',
    'pattimura': 'old',
    'rote': 'current',
    'suroboyo': 'current',
}

BASE_URLS = {
    'current': 'http://arsip.blankonlinux.or.id/blankon',
    'old': 'http://arsip.blankonlinux.or.id/blankon-legacy'
}

