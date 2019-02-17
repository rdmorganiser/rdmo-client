__title__ = 'rdmo_client'
__version__ = '0.12.0'
__author__ = 'Jochen Klar'
__email__ = 'mail@jochenklar.de'
__license__ = 'Apache-2.0'
__copyright__ = 'Copyright 2019 Jochen Klar'

VERSION = __version__

from .client import Client
from .accounts import Accounts
from .options import Options


class RDMOClient(object):

    def __init__(self, url, token=None, version=1):
        base_url = '%s/api/v%d/' % (url, version)
        headers = {}
        if token:
            headers['Authorization'] = 'Token %s' % token

        self.accounts = Client(base_url, headers)
        self.options = Options(base_url, headers)
