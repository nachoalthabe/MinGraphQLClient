"""Module contains flask server with minimanl GraphQL schema for test purposes"""

import argparse
import graphene


from contextlib import closing
from flask import Flask, request
from flask_graphql import GraphQLView

def shutdown_server():
    """Shut down the server."""

    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

class Person(graphene.ObjectType):
    """Class to populate GraphQL test endpoint."""

    id = graphene.ID()
    name = graphene.String()
    surname = graphene.String()
    age = graphene.Int()
    employed = graphene.Boolean()


class Query(graphene.ObjectType):
    """Graphene Query object."""

    person = graphene.Field(Person)
    
    def resolve_person(self, args, context, info):
        return Person(id=1, name='James', surname='Smith', age=33, employed=True)

view_func = GraphQLView.as_view('graphql', schema=graphene.Schema(query=Query))
app = Flask(__name__)
app.add_url_rule('/graphql', view_func=view_func)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__=='__main__':
    """
    Run local server on port provided via command-line arguments
    Run on 5000 post if port was not provided
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '-port', type=int, help='specify port to run server on')
    args = parser.parse_args()
    
    if args.p:
        app.run(port=args.p)
    else:
        app.run()
