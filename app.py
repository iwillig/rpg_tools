from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from database import load_engine, create_all_tables


def hello_world(request):
    return Response('Hello World!')


def load_app():
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        ## Is this the right way to handle local vars in python?
        app = config.make_wsgi_app()
    return app

if __name__ == '__main__':
    app = load_app()
    engine = load_engine()
    create_all_tables(engine)
    print("server-start", engine)

    server = make_server('0.0.0.0', 6543, app)

    server.serve_forever()