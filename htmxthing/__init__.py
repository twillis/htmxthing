from pyramid.config import Configurator
from .security import SecurityPolicy

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    with Configurator(settings=settings) as config:
        config.set_security_policy(
            SecurityPolicy(
                secret=settings['session_secret']
            ))
        config.include('pyramid_jinja2')
        config.include('.routes')
        config.include('.models')
        config.scan()
    return config.make_wsgi_app()
