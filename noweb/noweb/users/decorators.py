from django.shortcuts import redirect


from django.shortcuts import redirect

from .models import Users

def login_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap

def admin_required(function):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login')

        user = Users.objects.get(email=user)
        if user.point <= 0:
            return redirect('/product')

        return function(request, *args, **kwargs)
    
    return wrap
