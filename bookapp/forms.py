from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Book
from django.contrib.auth.forms import UserCreationForm


class BookCreateForm(ModelForm):
    class Meta:
          model = Book
          fields = "__all__"
class RegistrationForm(UserCreationForm):
      class Meta:
            model = User
            fields = ["username","email","password1","password2"]
