from .client import Client


class Options(Client):

    def get_optionsets(self):
        return self.get('options/optionsets/')

    def get_optionset(self, pk):
        return self.get('options/optionsets/%i/' % pk)

    def create_optionset(self, data):
        return self.post('options/optionsets/', data)

    def update_optionset(self, pk, data):
        return self.put('options/optionsets/%i/' % pk, obj)

    def delete_optionset(self, pk):
        return self.delete('options/optionsets/%i/' % pk)

    def get_options(self):
        return self.get('options/options/')

    def get_option(self, pk):
        return self.get('options/options/%i/' % pk)

    def create_option(self, data):
        return self.post('options/options/', data)

    def update_option(self, pk, data):
        return self.put('options/options/%i/' % pk, obj)

    def delete_option(self, pk):
        return self.delete('options/options/%i/' % pk)
