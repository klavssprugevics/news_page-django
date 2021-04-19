from django import forms
from django.forms import ModelForm
from news_list.models import News

# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'thumbnail', 'category', 'description', 'text']

# class NewsForm(forms.Form):

#     CATEGORIES = [
#         ('Sport', 'Sports'),
#         ('Technology', 'Technology'),
#         ('Culture', 'Culture'),
#         ('Other', 'Other')
#     ]

#     title = forms.CharField(label='Nosaukums', max_length=100)
#     author = forms.CharField(label='Autors', max_length=100)
#     thumbnail = forms.CharField(label='Attēls')
#     category = forms.ChoiceField(choices=CATEGORIES, widget=forms.RadioSelect)
#     description = forms.CharField(label='Apraksts', widget=forms.Textarea)
#     text = forms.CharField(label='Teksts', widget=forms.Textarea)
