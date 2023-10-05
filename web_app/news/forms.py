from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Articles, Comment
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
        }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
        }),

            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            })
        }


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['body']