# -*- coding: utf8 -*-

from coverage import coverage

cov = coverage(branch=True, omit=['flask/*', 'tests.py'])
cov.start()

import os
import unittest
from datetime import datetime, timedelta


class TestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass

if __name__ == '__main__':
    try:
        unittest.main()
    except:
        pass
    cov.stop()
    cov.save()
    print("\n\nCoverage Report:\n")
    cov.report()
    print("\nHTML version: " + os.path.join(basedir, "tmp/coverage/index.html"))
    cov.html_report(directory='tmp/coverage')
    cov.erase()
