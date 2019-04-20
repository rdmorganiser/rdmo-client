from .rest import RESTClient

__title__ = 'rdmo_client'
__version__ = '0.12.0'
__author__ = 'Jochen Klar'
__email__ = 'mail@jochenklar.de'
__license__ = 'Apache-2.0'
__copyright__ = 'Copyright 2019 Jochen Klar'

VERSION = __version__


class Client(RESTClient):

    conditions_url = 'conditions/conditions/'

    attributes_url = 'domain/attributes'

    optionsets_url = 'options/optionsets/'
    options_url = 'options/options/'

    catalogs_url = 'questions/catalogs/'
    sections_url = 'questions/sections/'
    questionsets_url = 'questions/questionsets/'
    questions_url = 'questions/questions/'
    valuetypes_url = 'questions/valuetypes/'
    widgettypes_url = 'questions/widgettypes/'

    tasks_url = 'tasks/tasks/'

    views_url = 'views/views/'

    def __init__(self, url, auth=None, token=None, version=1):
        self.base_url = '%s/api/v%d/' % (url, version)
        self.auth = auth

        if token:
            self.headers = {
                'Authorization': 'Token %s' % token
            }
        else:
            self.headers = {}

    # conditions

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

    # domain

    def list_attributes(self, **kwargs):
        return self.list(self.attributes_url, **kwargs)

    def nest_attributes(self, **kwargs):
        kwargs.update({'list_route': 'nested'})
        return self.list(self.attributes_url, **kwargs)

    def retrieve_attribute(self, pk):
        return self.retrieve(self.attributes_url, pk)

    def create_attribute(self, data):
        return self.create(self.attributes_url, data)

    def update_attribute(self, pk, data):
        return self.update(self.attributes_url, pk, data)

    def destroy_attribute(self, pk):
        return self.destroy(self.attributes_url, pk)

    # options

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

    # questions

    def list_catalogs(self, **kwargs):
        return self.list(self.catalogs_url, **kwargs)

    def index_catalogs(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.catalogs_url, **kwargs)

    def nest_catalogs(self, **kwargs):
        kwargs.update({'list_route': 'nested'})
        return self.list(self.catalogs_url, **kwargs)

    def retrieve_catalog(self, pk):
        return self.retrieve(self.catalogs_url, pk)

    def create_catalog(self, data):
        return self.create(self.catalogs_url, data)

    def update_catalog(self, pk, data):
        return self.update(self.catalogs_url, pk, data)

    def destroy_catalog(self, pk):
        return self.destroy(self.catalogs_url, pk)

    def list_sections(self, **kwargs):
        return self.list(self.sections_url, **kwargs)

    def index_sections(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.sections_url, **kwargs)

    def nest_sections(self, **kwargs):
        kwargs.update({'list_route': 'nested'})
        return self.list(self.sections_url, **kwargs)

    def retrieve_section(self, pk):
        return self.retrieve(self.sections_url, pk)

    def create_section(self, data):
        return self.create(self.sections_url, data)

    def update_section(self, pk, data):
        return self.update(self.sections_url, pk, data)

    def destroy_section(self, pk):
        return self.destroy(self.sections_url, pk)

    def list_questionsets(self, **kwargs):
        return self.list(self.questionsets_url, **kwargs)

    def index_questionsets(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.questionsets_url, **kwargs)

    def nest_questionsets(self, **kwargs):
        kwargs.update({'list_route': 'nested'})
        return self.list(self.questionsets_url, **kwargs)

    def retrieve_questionset(self, pk):
        return self.retrieve(self.questionsets_url, pk)

    def create_questionset(self, data):
        return self.create(self.questionsets_url, data)

    def update_questionset(self, pk, data):
        return self.update(self.questionsets_url, pk, data)

    def destroy_questionset(self, pk):
        return self.destroy(self.questionsets_url, pk)

    def list_questions(self, **kwargs):
        return self.list(self.questions_url, **kwargs)

    def index_questions(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.questions_url, **kwargs)

    def nest_questions(self, **kwargs):
        kwargs.update({'list_route': 'nested'})
        return self.list(self.questions_url, **kwargs)

    def retrieve_question(self, pk):
        return self.retrieve(self.questions_url, pk)

    def create_question(self, data):
        return self.create(self.questions_url, data)

    def update_question(self, pk, data):
        return self.update(self.questions_url, pk, data)

    def destroy_question(self, pk):
        return self.destroy(self.questions_url, pk)

    def list_valuetypes(self, **kwargs):
        return self.list(self.valuetypes_url)

    def list_widgettypes(self, **kwargs):
        return self.list(self.widgettypes_url)

    # tasks

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

    # views

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
