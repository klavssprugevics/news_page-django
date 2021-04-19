from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import News
from .forms import NewsForm

# Create your views here.

def home(request):

    # No musu sql datubazes izpildam query, kas ekvivalents - SELECT * FROM POST;
    data = News.objects.all().order_by('-date')[:5]

    # Redirecto lietotaju uz lapu un klat iedod http req datus
    return render(request, "index.html", {"posts":data})

def post(request, slug):
    
    # No musu sql datubazes izpilda m query, kas ekvivalents - SELECT * FROM POST WHERE slug = this.slug;
    data = News.objects.get(slug=slug)

    # Papildus panemam no datubas 3. jaunakos postus saja kategorija, lai pievienotu kaa ieteicamos
    related_posts = News.objects.filter(category=data.category).order_by('-date').exclude(slug=slug)[:3]

    
    return render(request, 'postview.html', {'post':data, 'related':related_posts})

def new_post(request):

    # need to process form data
    if request.method == 'POST':

        # creates form instance and populates it
        post = NewsForm(request.POST, request.FILES)

        # If valid, redirect user
        if post.is_valid():
            post.save()
            
            # TODO: Redirect to all posts
            return HttpResponseRedirect('/')
    # if user visits site (GET METHOD) - just render a blank form
    else:
        post = NewsForm()

    
    return render(request, 'add_post.html', {'form':post})
