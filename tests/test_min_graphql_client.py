import requests
import socket
import subprocess
import time
import unittest

#for nested exception handling in setUp
#from urllib3.exceptions import NewConnectionError, MaxRetryError
from flask import url_for
from contextlib import closing

from tests import testing_server
from mingraphqlclient.min_graphql_clinet import MinGraphQLClient

class GraphQLTestCase(unittest.TestCase): 
    
    def setUp(self): 
        """Call before every test case."""
        self.free_port = str(self.get_free_port())
        # supbrocess to Anki
        process = subprocess.Popen('python tests/testing_server.py -port ' + self.free_port, shell=True)

        #waiting up to 5 seconds, for local test server to start
        for i in range(5):
            try:
                requests.get('http://127.0.0.1:'+ self.free_port)
                break
            # TODO nested exception proper handling
            #except (ConnectionError, ConnectionRefusedError, NewConnectionError, MaxRetryError):
            except:
                time.sleep(0.25)

        graphql_endpoint = 'http://127.0.0.1:'+ self.free_port + '/graphql'
        self.graphql_client = MinGraphQLClient(graphql_endpoint)

    def tearDown(self):
        """Call after every test case."""
        
        requests.post("http://127.0.0.1:" + self.free_port + "/shutdown")

    def testBasic(self):
        """Basic test case."""
        
        graphql_response = self.graphql_client.execute('''
  query {
    person{
        id
        name
        surname
        age
        employed
    }
  }
''')
        self.assertTrue('James' in graphql_response)

    def get_free_port(self):
        """
        Get unoccupied network port.

        :returns: number of unoccupied network port
        :rtype: int
        """
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            sock.bind(('', 0))
            return sock.getsockname()[1]
