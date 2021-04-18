from django.shortcuts import render
from .models import News


# Create your views here.

def home(request):

    # No musu sql datubazes izpildam query, kas ekvivalents - SELECT * FROM POST;
    data = News.objects.all()

    # Redirecto lietotaju uz lapu un klat iedod http req datus
    return render(request, "index.html", {"posts":data})

def post(request, slug):
    
    # No musu sql datubazes izpilda m query, kas ekvivalents - SELECT * FROM POST WHERE slug = this.slug;
    data = News.objects.get(slug=slug)

    return render(request, 'postview.html', {'post':data})
