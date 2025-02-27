class ProjectsMixin:

    projects_url = 'projects/projects/'
    snapshots_url = 'projects/snapshots/'
    values_url = 'projects/values/'

    def list_projects(self, **kwargs):
        return self.list(self.projects_url, **kwargs)

    def retrieve_project(self, pk):
        return self.retrieve(self.projects_url, pk)

    def create_project(self, data):
        return self.create(self.projects_url, data)

    def update_project(self, pk, data):
        return self.update(self.projects_url, pk, data)

    def destroy_project(self, pk):
        return self.destroy(self.projects_url, pk)

    def resolve_project_condition(self, pk, condition):
        return self.retrieve(self.projects_url, pk, detail_route='resolve', condition=condition)

    def list_project_snapshots(self, parent_pk, **kwargs):
        kwargs.update({'nested_route': 'snapshots', 'parent_pk': parent_pk})
        return self.list(self.projects_url, **kwargs)

    def retrieve_project_snapshot(self, parent_pk, pk):
        return self.retrieve(self.projects_url, pk, nested_route='snapshots', parent_pk=parent_pk)

    def create_project_snapshot(self, parent_pk, data):
        return self.create(self.projects_url, data, nested_route='snapshots', parent_pk=parent_pk)

    def update_project_snapshot(self, parent_pk, pk, data):
        return self.update(self.projects_url, pk, data, nested_route='snapshots', parent_pk=parent_pk)

    def list_project_values(self, parent_pk, **kwargs):
        kwargs.update({'nested_route': 'values', 'parent_pk': parent_pk})
        return self.list(self.projects_url, **kwargs)

    def retrieve_project_value(self, parent_pk, pk):
        return self.retrieve(self.projects_url, pk, nested_route='values', parent_pk=parent_pk)

    def create_project_value(self, parent_pk, data):
        return self.create(self.projects_url, data, nested_route='values', parent_pk=parent_pk)

    def update_project_value(self, parent_pk, pk, data):
        return self.update(self.projects_url, pk, data, nested_route='values', parent_pk=parent_pk)

    def list_snapshots(self, **kwargs):
        return self.list(self.snapshots_url, **kwargs)

    def retrieve_snapshot(self, pk):
        return self.retrieve(self.snapshots_url, pk)

    def create_snapshot(self, data):
        return self.create(self.snapshots_url, data)

    def update_snapshot(self, pk, data):
        return self.update(self.snapshots_url, pk, data)

    def destroy_snapshot(self, pk):
        return self.destroy(self.snapshots_url, pk)

    def list_values(self, **kwargs):
        return self.list(self.values_url, **kwargs)

    def retrieve_value(self, pk):
        return self.retrieve(self.values_url, pk)

    def create_value(self, data):
        return self.create(self.values_url, data)

    def update_value(self, pk, data):
        return self.update(self.values_url, pk, data)

    def destroy_value(self, pk):
        return self.destroy(self.values_url, pk)
