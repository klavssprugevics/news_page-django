from datetime import date
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db.models import Q

from .models import News
from .forms import NewsForm, SearchForm

# Create your views here.

# Sakuma skats
def home(request):

    # No musu sql datubazes izpildam query, kas ekvivalents - SELECT * FROM POST;
    data = News.objects.all().order_by('-date')[:5]


    # Redirecto lietotaju uz lapu un klat iedod http req datus
    return render(request, "index.html", {"posts":data})

# Visu rakstu skats ar filtraciju
def all_posts(request):

    # POST metode tiek izpildita tad, kad mes uzspiezam aiziet pogu
    if request.method == 'POST':

        # Izgustam formu no POST
        form = SearchForm(request.POST)
        if form.is_valid():

            # Sakotneji tiek atlasiti pilnigi visi raksti
            filtered_posts = News.objects.all().order_by('-date')

            keyword = form.cleaned_data['keyword']

            # Salidzinam, vai nosaukums, apraksts vai teksts nesatur atslegvardu - atlasam tos
            if keyword != "":
                filtered_posts = News.objects.filter(
                    Q(title__contains=keyword) |
                    Q(description__contains=keyword) |
                    Q(text__contains=keyword))

            # Atlasam rakstus zem kategorijas, ja tada izveleta
            category = form.cleaned_data['category']           
            if category != "":
                filtered_posts = filtered_posts.filter(category=category)

            startDate = form.cleaned_data['startDate']
            endDate = form.cleaned_data['endDate']

            # Ja nav pieskirts startDate, tad tiek izvelets datums, kas pieder pasam pirmajam postam
            if startDate is None:
                first_post = News.objects.all().order_by('date')[0]
                first_post_date_obj = News._meta.get_field('date')
                startDate = first_post_date_obj.value_from_object(first_post)

            # Ja nav pieskirts endDate, tad to uzliekam par tagadni
            if endDate is None:
                endDate = date.today()

            # Atlasa tos rakstus, kas ir noraditaja laika intervala
            filtered_posts = filtered_posts.filter(date__date__range=[startDate, endDate]) 

            # Izvelas kartosanas secibu
            sort_order = form.cleaned_data['sort']
            if sort_order == "byOldest":
                filtered_posts = filtered_posts.order_by('date')
            else:
                filtered_posts = filtered_posts.order_by('-date')

        return render(request, 'all_posts.html', {"posts":filtered_posts})

    else:
        all_posts = News.objects.all().order_by('-date')
        return render(request, "all_posts.html", {"posts":all_posts})


# Individuala raksta skats
def post(request, slug):
    
    # No musu sql datubazes izpilda m query, kas ekvivalents - SELECT * FROM POST WHERE slug = this.slug;
    data = News.objects.get(slug=slug)

    # Papildus panemam no datubas 3. jaunakos postus saja kategorija, lai pievienotu kaa ieteicamos
    related_posts = News.objects.filter(category=data.category).order_by('-date').exclude(slug=slug)[:3]

    return render(request, 'post_view.html', {'post':data, 'related':related_posts})


# Izdzes rakstu ar noteikto slug
def delete_post(request, post_id=None):

    post_to_delete = News.objects.get(slug=post_id)
    post_to_delete.delete()
    return HttpResponseRedirect('/')


# Atlasa konkreta raksta datus un tos izmaina pie POST
def edit_post(request, post_id=None):

    news_post = News.objects.get(slug=post_id)
    post = NewsForm(instance=news_post)

    if request.method == 'POST':
        post = NewsForm(request.POST, request.FILES, instance=news_post)
        if post.is_valid():
            post.save()
            return HttpResponseRedirect('/')

    return render(request, 'edit_post.html', {'form':post})


# No POST formas panem datus un izveido raksta objektu
def new_post(request):

    # need to process form data
    if request.method == 'POST':

        # creates form instance and populates it
        post = NewsForm(request.POST, request.FILES)

        # If valid, redirect user
        if post.is_valid():
            post.save()
            
            return HttpResponseRedirect('/')
    # if user visits site (GET METHOD) - just render a blank form
    else:
        post = NewsForm()
    
    return render(request, 'add_post.html', {'form':post})
