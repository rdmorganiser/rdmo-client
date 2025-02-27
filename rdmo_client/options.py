class OptionsMixin:

    optionsets_url = 'options/optionsets/'
    options_url = 'options/options/'

    def list_optionsets(self, **kwargs):
        return self.list(self.optionsets_url, **kwargs)

    def index_optionsets(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.optionsets_url, **kwargs)

    def nest_optionsets(self, **kwargs):
        kwargs.update({'list_route': 'nested'})
        return self.list(self.optionsets_url, **kwargs)

    def retrieve_optionset(self, pk):
        return self.retrieve(self.optionsets_url, pk)

    def create_optionset(self, data):
        return self.create(self.optionsets_url, data)

    def update_optionset(self, pk, data):
        return self.update(self.optionsets_url, pk, data)

    def destroy_optionset(self, pk):
        return self.destroy(self.optionsets_url, pk)

    def list_options(self, **kwargs):
        return self.list(self.options_url, **kwargs)

    def index_options(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.options_url, **kwargs)

    def retrieve_option(self, pk):
        return self.retrieve(self.options_url, pk)

    def create_option(self, data):
        return self.create(self.options_url, data)

    def update_option(self, pk, data):
        return self.update(self.options_url, pk, data)

    def destroy_option(self, pk):
        return self.destroy(self.options_url, pk)
