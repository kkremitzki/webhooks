# -*- coding: utf-8 -*-

import sys, os, pwd

project = "webhooks"

BASE_DIR = os.path.join(os.path.dirname(__file__))
# activate virtualenv
activate_this = os.path.join(BASE_DIR, "env/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

if BASE_DIR not in sys.path:
    sys.path.append(BASE_DIR)

# give wsgi the "application"
from webhooks import application
