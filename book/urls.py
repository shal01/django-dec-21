from django.urls import path
from book import views

urlpatterns=[
    path("add",views.BookCreateView.as_view(),name="add-book"),
    path("all",views.BookListView.as_view(),name="all-list"),
    path("detail/<int:id>",views.BookDetailView.as_view(),name="details-book"),
    path("change/<int:id>",views.BookEditView.as_view(),name="edit-book"),
    path("remove/<int:id>",views.bookdelete,name="delete")
]