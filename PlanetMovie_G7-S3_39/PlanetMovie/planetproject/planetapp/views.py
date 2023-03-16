from django.shortcuts import render,redirect
from .models import PostModel,Comment,FavFilm
from .models import Movie4,User
from django.contrib import messages
import csv
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django_cassandra_engine.sessions.models import Session
import uuid
from collections import defaultdict
from django.shortcuts import get_object_or_404






def home(request,page=1) :
    data = sorted(list(Movie4.objects.all()) , key=lambda p: p.year_of_prod)
    return render(request, 'index.html' , context={'posts': data})


def search(request):
    if 'q' in request.GET:
        q = request.GET['q']

        data= Movie4.objects.filter(title=q)
    else : 
        data = sorted(list(Movie4.objects.all()) , key=lambda p: p.year_of_prod)
        #we stored all the data in the database in this list  sorte it by date then we sent that data into the index.html using the 'Postskey 
    return render(request, 'search.html' , context={'posts': data})



def load_more(request):
    page = request.GET.get('page', 1)
    items_per_page = 3
    data = Movie4.objects.all().limit(page * items_per_page)[:items_per_page]
    return JsonResponse({'data': data})


def allfilms(request) : 
    films = Movie4.objects.all()
    category_count = defaultdict(int)
    for film in films:
        category_count[film.category] += 1
    nbr = Movie4.objects.all().count()
    return render(request, 'admin.html' , {'nbr': nbr,'category_count':category_count})





def posts(request,pk) :
    post=PostModel.objects.get(id=pk)
    return render(request ,'showblog.html' , {'posts':post})

def movies(request,film_id):
    movie=Movie4.objects.get(pk=film_id)
    comments = Comment.objects.filter(film_id=movie.idfilm)
    current_films = Movie4.objects.get(idfilm=film_id)
    recommended_films = Movie4.objects.filter(category=current_films.category).exclude(idfilm=film_id)
    return render(request,'movie.html' ,{'movies':movie,'comments': comments,'recommended_films':recommended_films})








def newblog(request):
    if request.method == 'POST' :
        title = request.POST['title']
        body = request.POST['body']
        new_blog = PostModel.objects.create(title=title , body=body) #the title of the fome equals to the value fo the attribte in the database
        new_blog.save
       
        return redirect('blog')     #once saved redirect the user to his own page

    else :

        return render(request, 'newblog.html')

def update_blog(request,pk):
    if request.method == 'POST' :
        title = request.POST['title']
        body = request.POST['body']
        new_blog = PostModel.objects(id=pk).update(title=title , body=body) #the title of the fome equals to the value fo the attribte in the database
       
        return redirect('blog')     #once saved redirect the user to his own page

    else :
        

        return render(request, 'update_blog.html')

def updatef(request,film_id):
    film = Movie4.objects.get(pk=film_id)

    return render(request, 'update_movie.html', {'film': film})



def updatefilm(request,film_id):
    if request.method == 'POST':
        title = request.POST['title']
        status=request.POST['status']
        image = request.POST['image']
        category = request.POST['category']
        language = request.POST['language']
        year_of_prod = request.POST['year_of_prod']
        views_nb = request.POST['views_nb']
        video_id = request.POST['video_id']
        duration = request.POST['duration']
        description = request.POST['description']
        new_movie = Movie4.objects(idfilm=film_id).update(title=title ,category=category, image=image,language=language,year_of_prod=year_of_prod,views_nb=views_nb,status=status,video_id=video_id,duration=duration,description=description) #the title of the fome equals to the value fo the attribte in the database

       
        return redirect('admin')     #once saved redirect the user to his own page
   

def delete_blog(request, id):
  post= PostModel.objects.get(pk=id)
  post.delete()
  return redirect(('blog'))


def dell_fav(request,film_id):
    fav = get_object_or_404(FavFilm,film_id=film_id,user_id=request.session['username'])
    fav.delete()


    return redirect('favorite_films')





def deletefilm(request, film_id) :
    film=Movie4.objects.get(idfilm=film_id)
    film.delete()
    return redirect(('admin'))


def film(request) :
    return render(request,'film.html')

def favorites(request) :
    return render (request ,'favrt.html')

def categories(request) :
    return render(request , 'categories.html')

def blog(request) :
    posts_list = sorted(list(PostModel.objects.all()) , key=lambda p: p.created_at) #we stored all the data in the database in this list  sorte it by date then we sent that data into the index.html using the 'Postskey 
    return render(request, 'blog.html' , {'posts': posts_list})


def cat1(request):
    movies=Movie4.objects.filter(category='Comedy')
    context={'movies':movies}
    return render(request,'filter.html',context)

def cat2(request):
    movies=Movie4.objects.filter(category='Drama')
    context={'movies':movies}
    return render(request,'filter.html',context)

def cat3(request):
    movies=Movie4.objects.filter(category='Action')
    context={'movies':movies}
    return render(request,'filter.html',context)

def cat4(request):
    movies=Movie4.objects.filter(category='Animation')
    context={'movies':movies}
    return render(request,'filter.html',context)

def cat5(request):
    movies=Movie4.objects.filter(category='Animal')
    context={'movies':movies}
    return render(request,'filter.html',context)

def cat(request):
    movies=Movie4.objects.all()
    context={'movies':movies}
    return render(request,'filter.html',context)



