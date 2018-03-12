from __future__ import absolute_import
import os

import nox


@nox.session
def default(session):
    session.install('-r', 'requirements.txt')
    session.install('-e', '.')

    session.run('python', '-m', 'unittest', 'discover')
