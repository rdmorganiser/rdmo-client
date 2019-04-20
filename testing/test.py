from rdmo_client import Client

BASE_URL = 'http://localhost:8000'
AUTH = ('api', 'api')
TOKEN = '8bd704f41e0def27e0406e5ae8ec479ce575aa8f'
URI_PREFIX = 'https://rdmorganiser.github.io/terms/'

client = Client(BASE_URL, auth=AUTH)
# client = RDMOClient(BASE_URL, token=TOKEN)

# OPTIONSET = {
#     'key': 'colors'
# }
# OPTIONS = [
#     {
#         'key': 'red',
#         'title_de': 'rot',
#         'title_en': 'red',
#         'order': 1
#     },
#     {
#         'key': 'green',
#         'title_de': 'grün',
#         'title_en': 'green',
#         'order': 2
#     },
#     {
#         'key': 'blue',
#         'title_de': 'blau',
#         'title_en': 'blue',
#         'order': 3
#     },
#     {
#         'key': 'yellow',
#         'title_de': 'gelb',
#         'title_en': 'yellow',
#         'order': 4
#     }
# ]
# optionset = client.options.create_optionset(OPTIONSET)
# for option in OPTIONS:
#     client.options.create_option(dict(option, optionset=optionset['id']))

# optionsets = client.list_optionsets()
# print(optionsets)

# for option in client.options.list_options(optionset=6):
#     print(option)

# client.options.destroy_optionset(6)
# catalogs = client.list_catalogs()
# print(catalogs)

# catalogs = client.list_sections(catalog=1)
# print(catalogs)

# conditions = client.index_conditions()
# print(conditions)

# attributes = client.list_attributes()
# print(attributes)

# attributes = client.nest_attributes()
# print(attributes)
