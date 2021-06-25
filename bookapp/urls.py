from django.urls import path
from django.views.generic import TemplateView

from .views import BookCreateView,BookListView,BookUpdateView,BookDetailView,\
    BookDeleteView,DBookCreateView,DBookListView,DBookUpdateView,\
    DBookDeleteView,UserRegistrationView,LoginView
urlpatterns =[
    path("create",BookCreateView.as_view(),name="create"),
    path("books",BookListView.as_view(),name="list"),
    path("books/<int:pk>",BookUpdateView.as_view(),name="update"),
    path("books/details/<int:pk>",BookDetailView.as_view(),name="detail"),
    # path("books/delete/<int:pk>)",BookDeleteView.as_view(),name="delete"),
    path("dbooks",DBookCreateView.as_view(),name="dcreate"),
    path("dbooks/list",DBookListView.as_view(),name="dlist"),
    path("dbooks/update<int:pk>",DBookUpdateView.as_view(),name="dupdate"),
    path("dbooks/view<int:pk>",DBookUpdateView.as_view(),name="ddetail"),
    path("dbooks/remove<int:pk>",DBookDeleteView.as_view(),name="delete"),
    # path("login",TemplateView.as_view(template_name="login.html"),name="login"),
    path("registration",UserRegistrationView.as_view(),name="register"),
    path("login",LoginView.as_view(),name="login"),
]
