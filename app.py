from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from database import load_engine, create_all_tables
import logging

logging.basicConfig(encoding="utf-8", level=logging.INFO)


def hello_world(request):
    return Response("Hello World!")


def load_app():
    """Returns the wsgi application from pyramid"""
    with Configurator() as config:
        config.add_route("hello", "/")
        config.add_view(hello_world, route_name="hello")
        return config.make_wsgi_app()


def main():
    """Returns the WSGI APP and the database engine object
    :rtype: object
    """
    app = load_app()
    engine = load_engine()
    create_all_tables(engine)
    return app, engine


# Primary main method. Loads the app and the engine
if __name__ == "__main__":
    app, engine = main()
    logging.info("loading-app-and-engine")
    server = make_server("0.0.0.0", 6543, app)
    logging.info("http-server-started")
    server.serve_forever()
