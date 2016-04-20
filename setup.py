try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test Runner For Susy',
    'author': 'Joao Vitor Araki Goncalves',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose','requests','argcomplete'],
    'scripts': ['bin/test-runner'],
    'packages': ['NAME'],
    'name': 'test-runner'
}

setup(**config)
