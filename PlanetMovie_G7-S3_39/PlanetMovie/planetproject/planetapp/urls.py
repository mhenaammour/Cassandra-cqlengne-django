from django.urls import path
from .import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('film',views.film,name='film'),

    path('categories' , views.categories , name = 'categories'),
    path('blog' , views.blog, name='blog'),
    path('admin' , views.admin, name='admin'),
    path('search' , views.search, name='search'),
    path('newblog' , views.newblog, name='newblog'),
    path('cat' , views.cat, name='cat'),
    path('cat1' , views.cat1, name='cat1'),
    path('cat2' , views.cat2, name='cat2'),
    path('cat3' , views.cat3, name='cat3'),
    path('cat4' , views.cat4, name='cat4'),
    path('cat5' , views.cat5, name='cat5'),
    path('cat6' , views.cat6, name='cat6'),
    path('cat7' , views.cat7, name='cat7'),
    path('year_2020_2021',views.year_2020_2021,name='year_2020_2021'),
    path('year_2010_2019',views.year_2010_2019,name='year_2010_2019'),
    path('year_2000_2009',views.year_2000_2009,name='year_2000_2009'),
    path('year_1980_1999',views.year_1980_1999,name='year_1980_1999'),
    path('year_2022' , views.year_2022, name='year_2022'),
    path('posts/<str:pk>',views.posts , name ='posts'),
    path('movies/<uuid:film_id>',views.movies , name ='movies'),
    path('posts/update_blog/<str:pk>',views.update_blog , name ='update_blog'),
    path('posts/delete_blog/<str:id>',views.delete_blog , name ='delete_blog'),
    path('deletefilm/<uuid:film_id>',views.deletefilm , name ='deletefilm'),
    path('movie4_csv',views.Movie4csv,name="movie4_csv"),
    path('signin',views.signin,name="signin"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
    
    path('newest',views.newest,name='newest'),
    path('mostwatched',views.mostwatched,name='mostwatched'),
    path('toprated',views.toprated,name='toprated'),
    path('load-more/', views.load_more, name='load-more'),
    path('addfilm' , views.addfilm, name='addfilm'),
    path('posts/<uuid:film_id>/add_comment/', views.add_comment, name='add_comment'),
    path('fav/<uuid:film_id>/add_to_fav/', views.add_fav, name='add_fav'),
    path('myfav' , views.favorite_films, name='favorite_films'),
    path('dellfav/<uuid:film_id>/', views.dell_fav, name='dell_fav'),
    path('updatefilm/<uuid:film_id>',views.updatefilm , name ='updatefilm'),
    path('update/<uuid:film_id>',views.updatef , name ='updatef'),



    








]