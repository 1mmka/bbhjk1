from django.shortcuts import render,redirect
from app.models import Library
from django.views.generic import CreateView,ListView
from django.forms import modelform_factory
from django.db import transaction

# Create your views here.
custom_modelform = modelform_factory(Library,fields=('book_name','price'))

class CreateLibraryBook(CreateView):
    form_class = custom_modelform
    template_name = 'adding.html'
    success_url = 'listings'
    
    @transaction.atomic
    def post(self,request):
        with transaction.atomic():
            return redirect('listings')
                
def ListLibraryBook(request):
    books = Library.custom_object.published_or_not()
    return render(request, 'listing.html', {'dct': books})