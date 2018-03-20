# epydoc -- Backwards compatibility
#
# Copyright (C) 2005 Edward Loper
# Author: Edward Loper <edloper@loper.org>
# URL: <http://epydoc.sf.net>
#
# $Id: util.py 956 2006-03-10 01:30:51Z edloper $

"""
Backwards compatibility with previous versions of Python.
"""
__docformat__ = 'epytext'

import sys

try:
    import builtins
except ImportError:
    import __builtin__ as builtins

try:
    basestring = builtins.basestring
except AttributeError:
    basestring = (str, )


PY3 = sys.version_info >= (3, 0)
