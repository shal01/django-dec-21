from django.urls import path
from todoapp import views

urlpatterns=[
path("add",views.TodoCreateView.as_view(),name="addtodo"),
path('all',views.TodoListView.as_view(),name="alltodos"),
path("detail/<int:id>",views.TodoDetails.as_view(),name="detail"),
path("edit/<int:id>",views.TodoEditView.as_view(),name="edit"),
path("remove/<int:id>",views.TodoDeleteView.as_view(),name="remove"),
path("account/signup",views.SignUpView.as_view(),name="signup"),
path("",views.SignInView.as_view(),name="sign-in"),
path("account/signout",views.signout,name="signout"),
path("profile",views.ProfileCreateView.as_view(),name="profile"),




]