import bcrypt
from pyramid.authentication import AuthTktCookieHelper
from .models import User

def hash_password(pw):
    pwhash = bcrypt.hashpw(pw.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8')


def check_password(pw, hashed_pw):
    expected_hash = hashed_pw.encode('utf8')
    return bcrypt.checkpw(pw.encode('utf8'), expected_hash)

def get_user_by_id(session, user_id):
    return session.query(User).filter_by(id=user_id).one_or_none()

IDENTITY_KEY='userid'

class SecurityPolicy:
    def __init__(self, secret):
        self.authtkt = AuthTktCookieHelper(secret=secret)

    def identity(self, request):
        identity = self.authtkt.identify(request)
        if identity is not None:
            return identity

    def authenticated_userid(self, request):
        identity = self.identity(request)
        if identity is not None and get_user_by_id(request.dbsession, identity[IDENTITY_KEY]):
            return identity[IDENTITY_KEY]

    def remember(self, request, userid, **kw):
        return self.authtkt.remember(request, userid, **kw)

    def forget(self, request, **kw):
        return self.authtkt.forget(request, **kw)
