class QuestionsMixin(object):

    catalogs_url = 'questions/catalogs/'
    pages_url = 'questions/pages/'
    sections_url = 'questions/sections/'
    questionsets_url = 'questions/questionsets/'
    questions_url = 'questions/questions/'
    valuetypes_url = 'questions/valuetypes/'
    widgettypes_url = 'questions/widgettypes/'

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

    def list_pages(self, **kwargs):
        return self.list(self.pages_url, **kwargs)

    def index_pages(self, **kwargs):
        kwargs.update({'list_route': 'index'})
        return self.list(self.pages_url, **kwargs)

    def nest_pages(self, **kwargs):
        kwargs.update({'list_route': 'nested'})
        return self.list(self.pages_url, **kwargs)

    def retrieve_page(self, pk):
        return self.retrieve(self.pages_url, pk)

    def create_page(self, data):
        return self.create(self.pages_url, data)

    def update_page(self, pk, data):
        return self.update(self.pages_url, pk, data)

    def destroy_page(self, pk):
        return self.destroy(self.pages_url, pk)

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
