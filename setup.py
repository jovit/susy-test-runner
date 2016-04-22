try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Test Runner For Susy',
    'author': 'Joao Vitor Araki Goncalves',
    'author_email': 'joao_vitor_araki_goncalves@hotmail.com',
    'version': '0.1',
    'install_requires': ['nose','requests','argcomplete'],
    'scripts': ['bin/test-runner'],
    'name': 'test-runner'
}

setup(**config)
