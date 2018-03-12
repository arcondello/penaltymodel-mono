from __future__ import absolute_import
import os

import nox


@nox.session
def default(session):
    session.install('-r', 'requirements.txt')
    session.install('-e', '.')

    session.run('python', '-m', 'unittest', 'discover')


@nox.session
@nox.parametrize('py', ['2.7', '3.4', '3.5', '3.6'])
def unit(session, py):
    """Run the unit test suite."""

    # Run unit tests against all supported versions of Python.
    session.interpreter = 'python{}'.format(py)

    # Set the virtualenv dirname.
    session.virtualenv_dirname = 'unit-' + py

    default(session)