def cat6(request):
    movies=Movie4.objects.filter(category='Bibliography')
    context={'movies':movies}
    return render(request,'filter.html',context)

def cat7(request):
    movies=Movie4.objects.filter(category='Adventure')
    context={'movies':movies}
    return render(request,'filter.html',context)




def Movie4csv(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition'] ='attachment ; filename=Movie4.csv'
    writer=csv.writer(response)
    movies=Movie4.objects.all()

    writer.writerow(['idfilm','title','category','views_nb'])
    for movie in movies:
        writer.writerow([movie.idfilm,movie.title,movie.category,movie.views_nb])

    return response





   

def year_2022(request):
    movies=Movie4.objects.filter(year_of_prod__in=[2022])
    context={'movies':movies}
    return render(request,'filter.html',context)

def year_2020_2021(request):
    movies=Movie4.objects.filter(year_of_prod__in=[2020,2021])
    context={'movies':movies}
    return render(request,'filter.html',context)

def year_2010_2019(request):
    movies=Movie4.objects.filter(year_of_prod__in=[*range(2010,1*2019,1)])
    context={'movies':movies}
    return render(request,'filter.html',context)

def year_2000_2009(request):
    movies=Movie4.objects.filter(year_of_prod__in=[*range(2000,2009,1)])
    context={'movies':movies}
    return render(request,'filter.html',context)

def year_1980_1999(request):
    movies=Movie4.objects.filter(year_of_prod__in=[*range(1980,1999,1)])
    context={'movies':movies}
    return render(request,'filter.html',context)

def newest(request):
    movies=Movie4.objects.filter(year_of_prod__gte=2022)
    context={'movies':movies}
    return render(request,'filter.html',context)

def mostwatched(request):
    movies=Movie4.objects.filter(views_nb__gte=150000)
    context={'movies':movies}
    return render(request,'filter.html',context)

def toprated(request):
    movies=Movie4.objects.filter(status='Top Rated')
    context={'movies':movies}
    return render(request,'filter.html',context)
  
def addfilm(request):
    if request.method == 'POST' :
        status=request.POST['status']
        title = request.POST['title']
        image = request.POST['image']
        category = request.POST['category']
        language = request.POST['language']
        year_of_prod = request.POST['year_of_prod']
        views_nb = request.POST['views_nb']
        video_id=request.POST['video_id']
        duration=request.POST['duration']
        description=request.POST['description']
        new_movie = Movie4(idfilm=uuid.uuid4() ,title=title ,category=category, image=image,language=language,year_of_prod=year_of_prod,views_nb=views_nb,status=status,video_id=video_id,duration=duration,description=description) #the title of the fome equals to the value fo the attribte in the database
        new_movie.save()
       
        return redirect('home')     #once saved redirect the user to his own page

    else :

        return render(request, 'addfilm.html')
    

def admin(request) :
    films = Movie4.objects.all()

    # Count the number of films per category
    category_counts = {}
    for film in films:
        if film.category in category_counts:
            category_counts[film.category] += 1
        else:
            category_counts[film.category] = 1
    categories = list(category_counts.keys())
    counts = list(category_counts.values())
  
    
    if 'q' in request.GET:
        q = request.GET['q']
        film_list= Movie4.objects.filter(title=q)
    else : 
        film_list = sorted(list(Movie4.objects.all()) , key=lambda p: p.year_of_prod)
    
    return render(request, 'admin.html' , {'films': film_list,  'categories': categories,
        'counts': counts})


def load_more(request):
    page = request.GET.get('page')
    movies = Movie4.objects.all()[page*3:(page+1)*3]
    return render(request, 'index.html', {'posts': movies})

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            user = User.objects.get(username=username)
            return render(request, 'register.html', {'error': 'Username already exists'})
        except User.DoesNotExist:
            user = User(username=username, password=password, email=email)
            user.save()
            request.session['username'] = username
            return redirect('signin')
    return render(request, 'register.html')




def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username, password=password)
            request.session['username'] = username
            if user.username=='admin1':
                err=user.username
            else:
                err=''

            return render(request, 'index.html',{'err':err} )



        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid login credentials'})
    return render(request, 'login.html')


def signout(request):
    if 'username' in request.session:
        del request.session['username']
    return redirect('signin')



def add_comment(request, film_id):
    if request.method == 'POST':
        film = Movie4.objects.get(pk=film_id)

        comm = request.POST['comment']
        user_id = request.session['username']
        film_id = film.idfilm
        comment = Comment(id=uuid.uuid4(), user_id=user_id, film_id=film_id, text=comm)
        comment.save()
        return redirect('movies', film_id=film_id)
    
    return render(request, 'movie.html')





def add_fav(request, film_id):
    film = Movie4.objects.get(pk=film_id)

    user_id = request.session['username']
    film_id = film.idfilm
    fav=FavFilm(id=uuid.uuid4(),user_id=user_id, film_id=film_id)
    fav.save()
    
    return redirect('home')

def favorite_films(request):
    user_id = request.session['username']

    favorites = FavFilm.objects.filter(user_id=user_id)
    films = []
    for favorite in favorites:
        films.append(Movie4.objects.get(pk=favorite.film_id))
    return render(request, 'myfav.html', {'posts': films,'err':'Vous avez pas encore de films favoris !' })