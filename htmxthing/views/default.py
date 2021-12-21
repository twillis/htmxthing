from pyramid.view import view_config


@view_config(route_name='home', renderer='htmxthing:templates/mytemplate.jinja2')
def my_view(request):
    # from ..models import User
    # from ..security import hash_password
    # import transaction
    # user = User(email="tom.willis@gmail.com", password=hash_password("Password123$"))
    # request.dbsession.add(user)
    # transaction.commit()
    return {}
