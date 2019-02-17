import re

from setuptools import setup, find_packages

with open('rdmo_client/__init__.py') as f:
    metadata = dict(re.findall(r'__(.*)__ = [\']([^\']*)[\']', f.read()))

setup(
    name=metadata['title'],
    version=metadata['version'],
    author=metadata['author'],
    author_email=metadata['email'],
    maintainer=metadata['author'],
    maintainer_email=metadata['email'],
    license=metadata['license'],
    url='https://github.com/rdmorganiser/rdmo-client',
    description=u'',
    long_description=open('README.md').read(),
    install_requires=[
        'requests>=2.21.0',
        'simplejson>=3.16.0'
    ],
    classifiers=[
        # https://pypi.org/classifiers/
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    packages=find_packages(),
    include_package_data=True
)
