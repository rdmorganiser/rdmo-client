class DomainMixin:

    attributes_url = 'domain/attributes'

    def list_attributes(self, **kwargs):
        return self.list(self.attributes_url, **kwargs)

    def nest_attributes(self, pk):
        return self.retrieve(self.attributes_url, pk, list_route='nested')

    def retrieve_attribute(self, pk):
        return self.retrieve(self.attributes_url, pk)

    def create_attribute(self, data):
        return self.create(self.attributes_url, data)

    def update_attribute(self, pk, data):
        return self.update(self.attributes_url, pk, data)

    def destroy_attribute(self, pk):
        return self.destroy(self.attributes_url, pk)
