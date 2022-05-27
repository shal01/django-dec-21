from django.shortcuts import render,redirect
from book.models import Boooks
from book.forms import BookForm
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
# Create your views here.
# django.views.generic.CreateView.EditView.DeleteView.UpdateView


from django.urls import reverse_lazy

class BookCreateView(CreateView):
    model = Boooks
    form_class = BookForm
    template_name = "book_add.html"
    success_url = reverse_lazy("all-list")



class BookListView(ListView):
    model = Boooks
    template_name = "book_list.html"
    context_object_name ='books'              #used for to override context_list_view as {'form'}

class BookDetailView(DetailView):
    model=Boooks
    template_name = "book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"


class BookEditView(UpdateView):
    model = Boooks
    form_class = BookForm
    template_name = "book-edit.html"
    success_url = reverse_lazy("all-list")
    pk_url_kwarg = "id"


def bookdelete(request,*args,**kwargs):
    id=kwargs.get('id')
    Boooks.objects.get(id=id).delete()
    return redirect('all-list')






# book_create
# edit
# delete
# list
# detail
