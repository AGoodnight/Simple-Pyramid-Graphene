from pyramid.config import Configurator

from sqlalchemy import engine_from_config

from .constants import *

from .models import DBSession, Base


def main(global_config, **settings):
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.prepare(autoload_with=engine)
    Base.metadata.bind = engine

    config = Configurator(settings=settings)
    config.include('pyramid_tm')
    config.include('pyramid_debugtoolbar')
    config.add_route(HOME, HOME_PATH)
    config.add_route(HELLO,HELLO_PATH)
    config.add_route('%s_json' % (HELLO),'%s.json' % (HELLO_PATH))
    config.scan('.views')
    return config.make_wsgi_app()
    

if __name__ == '__main__':
    main()