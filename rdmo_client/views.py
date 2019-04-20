from .client.rest import RESTClient


class ViewsMixin(RESTClient):

    views_url = 'views/views/'

    def list_views(self, **kwargs):
        return self.list(self.views_url, **kwargs)

    def index_views(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.views_url, **kwargs)

    def retrieve_view(self, pk):
        return self.retrieve(self.views_url, pk)

    def create_view(self, data):
        return self.create(self.views_url, data)

    def update_view(self, pk, data):
        return self.update(self.views_url, pk, data)

    def destroy_view(self, pk):
        return self.destroy(self.views_url, pk)
