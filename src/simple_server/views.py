#file -- views.py --
import logging
log = logging.getLogger(__name__)
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config, view_defaults
from .constants import * 

class SimpleServerViews:
    def __init__(self, request):
        self.request = request

    @view_config(route_name=HOME)
    def home(self):
        log.debug('in home view')
        return {'name': 'Home View'}

    @view_config(route_name=HELLO)
    @view_config(route_name='%s_json' % (HELLO), renderer='json')
    def hello(self):
        name = self.request.params.get('name', 'no name provided')
        log.debug('in hello view for %s' % (name))
        return { 'name': name } 