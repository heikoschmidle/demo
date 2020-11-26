import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "demo",
    version = "0.0.1",
    author = "Heiko Schmidle",
    description = ("An demonstration fro Nextjournal"),
    license = "BSD",
    keywords = "Nextjournal",
    long_description=read('README')
)
