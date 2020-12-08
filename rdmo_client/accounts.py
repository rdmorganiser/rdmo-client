from .client.rest import RESTClient


class AccountsMixin(RESTClient):

    users_url = 'accounts/users/'

    def list_users(self, **kwargs):
        return self.list(self.users_url, **kwargs)

    def retrieve_user(self, pk):
        return self.retrieve(self.users_url, pk)
