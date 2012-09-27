from functools import wraps

from django.http import Http404

def only_staff_member(view_func):
    """
    Decorator for views that checks that the user is logged in and is a staff
    member, displaying a 404 page if necessary
    """
    @wraps(view_func)
    def _checklogin(request, *args, **kwargs):
        if request.user.is_active and request.user.is_staff:
            return view_func(request, *args, **kwargs)
        raise Http404
    return _checklogin
