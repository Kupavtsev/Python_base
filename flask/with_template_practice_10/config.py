DEBUG = True
SECRET_KEY = 'key'
WTF_CSRF_ENABLED = False

try:
    from config_local import *
except ImportError:
    pass
