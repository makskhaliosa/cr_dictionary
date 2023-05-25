from django.urls import path
from . import views

app_name = 'search_words'

urlpatterns = [
    path('', views.index, name='index'),
    path('search_result/', views.search_result, name='search_result'),
    path('character_create/', views.character_create, name='character_create'),
    path('<str:character>/', views.character_page, name='character_page'),
    path(
        '<str:character>/character_edit/',
        views.character_edit,
        name='character_edit'
    ),
]
