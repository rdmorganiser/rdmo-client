class TasksMixin(object):

    tasks_url = 'tasks/tasks/'

    def list_tasks(self, **kwargs):
        return self.list(self.tasks_url, **kwargs)

    def index_tasks(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.tasks_url, **kwargs)

    def retrieve_task(self, pk):
        return self.retrieve(self.tasks_url, pk)

    def create_task(self, data):
        return self.create(self.tasks_url, data)

    def update_task(self, pk, data):
        return self.update(self.tasks_url, pk, data)

    def destroy_task(self, pk):
        return self.destroy(self.tasks_url, pk)
