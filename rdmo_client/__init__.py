from .accounts import AccountsMixin
from .client.rest import RESTClient
from .conditions import ConditionsMixin
from .domain import DomainMixin
from .options import OptionsMixin
from .projects import ProjectsMixin
from .questions import QuestionsMixin
from .tasks import TasksMixin
from .views import ViewsMixin

__title__ = 'rdmo_client'
__version__ = '0.12.0'
__author__ = 'Jochen Klar'
__email__ = 'mail@jochenklar.de'
__license__ = 'Apache-2.0'
__copyright__ = 'Copyright 2019 Jochen Klar'

VERSION = __version__


class Client(AccountsMixin, ConditionsMixin, DomainMixin, OptionsMixin, ProjectsMixin, QuestionsMixin, TasksMixin, ViewsMixin, RESTClient):

    def __init__(self, url, auth=None, token=None, version=1):
        self.base_url = '%s/api/v%d/' % (url, version)
        self.auth = auth

        if token:
            self.headers = {
                'Authorization': 'Token %s' % token
            }
        else:
            self.headers = {}
