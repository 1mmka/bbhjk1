from django.urls import path
from app.views import CreateLibraryBook,ListLibraryBook

urlpatterns = [
    path('',CreateLibraryBook.as_view(),name='home-page'),
    path('listings',ListLibraryBook,name='listings')
]