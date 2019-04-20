class ConditionsMixin(object):

    conditions_url = 'conditions/conditions/'

    def list_conditions(self, **kwargs):
        return self.list(self.conditions_url, **kwargs)

    def index_conditions(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.conditions_url, **kwargs)

    def retrieve_condition(self, pk):
        return self.retrieve(self.conditions_url, pk)

    def create_condition(self, data):
        return self.create(self.conditions_url, data)

    def update_condition(self, pk, data):
        return self.update(self.conditions_url, pk, data)

    def destroy_condition(self, pk):
        return self.destroy(self.conditions_url, pk)
