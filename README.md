# MinGraphQLClient
Minimalistic GrqphQL client for Python 3. Just a simple Python GraphQL client for testing purposes.

## Install
```sh
pip install mingraphqlclient
```
## How to use
```py
 from mingraphqlclient.min_graphql_clinet import MinGraphQLClient
 
 graphql_endpoint = 'http://127.0.0.1:5000/graphql'
 
test_client = MinGraphQLClient(graphql_endpoint)
print(test_client.execute('''
  query {
    person{
        id
        name
        surname
        age
        employed
    }
  }
'''))
```
#### In plans (TODO)
* add graphql query execution via command-line script