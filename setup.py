import setuptools
from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='demo',
    version='1.0',
    #packages=['src/agda_kernel'],
#     packages=setuptools.find_packages(where="src"),
#     package_dir={""},
    description='Demo',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Heiko Schmidle',
    url='https://github.com/heikoschmidle/demo',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
    ]
)
