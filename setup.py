from distutils.core import setup

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Database',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6'
    ]

install_requires = []

tests_require = [
    'flask',
    'flask_graphql',
    'graphene',
    'requests']

setup(
    name='MinGraphQLClient',
    description='Minimalistic GraphQL client for Python 3',
    keywords='simple graphql client',
    license='MIT',
    author='Filipp W.',
    author_email='whfilipp@gmail.com',
    url='https://github.com/filippw/MinGraphQLClient',
    download_url='https://github.com/filippw/MinGraphQLClient/archive/master.zip',
    version='1.0.0a1',
    install_requires=install_requires,
    tests_require=tests_require,
    packages=['mingraphqlclient'],
    classifiers=classifiers
    )
    
