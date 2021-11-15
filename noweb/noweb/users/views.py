from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.utils.decorators import method_decorator

from .forms import RegisterForm, LoginForm
from .decorators import login_required
# from product.forms import FileHandlerForm
from product.models import Product

# Create your views here.

# def index(request):
#     return render(request, 'index.html', { 'email' : request.session.get('user') })

@method_decorator(login_required, name='dispatch')
class IndexView(TemplateView):
    template_name = 'index.html'

    
    
# class IndexView(TemplateView):
#     template_name = 'index.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         get_files = Product.objects.all()

#         context = {'form': FileHandlerForm, 'get_file':get_files}
#         return context

#     def post(self, request, **kwargs):
#         context = {}
#         if request.method == 'POST':
#             form = FileHandlerForm(request.POST, request.FILES)

#             if form.is_valid():
#                 Product.objects.get_or_create(file_upload=form.cleaned_data.get('file_upload'))

#                 return redirect('users:index')
#             else:
#                 context['from'] = form
#         else:
#             context['form'] = form

#         return redirect('users:index')


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'

class LoginView(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        self.request.session['user'] = form.email

        return super().form_valid(form)
        
def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/login')