# -*- coding: utf-8 -*-
#!/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function

import os
import sys
import locale
import logging
import warnings

import six
import requests
import requests_html


try:
    import curses
except ImportError:
    if sys.platform == "win32":
        sys.exit("Fatal Error: This program is not compatible with Windows"
                 "Operating systems. \n Please try installing on either Linux"
                 "or Mac OS")
    else:
        sys.exit("Fatal Error: Your python distribution appears to be missing"
                "_curses.so.\nWas it compiled without support for curses?")


webbrowser_import_warning = ("webbrowser" in sys.modules")
NTV_BROWSER, BROWSER = os.environ.get("NTV_BROWSER"), os.environ.get("BROWSER")

if NTV_BROWSER:
    os.environ["BROWSER"] = NTV_BROWSER

#from . import docs
#from . import packages
#from .packages import praw
#from .config import Config, copy_default_config, copy_default_mailcap
#from .theme import Theme
#from .oath import OAuthHelper
#from .terminal import Terminal
#from .content import RequestHeaderRateLimiter
#from .objects import curses_session, patch_webbrowser
# from .subreddit_page import SubredditPage
#from .exceptions import ConfigError, SubredditError
from .__version__ import __version__
