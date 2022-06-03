from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import movieForm
from .models import movie

# Create your views here.
def index(request):
    movies=movie.objects.all()
    context={
        'movie_list' :movies
    }
    return  render(request, 'index.html', context)
def movie_detail(request,movie_id):
    item=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'movie': item})
def add_movie(request):
    if request.method=='POST':
        name=request.POST.get('movie_name',)
        year = request.POST.get('movie_year', )
        desc = request.POST.get('movie_desc', )
        img = request.FILES['movie_img']
        from .models import movie
        movie=movie(movie_name=name, Movie_year=year, movie_desc=desc,movie_img=img)
        movie.save()
    return render(request,'add.html')

def update(request,id):
    movies=movie.objects.get(id=id)
    form=movieForm(request.POST or None, request.FILES, instance=movies)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form': form, 'movie': movies})

def delete(request,id):
    if request.method=='POST':
        movies=movie.objects.get(id=id)
        movies.delete()
        return redirect('/')
    return render(request,'delete.html')