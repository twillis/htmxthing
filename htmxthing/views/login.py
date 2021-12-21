from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
)
from pyramid.view import (
    view_config,
    view_defaults,
)
from ..security import check_password
from ..models import User


@view_defaults(route_name='login')
class LoginView:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @property
    def dbsession(self):
        return self.request.dbsession

    def get_user_by_email(self, email):
        return self.dbsession.query(User).filter_by(email=email).one_or_none()

    @view_config(request_method='GET',
                 renderer='htmxthing:templates/login.jinja2')
    def index(self):
        login_url = self.request.route_url('login')
        referrer = self.request.url
        if referrer == login_url:
            referrer = '/'
        came_from = self.request.params.get('came_from', referrer)
        return dict(
            name='Login',
            message='',
            url=f'{self.request.application_url}/login',
            came_from=came_from,
            email='',
            password='',
        )

    @view_config(request_method='POST')
    def login(self):
        user = self.get_user_by_email(self.request.params['email'])

        if user and check_password(self.request.params['password'],
                                   user.password):
            headers = remember(self.request, user.id)
            return HTTPFound(
                headers=headers,
                location=self.request.params['came_from'],
            )

    @view_config(route_name='logout', request_method='POST')
    def logout(self):
        return HTTPFound(
            headers=forget(self.request),
            location=self.request.route_url('home'),
        )
