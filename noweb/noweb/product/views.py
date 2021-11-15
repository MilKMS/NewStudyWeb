import os
from django.contrib import admin

from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic.base import View, TemplateView
from django.views.generic.detail import SingleObjectMixin
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse, response, HttpResponse, Http404
from django.conf import settings
from django.utils.decorators import method_decorator

# from django.http import StreamingHttpResponse

# from WSGIREF.UTIL import FileWrapper
# import mimetypes
# import os

from .models import Product
from users.decorators import login_required, admin_required
from users.models import Users
# from .forms import FileHandlerForm

# Create your views here.

@method_decorator(login_required, name='dispatch')
class ProductList(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_list'

@method_decorator(admin_required, name='dispatch')
class VideoList(ListView):
    model = Product
    template_name = 'download.html'
    context_object_name = 'product_list'


@method_decorator(login_required, name='dispatch')
class VideoDownload(SingleObjectMixin, View):
    queryset = Product.objects.all()

    def get(self, request, document_id):
        object = self.get_object(document_id)
        
        if request.user.point >= object.price:
            file_path = object.attached.path
            file_type = object.content_type
            fs = FileSystemStorage(file_path)
            response = FileResponse(fs.open(file_path, 'rb'), content_type=file_type)
            response['Content-Disposition'] = f'attachment; filename={object.get_filename()}'
            
            return response


@method_decorator(admin_required, name='dispatch')
def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)

    user = request.session.get('user')
    data = Users.objects.all( email=user )
    print(data)


    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

    raise Http404
