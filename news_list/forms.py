from django import forms
from django.forms import ModelForm
from news_list.models import News

# https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'author', 'thumbnail', 'category', 'description', 'text']

class SearchForm(forms.Form):

    keyword = forms.CharField(label='keyword', max_length=20, required=False)
    category = forms.CharField(label='category', required=False)
    sort = forms.CharField(label='sort', required=False)
    startDate = forms.DateField(label='startDate', required=False)
    endDate = forms.DateField(label='endDate', required=False)
