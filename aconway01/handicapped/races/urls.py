from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

app_name = 'races'

urlpatterns = [
    path('', views.home, name="home"),
    path('races/<str:racedate>/<str:trackid>/', views.view_races, name="view_races"),
    path('races/<str:racedate>/<str:trackid>/<str:racenumber>/',
         views.view_race, name="view_race"),
]
