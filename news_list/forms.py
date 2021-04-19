from django import forms
from django.forms import ModelForm
from news_list.models import News

# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'thumbnail', 'category', 'description', 'text']
