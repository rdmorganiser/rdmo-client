from .accounts import AccountsMixin
from .client.rest import RESTClient
from .conditions import ConditionsMixin
from .domain import DomainMixin
from .options import OptionsMixin
from .projects import ProjectsMixin
from .questions import QuestionsMixin
from .tasks import TasksMixin
from .views import ViewsMixin

try:
    from ._version import __version__, __version_tuple__, version, version_tuple
except ImportError:
    __version__ = __version_tuple__ = version = version_tuple = None


class Client(
    AccountsMixin, ConditionsMixin, DomainMixin, OptionsMixin,
    ProjectsMixin, QuestionsMixin, TasksMixin, ViewsMixin, RESTClient
    ):

    def __init__(self, url, auth=None, token=None, version=1):
        self.base_url = f'{url}/api/v{version}/'
        self.auth = auth

        if token:
            self.headers = {
                'Authorization': f'Token {token}'
            }
        else:
            self.headers = {}
