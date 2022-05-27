from django.db import models
from django.contrib.auth.models import User


# Create your models here.
#ORM - Object Relational mappers
#ORM for creating a resource




class Todos(models.Model):
  task_name=models.CharField(max_length=120)
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  date=models.DateField(auto_now_add=True)
  status=models.BooleanField(default=False)

  def __str__(self):
    return self.task_name


class UserProfile(models.Model):
  user=models.OneToOneField(User,on_delete=models.CASCADE)
  profile_pic=models.ImageField(upload_to="images")
  date_of_field=models.DateField(null=True)
  phone_no=models.CharField(max_length=12)











# ORM queries
# Object relational  mapper
# ORM querry for creating a resources
# ref_name=model_name(field1="value",field2="value2"..)
# ref_name.save()

#  ORM query for fetching all records
 # ref_name=model_name.objects.all
 #qs=todos.objects.all()
 #Filtering ORM Query
 # qs=Todos.objects.filter(status=True)
 # qs=todos.objects.all().exclude(user="user1")

# get is used to find a specific todo object
# qs=Todos.objects.get(id=4)

# Update:-
#  todo=Todos.objects.get(id=1)
 # todo.task_name="ebill"

 # delete : -

 # todos.objects.get(id=2).delete()   dont need any extra variable to store

