from .http import HTTPClient


class RESTClient(HTTPClient):

    def _build_url(self, resource_url, kwargs, pk=None):
        url = resource_url.rstrip('/') + '/'

        if 'list_route' in kwargs:
            url += kwargs.pop('list_route').rstrip('/') + '/'
        elif 'nested_route' in kwargs:
            url += '%i/' % kwargs.pop('parent_pk')
            url += kwargs.pop('nested_route').rstrip('/') + '/'

        if pk:
            url += '%i/' % pk

        if 'detail_route' in kwargs:
            url += kwargs.pop('detail_route').rstrip('/') + '/'

        return url

    def list(self, resource_url, **kwargs):
        url = self._build_url(resource_url, kwargs)
        return self.get(url, params=kwargs)

    def retrieve(self, resource_url, pk, **kwargs):
        url = self._build_url(resource_url, kwargs, pk)
        return self.get(url)

    def create(self, resource_url, data, **kwargs):
        url = self._build_url(resource_url, kwargs)
        return self.post(url, data)

    def update(self, resource_url, pk, data, **kwargs):
        url = self._build_url(resource_url, kwargs, pk)
        return self.put(url, data)

    def destroy(self, resource_url, pk, **kwargs):
        url = self._build_url(resource_url, kwargs, pk)
        return self.delete(url) #pk included in url, thats sufficient
