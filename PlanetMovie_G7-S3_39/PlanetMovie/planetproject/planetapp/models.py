
from django.db import models
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
import uuid
from datetime import datetime


# Create your models here.

class PostModel (DjangoCassandraModel):
   
        
    id = columns.UUID(primary_key=True, default = uuid.uuid4) 
    title = columns.Text(required=True)
    body = columns.Text(required=True)
    created_at = columns.DateTime(default = datetime.now)
    




CATEGORY_CHOICES = (
    {'A','ACTION'},
    {'D','DRAMA'},
    {'C','COMEDY'},
    {'R','ROMANCE'},
    {'H','HORROR'},
    {'F','FICTION'},
    {'N','ANIMATION'},
)
LANGUAGE_CHOICES = (
    {'EN','ENGLISH'},
    {'FR','FRENCH'},
    {'KB','KABYLE'},
    {'AR','ARABIC'},
    {'GR','GERMAN'},
    
)
STATUS_CHOICES = (
    {'RA','RECENTLY ADDED'},
    {'MW','MOST WATCHED'},
    {'TR','TOP RATED'},
)



class Movie4(DjangoCassandraModel):
    idfilm=columns.UUID(primary_key=True , default = uuid.uuid4)
    title=columns.Text(max_length=200,required=True)
    image=columns.Text(required=False)
    category=columns.Text(required=True)
    status=columns.Text(required=True)
    language=columns.Text(required=True)
    year_of_prod=columns.Integer(required=True)
    added_at=columns.DateTime(default=datetime.now)
    views_nb=columns.Integer()
    duration=columns.Text(required=True)
    description=columns.Text(required=True)
    video_id=columns.Text(required=True)
    partition_key = ['category,idfilm']






class User(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    username = columns.Text()
    password = columns.Text()
    email = columns.Text()




class Comment(DjangoCassandraModel):
    id = columns.UUID(primary_key=True, default=uuid.uuid4)
    text = columns.Text()
    user_id = columns.Text()
    film_id = columns.UUID()
    added_at=columns.DateTime(default=datetime.now)

class FavFilm(DjangoCassandraModel):
    class meta:
        get_pk_field='id'


    id = columns.UUID(primary_key=True,partition_key=True, default=uuid.uuid4)
    user_id = columns.Text()
    film_id = columns.UUID()
    added_at=columns.DateTime(default=datetime.now)

