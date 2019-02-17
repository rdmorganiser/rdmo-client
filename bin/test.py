from rdmo_client import RDMOClient

BASE_URL = 'http://localhost:8000'
TOKEN = 'e925d7a5acf5daf0a4553da633d9b2e6d96b33a9'

OPTIONSET = {
    'key': 'colors'
}
OPTIONS = [
    {
        'key': 'red',
        'title_de': 'rot',
        'title_en': 'red',
        'order': 1
    },
    {
        'key': 'green',
        'title_de': 'grün',
        'title_en': 'green',
        'order': 2
    },
    {
        'key': 'blue',
        'title_de': 'blau',
        'title_en': 'blue',
        'order': 3
    },
    {
        'key': 'yellow',
        'title_de': 'gelb',
        'title_en': 'yellow',
        'order': 4
    }
]

client = RDMOClient(BASE_URL, token=TOKEN)

optionset = client.options.create_optionset(OPTIONSET)

for option in OPTIONS:
    client.options.create_option(dict(option, optionset=optionset['id']))
