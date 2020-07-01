""" Setup file """

from setuptools import setup, find_packages
from typing import Sequence
from pathlib import Path


def read(fname: str) -> str:
    return open(Path(__file__).parent / fname).read()


def read_requirements(filename: str) -> Sequence[str]:
    return read(filename).splitlines()


settings = dict(
    name='pdoc-test',
    packages=find_packages(exclude=["test"]),
    version='0.0.1',
    author='Carsten-Leue',
    author_email='',
    description=('This is an awesome project!'),
    license='IBM',
    keywords='pdoc-test',
    url='https://github.com/Carsten-Leue/pdoc-test',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    include_package_data=True,
    python_requires='>=3.6',
    install_requires=read_requirements('requirements.txt'),
    tests_require=read_requirements('test-requirements.txt'),
    classifiers=[
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',        
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: IBM',
        'Typing :: Typed'
    ],
    zip_safe=False
)

setup(**settings)
