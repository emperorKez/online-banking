import os

env = os.environ.get('DJANGO_ENV', 'production')

if env == 'production':
    from .prod import *
else:
    from .prod import *