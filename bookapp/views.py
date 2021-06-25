from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.urls import reverse_lazy

from .forms import BookCreateForm, RegistrationForm
from django.views.generic import TemplateView, CreateView, ListView, UpdateView,DetailView,DeleteView
from .models import Book

# Create your views here.
class DBookCreateView(CreateView):
      model = Book
      form_class = BookCreateForm
      template_name = "createbook.html"
      success_url = reverse_lazy("list")
class DBookListView(ListView):
      model = Book
      template_name = "listbook.html"
      context_object_name = "books"
class DBookUpdateView(UpdateView):
      template_name = "updatebook.html"
      form_class = BookCreateForm
      model = Book
      success_url = reverse_lazy("dlist")
class DBookDetailView(DetailView):
      model = Book
      template_name = "bookdetaill.html"
      context_object_name = "book"
class DBookDeleteView(DeleteView):
      model = Book
      template_name = "delete.html"
      success_url = reverse_lazy("list")
class UserRegistrationView(CreateView):
      model = User
      form_class = RegistrationForm
      template_name = "registration.html"
      success_url = reverse_lazy("login")

class LoginView(TemplateView):
    model = User
    template_name = "login.html"

    def get(self, request,*args,**kwargs):
        return render(request, self.template_name)
    def post(self, request, *args,**kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user:
            print("succsess***")
            return redirect("list")
        else :
            print("failed****")
            return render(request,self.template_name)









class BookCreateView(TemplateView):
    model = Book
    form_class=BookCreateForm
    template_name = "createbook.html"
    context={}
    def get (self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(request, self.template_name,self.context)
    def post (self,request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            print("*******saved")
            # return render(request, self.template_name, self.context)
            return redirect("list")
class BookListView(TemplateView):
    model = Book
    template_name = "listbook.html"
    context = {}
    def get(self,request,*args,**kwargs):
        books = self.model.objects.all()
        self.context["books"] = books
        return render(request, self.template_name, self.context)
# update views
class GetobjectMixin:
    def get_object(self, id):

      return self.model.objects.get(id=id)
class BookUpdateView(TemplateView,GetobjectMixin):
    model = Book
    form_class = BookCreateForm
    template_name ="updatebook.html"
    context = {}
    # def get_object(self,id):
    #     return self.model.objects.get(id=id)
    def get(self,request,*args,**kwargs):
        # id =kwargs.get("pk")
        # book = self.model.objects.get(id=id)
        book = self.get_object(kwargs.get("pk"))
        form= self.form_class(instance=book)
        self.context["form"]=form
        return render(request, self.template_name, self.context )
    def post(self,request,*args,**kwargs):
        book = self.get_object(kwargs.get("pk"))
        form = self.form_class(instance=book,data=request.POST)
        if form.is_valid():
           form.save()
        return redirect("list")
class BookDetailView(TemplateView,GetobjectMixin):
      model = Book
      template_name = "bookdetaill.html"
      context = {}
      def get(self,request,*args,**kwargs):
          book = self.get_object(kwargs.get("pk"))
          self.context["book"] = book
          return render(request, self.template_name, self.context)
class BookDeleteView(TemplateView,GetobjectMixin):
      model = Book
      def get(self,request,*args,**kwargs):
          book = self.get_object(kwargs.get("pk"))
          book.delete()
          return redirect("list")


