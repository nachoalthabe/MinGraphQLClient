"""
Contains single GraphQL client class

Based on: https://github.com/graphcool/python-graphql-client
"""

import json

from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.request import Request

class MinGraphQLClient(object):
    """Minimalistic GrqphQL client"""

    def __init__(self, endpoint):
        """
        :param endpoint: url of the used GraphQL endpoint
        :type endpoint: str
        """
        self.endpoint = endpoint
        self._token = None

    def execute(self,
                query,
                variables=None,
                request_enc='ASCII',
                response_enc='ASCII'):
        """
        Execute query

        :param query: query to be executed
        :param variables: variables (if any)
        :param request_enc: request encoding
        :param response_enc: response expected encoding
        :type request_enc: str
        :type response_enc: str
        :type query: str
        :type variables: str

        :returns: response from the executed request
        :rtype: str
        """
        
        return self._send(query,
                          variables,
                          request_enc,
                          response_enc)

    @property
    def token(self):
        """Token getter"""
        
        return self._token
    
    @token.setter
    def token(self, token_value):
        """Token setter"""

        self._token = token_value


    def _send(self, query, variables, request_enc, response_enc):
        """
        Send query to the endpoint

        :param query: query to be sent
        :param variables: variables (if any)
        :param request_enc: request encoding
        :param response_enc: response expected encoding
        :type query: str
        :type variables: str
        :type request_enc: str
        :type response_enc: str
        
        :returns: response from request execution
        :rtype: str
        """

        data = {'query': query,
                'variables': variables}
        headers = {'Accept': 'application/json',
                   'Content-Type': 'application/json'}

        if self.token is not None:
            headers['Authorization'] = 'Bearer %s' % self.token

        req = Request(self.endpoint, json.dumps(data).encode(request_enc), headers)

        try:
            # handling case for missig https certificate
            if self.endpoint.startswith('https'):
                ctx = ssl.create_default_context()
                ctx.check_hostname = False
                ctx.verify_mode = ssl.CERT_NONE
            else:
                ctx = None
            response = urlopen(req, context=ctx)
            return response.read().decode(response_enc)
        except HTTPError as e:
            print(e.read())
            print('')
            raise e

