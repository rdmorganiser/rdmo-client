from .client import Client


class Accounts(Client):

    @property
    def users(self):
        return self.get('accounts/users/')

    def user(self, pk):
        return self.get('accounts/users/%d' % pk)
