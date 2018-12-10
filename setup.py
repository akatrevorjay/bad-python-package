#!/usr/bin/env python

import logging
import warnings

import setuptools
import setuptools.command
import setuptools.command.develop as scd
import setuptools.command.install as sci

import pkg_utils

log = logging.getLogger(__name__)


class UserError(Exception):
    """ PEBKAC """


def _nope(marker=''):
    if marker:
        marker = '[%s] ' % marker
    raise UserError("%sI bet you meant to pip install a different package, didn't you?" % marker)


class PostDevelopCommand(scd.develop):
    """Post-installation for development mode."""

    def run(self):
        _nope()


class PostInstallCommand(sci.install):
    """Post-installation for installation mode."""

    def run(self):
        _nope()


with open('README.rst', 'r') as fh:
    readme = fh.read()

_cmdclass = dict(
    develop=PostDevelopCommand,
    install=PostInstallCommand,
)

_conf = dict(
    name='bad-python-package',
    summary='no regrets',
    author='Trevor Joynson',
    author_email='github@skywww.net',
    long_description=readme,
    license='Private',
    cmdclass=_cmdclass,
    packages=setuptools.find_packages(),
    version='0.0.1',
    keywords=['move-along', 'nothing-to-see-here'],
    classifiers=[
        # This marker prevents accidental uploads to public PyPi.
        'Private :: Do Not Upload'
    ],
)

_conf.update(pkg_utils.setup_requirements())

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    setuptools.setup(**_conf)
