from pyramid.config import Configurator
from .constants import *

def main(args):
    with Configurator() as config:
        config.include('pyramid_debugtoolbar')
        config.add_route(HOME, HOME_PATH)
        config.add_route(HELLO,HELLO_PATH)
        config.add_route('%s_json' % (HELLO),'%s.json' % (HELLO_PATH))
        config.scan('.views')
        return config.make_wsgi_app()
    

if __name__ == '__main__':
    main()