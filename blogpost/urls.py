from django.urls import path
from . import views

urlpatterns=[
    path("", views.index, name="homepage"),
    path("create-post", views.createpost, name="createpost"),
    path("post-list", views.postlist, name="postlist"),
    path("post/<slug:slug>/", views.postdetails, name="postdetails"),


]